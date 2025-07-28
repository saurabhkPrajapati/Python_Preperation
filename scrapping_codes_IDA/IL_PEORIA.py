import math

import scrapy
from scrapy.http import headers
from scrapy.utils.response import open_in_browser
import re

class Peoria(scrapy.Spider):
    name = 'peoria'
    start_date = '07/01/2021'
    end_date = '07/03/2021'
    headers = {
        # 'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.101 Safari/537.36'}
        'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
        'Accept-Encoding': 'gzip, deflate, br', 'Accept-Language': 'en-US,en;q=0.9', 'Connection': 'keep-alive',
        'Host': 'recorder.peoriacounty.org', 'Referer': 'https://recorder.peoriacounty.org/recorder/web/',
        'sec-ch-ua': '" Not;A Brand";v="99", "Google Chrome";v="91", "Chromium";v="91"', 'sec-ch-ua-mobile': '?0',
        'Sec-Fetch-Dest': 'document', 'Sec-Fetch-Mode': 'navigate', 'Sec-Fetch-Site': 'same-origin',
        'Sec-Fetch-User': '?1', 'Upgrade-Insecure-Requests': '1',
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36'
    }

    def start_requests(self):
        urls = "https://recorder.peoriacounty.org/recorder/web/"

        yield scrapy.Request(
            url=urls,
            callback=self.parse1,
            headers=self.headers,
            dont_filter=True,
            method="GET"
        )
    #click on disclaimer
    def parse1(self, response):
        # open_in_browser(response)
        yield scrapy.Request(
            url="https://recorder.peoriacounty.org/recorder/web/login.jsp?submit=I+Acknowledge",
            callback=self.parse2,
            dont_filter=True,
            method="GET",
            headers=self.headers,
        )
    #public login
    def parse2(self, response):
        # open_in_browser(response)
        data={'submit': 'Public Login', 'guest': 'true'}
        yield scrapy.FormRequest(
            url="https://recorder.peoriacounty.org/recorder/web/loginPOST.jsp",
            callback=self.parse3,
            formdata=data,
            dont_filter=True,
            method="POST",
            headers=self.headers,
            meta={'handle_httpstatus_list':[302]}
        )

    def parse3(self, response):
        # open_in_browser(response)
        data ={'RecordingDateIDStart': self.start_date, 'RecordingDateIDEnd': self.end_date,
               'BothNamesIDSearchType': 'Advanced Searching', 'GrantorIDSearchType': 'Basic Searching',
               'GranteeIDSearchType': 'Basic Searching', 'ShortDescIDSearchType': 'Starts With',
               'TractIndexIDSearchType': 'Starts With',
               'PropertyAddIDSearchType': 'Starts With', 'AllDocuments': 'ALL',
               'docTypeTotal': '287'}

        yield scrapy.FormRequest(
            url="https://recorder.peoriacounty.org/recorder/eagleweb/docSearchPOST.jsp",
            callback=self.parse4,
            formdata=data,
            dont_filter=True,
            method="POST",
            headers=self.headers,
            meta={'handle_httpstatus_list': [302]}
        )

    def parse4(self, response):

        for i in [self.parse5,self.parse5_]:
            yield scrapy.Request(
            url="https://recorder.peoriacounty.org/recorder/eagleweb/docSearchResults.jsp?searchId=0&page=1&pageSize=100&sort=RecordingDate&sort2=&dir=asc",
            callback=i,
            dont_filter=True,
            method="GET",
            headers=self.headers,

        )

    def parse5_(self, response):
        # open_in_browser(response)
        text = response.xpath("//span[@class='pagebanner']/text()").get()
        total = int(re.search('(\d*)\s*items', text).group(1))
        num = math.ceil(total/100)
        print(num)
        urlslist = [
                    "https://recorder.peoriacounty.org/recorder/eagleweb/docSearchResults.jsp?searchId=0&pageSize=100&page=2&sort=RecordingDate&sort2=&dir=asc",
                    "https://recorder.peoriacounty.org/recorder/eagleweb/docSearchResults.jsp?searchId=0&pageSize=100&page=3&sort=RecordingDate&sort2=&dir=asc"

        ]

        headers={'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
                 'Accept-Encoding': 'gzip, deflate, br', 'Accept-Language': 'en-US,en;q=0.9', 'Connection': 'keep-alive',
                 'Host': 'recorder.peoriacounty.org', 'Referer': 'https://recorder.peoriacounty.org/recorder/eagleweb/docSearchResults.jsp?searchId=0&page=1&pageSize=100&sort=RecordingDate&sort2=&dir=asc',
                 'sec-ch-ua': '" Not;A Brand";v="99", "Google Chrome";v="91", "Chromium";v="91"', 'sec-ch-ua-mobile': '?0', 'Sec-Fetch-Dest': 'document', 'Sec-Fetch-Mode': 'navigate', 'Sec-Fetch-Site': 'same-origin',
                 'Sec-Fetch-User': '?1', 'Upgrade-Insecure-Requests': '1',
                 'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36'}
        num=num+1
        for i in range(2,num):
        # for i in urlslist:
            yield scrapy.Request(
                    url= f"https://recorder.peoriacounty.org/recorder/eagleweb/docSearchResults.jsp?searchId=0&pageSize=100&page={i}&sort=RecordingDate&sort2=&dir=asc",
                    # url=i,
                    callback=self.parse5,
                    dont_filter=True,
                    method="GET",
                    headers=headers,

                )


    def parse5(self, response):
        open_in_browser(response)
        count=0
        text=response.xpath("//span[@class='pagebanner']/text()").get()
        total=re.search('(\d*)\s*items',text).group(1)
        print(total)
        Total_links=response.xpath(f"//strong/a[not(contains(text(),'*{total} results'))]/@href").getall()
        # print(Total_links)
        for i in Total_links:
            # count+=1
            # if count>20:
            #     break
            i=i.replace('../','')
            yield scrapy.Request(
                    url=f"https://recorder.peoriacounty.org/recorder/{i}",
                    # url="https://recorder.peoriacounty.org/recorder/eagleweb/viewDoc.jsp?node=DOC337S213",
                    callback=self.parse6,
                    dont_filter=True,
                    method="GET",
                    headers=self.headers,

                )

    def parse6(self, response):
        # open_in_browser(response)

        Document_Number= response.xpath("//span[text()='Document Number']/../span[2]/span/text()").get(default='')
        Book=response.xpath("//span[text()='Book']/../span[2]/span/text()").get(default='')
        Page=response.xpath("//span[text()='Page']/../span[2]/span/text()").get(default='')
        Confirmation=response.xpath("//span[text()='Confirmation #']/../span[2]/span/text()").get(default='')
        Recording_Date=response.xpath("//span[text()='Recording Date']/../span[2]/span/text()").get(default='')
        Number_Pages=response.xpath("//span[text()='Number Pages']/../span[2]/span/text()").get(default='')
        Total_Fees=response.xpath("//span[text()='Total Fees']/../span[2]/span/text()").get(default='')
        Document_Date=response.xpath("//span[text()='Document Date']/../span[2]/span/text()").get(default='')
        Consideration_Amount=response.xpath("//span[text()='Consideration Amount']/../span[2]/span/text()").get(default='')
        Return_Address=response.xpath("//legend[text()='Return Address']/../span[2]/span/text()").get(default='')
        Address_1=response.xpath("//span[text()='Address 1']/../span[2]/span/text()").get(default='')
        Address_2=response.xpath("//span[text()='Address 2']/../span[2]/span/text()").get(default='')
        City=response.xpath("//span[text()='City']/../span[2]/span/text()").get(default='')
        State=response.xpath("//span[text()='State']/../span[2]/span/text()").get(default='')
        Zip=response.xpath("//span[text()='Zip']/../span[2]/span/text()").get(default='')
        Mailback_Date=response.xpath("//span[text()='Mailback Date']/../span[6]/span/text()").get(default='')
        Grantors = ""
        try:
            for i in range(1,8):
                grantor = response.xpath(f"(//th[text()='Grantor']/../following-sibling::tr/td/span){[i]}/text()").get(default='')
                Grantors = Grantors+ "|" + grantor
                Grantors = Grantors.strip('|').strip('|').lstrip('|')
        except:
            pass
        #not working....... Grantors=response.xpath("//th[text()='Grantor']/ancestor::tbody[1]/tr[2]/td/span").getall()
        # Grantors=response.xpath("(//th[text()='Grantor']/../following-sibling::tr/td/span)[1]/text()").get()
        Grantees = ""
        try:
            for i in range(1,8):
                grantee = response.xpath(f"(//th[text()='Grantee']/../following-sibling::tr/td/span){[i]}/text()").get(default='')

                Grantees = Grantees + "|" + grantee
                Grantees = Grantees.strip('|').strip('|').lstrip('|')
        except:
            pass

        Parcel = ""
        try:
            for i in range(1,20,2):
                parcel=response.xpath(f"(//th[text()='Parcel']/../following-sibling::tr/td/span/a){[i]}/text()").get(default='')
                if parcel != "":
                   Parcel = Parcel + "|" + parcel+"(GIS)"
                Parcel = Parcel.strip('|').strip('|').lstrip('|')
        except:
            pass
        Property_Address= ""
        try:
            for i in range(1, 20):
                property_address = response.xpath(f"//th[text()='Property Address']/../following-sibling::tr{[i]}/td[2]").get(
                    default='')
                if property_address != "":
                    Property_Address = Property_Address+ "|" + property_address
                    Property_Address=Property_Address.replace("\"",'').replace('''<td valign=top><span class=text>''','').replace("</span></td>","").replace("<br>","")
                    Property_Address= Property_Address.strip('|').strip('|').lstrip('|')
        except:
            pass
        Tract_Book= ""
        try:
            for i in range(1, 20):
                tb = response.xpath(f"//th[text()='Tract Book']/../following-sibling::tr{[i]}/td[3]").get(
                    default='')
                if tb!= "":
                    Tract_Book= Tract_Book + "|" + tb
                    Tract_Book= Tract_Book.replace("\"",'').replace('''<td valign=top><span class=text>''','').replace("</span></td>","").replace("<br>","")
                    Tract_Book= Tract_Book.strip('|').strip('|').lstrip('|')
        except:
            pass
        Legal_Page = ""
        try:
            for i in range(1, 20):
                tb = response.xpath(f"//th[text()='Page']/../following-sibling::tr{[i]}/td[4]").get(
                    default='')
                if tb != "":
                    Legal_Page = Legal_Page + "|" + tb
                    Legal_Page = Legal_Page.replace("\"", '').replace('''<td valign=top><span class=text>''',
                                                                      '').replace("</span></td>", "").replace("<br>",
                                                                                                              "")
                    Legal_Page = Legal_Page.strip('|').strip('|').lstrip('|')
        except:
            pass
        Seq= ""
        try:
            for i in range(1, 20):
                tb = response.xpath(f"//th[text()='Seq']/../following-sibling::tr{[i]}/td[5]").get(
                    default='')
                if tb != "":
                    Seq = Seq + "|" + tb
                    Seq= Seq.replace("\"", '').replace('''<td valign=top><span class=text>''',
                                                                      '').replace("</span></td>", "").replace("<br>",
                                                                                                              "")
                    Seq = Seq.strip('|').strip('|').lstrip('|')
        except:
            pass
        Legal_Description = ""
        try:
            for i in range(1, 20):
                ld = response.xpath(f"//th[text()='Legal Description']/../following-sibling::tr{[i]}/td[6]").get(
                    default='')
                if ld != "":
                    Legal_Description= Legal_Description + "|" + ld
                    Legal_Description= Legal_Description.replace("\"",'').replace('''<td valign=top><span class=text>''','').replace("</span></td>","").replace("<br>","")
                    Legal_Description= Legal_Description.strip('|').strip('|').lstrip('|')
        except:
            pass

        Short_Description = ""
        try:
            for i in range(1, 20):
                ld = response.xpath(f"//th[text()='Short Description']/../following-sibling::tr{[i]}/td[6]").get(
                    default='')
                if ld != "":
                    Short_Description = Short_Description + "|" + ld
                    Short_Description= Short_Description.replace("\"", '').replace(
                        '''<td valign=top><span class=text>''', '').replace("</span></td>", "").replace("<br>", "")
                    Short_Description= Short_Description.strip('|').strip('|').lstrip('|')
        except:
            pass

        Tract_Index_Description = ""
        try:
            for i in range(1, 20):
                td = response.xpath(f"//th[text()='Tract Index Description']/../following-sibling::tr{[i]}/td[7]").get(
                    default='')
                if td != "":
                    Tract_Index_Description= Tract_Index_Description + "|" + td
                    Tract_Index_Description = Tract_Index_Description.replace("\"", '').replace('''<td valign=top><span class=text>''', '').replace("</span></td>", "").replace("<br>", "")
                    Tract_Index_Description= Tract_Index_Description.strip('|').strip('|').lstrip('|')
        except:
            pass
        Contact_Address=response.xpath("//h2[text()='Address:']/following-sibling::text()[1]").get(default='') +" "+\
                        response.xpath("//h2[text()='Address:']/following-sibling::text()[2]").get(default='')+" "+\
                        response.xpath("//h2[text()='Address:']/following-sibling::text()[3]").get(default='')
        Phone=response.xpath("//h2[text()='Phone:']/following-sibling::text()[1]").get(default='')
        Office_Hours=response.xpath("//h2[text()='Office Hours:']/following-sibling::text()[1]").get(default='')
        County_Clerk=response.xpath("//h2[text()='County Clerk:']/following-sibling::text()[1]").get(default='')
        Document_Type= response.xpath("//div[@id='middle']/h1/following-sibling::text()[1]").get(default='').split("-")[1]
        Related_Document_Number=response.xpath("//th[text()='Document Number']/../../tr[2]/td/span/text()").get(default='')

        yield {
            "Document_Type":Document_Type.replace("\xa0","").replace("\n","").replace('\t','').strip(),
            "Document Number":Document_Number.replace("\xa0","").replace("\n",""),
            "Book":Book.replace("\xa0","").replace("\n",""),
            "Page":Page.replace("\xa0","").replace("\n",""),
            "Confirmation":Confirmation.replace("\xa0","").replace("\n",""),
            "Recording Date":Recording_Date.replace("\xa0","").replace("\n",""),
            "Number Pages":Number_Pages.replace("\xa0","").replace("\n",""),
            "Total Fees":Total_Fees.replace("\xa0","").replace("\n",""),
            "Document Date":Document_Date.replace("\xa0","").replace("\n",""),
            "Consideration Amount":Consideration_Amount.replace("\xa0","").replace("\n",""),
            "Return Address":Return_Address.replace("\xa0","").replace("\n",""),
            "Address 1":Address_1.replace("\xa0","").replace("\n",""),
            "Address 2":Address_2.replace("\xa0","").replace("\n",""),
            "City":City.replace("\xa0","").replace("\n",""),
            "State":State.replace("\xa0","").replace("\n",""),
             "Zip":Zip.replace("\xa0","").replace("\n",""),
            "Mailback Date":Mailback_Date.replace("\xa0","").replace("\n",""),
            "Grantors": Grantors.replace("\xa0","").replace("\n",""),
                # .replace("\xa0",""),
            "Grantees": Grantees.replace("\xa0","").replace("\n",""),
            "Parcel":Parcel.replace("\xa0","").replace("\n",""),
            "Property Address":Property_Address.replace("\xa0","").replace("\n",""),
            "Tract Book":Tract_Book.replace("\xa0","").replace("\n",""),
             "Legal Page":Legal_Page.replace("\xa0","").replace("\n",""),
            "Seq":Seq.replace("\xa0","").replace("\n",""),
             "Legal Description":Legal_Description.replace("\xa0","").replace("\n",""),
            "Short Description":Short_Description.replace("\xa0","").replace("\n",""),

             "Tract Index Description":Tract_Index_Description.replace("\xa0","").replace("\n",""),
            " Contact Address": Contact_Address.replace("\xa0","").replace("\n",""),
            "Phone":Phone.replace("\xa0","").replace("\n",""),
            "Office Hours":Office_Hours.replace("\xa0","").replace("\n",""),
            "County Clerk":County_Clerk.replace("\xa0","").replace("\n",""),
            "Related Document Number":Related_Document_Number.replace("\xa0","").replace("\n",""),

        }

from scrapy.cmdline import execute
execute('scrapy crawl peoria -o IL-PEORIA-07012021-07032021.csv'.split())
# " -o CA-PEORIA-07012021-07032021.csv"