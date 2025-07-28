import scrapy
from scrapy.utils.response import open_in_browser
import time
import re
from selenium import webdriver
from selenium.webdriver.common.keys import Keys


# driver= webdriver.Chrome(r"C:\Users\Saurabh prajapati\PycharmProjects\selenium\chromedriver.exe")


class Blaircounty(scrapy.Spider):
    name = 'Blair_county'
    allowed_domains = []
    start_urls = [
       "https://www.landex.com/webstore/jsp/cart/DocumentSearchResults.jsp?LastName=&FirstName=&StartDate=07%2F12%2F2020&EndDate=07%2F20%2F2020&MunicipalityCriteria=%2B.landex.16&InstrumentCriteria=%2B.landex&DisplayItemsPerPage=250&MaximumMatches=250",
       "https://www.landex.com/webstore/jsp/cart/DocumentSearchResults.jsp?DisplayPage=2&DisplayPage=2LastName=&FirstName=&StartDate=07%2F12%2F2020&EndDate=07%2F20%2F2020&MunicipalityCriteria=%2B.landex.16&InstrumentCriteria=%2B.landex&DisplayItemsPerPage=250&MaximumMatches=250",
        "https://www.landex.com/webstore/jsp/cart/DocumentSearchResults.jsp?DisplayPage=2&DisplayPage=2LastName=&FirstName=&StartDate=07%2F12%2F2020&EndDate=07%2F20%2F2020&MunicipalityCriteria=%2B.landex.16&InstrumentCriteria=%2B.landex&DisplayItemsPerPage=250&MaximumMatches=250",
                 ]
    count=2

    def parse(self, response):
        open_in_browser(response)
       # total=response.xpath("(//a[@class='info']/@onclick)[3]").extract()
        total = response.xpath("(//a[@class='info']/@onclick)").getall()


        for i in range(1, (len(total) + 1)):

            iter = str(response.xpath(f"(//a[@class='info']/@onclick)[{i}]").extract())

            test = (re.search('[^\\n](.*)', iter)).group()
            test=str(test)
        # test=re.search('align=top>REGISTER OF WILLS MASTER',total)
        #test=(re.search('[^\\n](.*)',total)).group()
        # match=test.group()
            try:
                Recorded_Date=(re.search('<STRONG>Recorded Date:<\/STRONG><\/td><td valign=top>(.*\n*, \d{4})',test)).group(1)

            except:
                Recorded_Date=""
            try:
                Instrument=(re.search('<STRONG>Instrument #:<\/STRONG><\/td><td valign=top>(\d*\n*\d*)<\/td>',test)).group(1)
            except:
                Instrument=""
            try:
                Time=(re.search('<br>(\d{0,4}:\d{0,4}:\d{0,4}) PM',test)).group(1)
            except:
                Time =""

            try:
                Instrument_Type=(re.search('<STRONG>Instrument Type:<\/STRONG><\/td><td(\n*)(\s*)valign=top>(.*)<\/td><\/tr><tr><td width=150 valign=top class=arial-black-14px-bold><STRONG>County',test)).group(0)
                Instrument_Type=(re.search('valign=top>(.*)<\/td><\/tr><tr>',Instrument_Type)).group(1)
            except:
                Instrument_Type =""
            try:
                Municipality=(re.search('<STRONG>Municipality:<\/STRONG><\/td><td\n*\s*valign=top>(.*)<\/td><\/tr><tr><td width=150\n*\s*valign=top class=arial-black-14px-bold><STRONG>Recording Status',test)).group(1)
            except:
                Municipality =""
            try:
                Recording_Status=(re.search('<STRONG>Recording Status:<\/STRONG><\/\n*\s*td><td valign=top>(\w*)<\/td><\/tr><\/table>',test)).group(1)
            except:
                Recording_Status =""
            try:
                DECEASED=(re.search('<STRONG>DECEASED<\/STRONG><\/td><\/tr><tr><td width=50% valign=top>(.*)<BR><\/td><td valign=top>',test)).group(1)
            except:
                DECEASED=""
            try:
                Book=(re.search('<STRONG>Book:<\/STRONG><\/td><td valign=top>(.*)<\/td><\/tr><tr><td width=150',test)).group(0)
                Book=(re.search('<STRONG>Book:<\/STRONG><\/td><td valign=top>(.*)<\/td><\/tr><tr><td width=150\n*\s*valign=top class=arial-black-14px-bold><STRONG>Page',Book)).group(1)
            except:
                Book =""
            try:
                Page=(re.search('<STRONG>Page:<\/STRONG><\/td><td valign=top>(.*)<\/td><\/tr><tr><td width=150 valign=top class=arial-black-14px-bold><STRONG>',test)).group(1)
            except:
                Page =""
            try:
                Total_Pages=(re.search('<STRONG>Total Pages:<\/STRONG><\/td><td valign=top>(.*)<\/td><\/tr><tr><td width=150 valign=top \n*\s*class=arial-black-14px-bold rowspan=2><STRONG>Parcel',test)).group(1)
            except:
                Total_Pages =""
            try:
                Parcel_Number=(re.search('><STRONG>Parcel Numbers:<\/STRONG><\/td><td valign=top rowspan=2>(.*)<\/td><\/tr><\/table><\/td><\/tr><tr><td colspan=2>\n*\s*<table width=100% border=0><tr><td width=150 valign=top class=arial-black-14px-bold><STRONG>Notes',test)).group(1)
            except:
                Parcel_Number =""

            yield {"Instrument":Instrument,
                  "Recoded Date":Recorded_Date+""+Time,
                   "County":"Blair",
                   "Instrument Type":Instrument_Type,
                   "Municipality":Municipality,
                    "Recording_Status":Recording_Status,
                   "DECEASED":DECEASED,
                   "Book":Book,
                   "Page":Page,
                   "Total Pages":Total_Pages,
                   'Parcel Numbers':Parcel_Number


               }

        urls = [
            "https://www.landex.com/webstore/jsp/cart/DocumentSearchResults.jsp?DisplayPage=2&DisplayPage=2LastName=&FirstName=&StartDate=07%2F12%2F2020&EndDate=07%2F20%2F2020&MunicipalityCriteria=%2B.landex.16&InstrumentCriteria=%2B.landex&DisplayItemsPerPage=250&MaximumMatches=250",
            "https://www.landex.com/webstore/jsp/cart/DocumentSearchResults.jsp?DisplayPage=3&DisplayPage=3LastName=&FirstName=&StartDate=07%2F12%2F2020&EndDate=07%2F20%2F2020&MunicipalityCriteria=%2B.landex.16&InstrumentCriteria=%2B.landex&DisplayItemsPerPage=250&MaximumMatches=250",
            "https://www.landex.com/webstore/jsp/cart/DocumentSearchResults.jsp?DisplayPage=4&DisplayPage=4LastName=&FirstName=&StartDate=07%2F12%2F2020&EndDate=07%2F20%2F2020&MunicipalityCriteria=%2B.landex.16&InstrumentCriteria=%2B.landex&DisplayItemsPerPage=250&MaximumMatches=250",
            "https://www.landex.com/webstore/jsp/cart/DocumentSearchResults.jsp?DisplayPage=5&DisplayPage=5LastName=&FirstName=&StartDate=07%2F12%2F2020&EndDate=07%2F20%2F2020&MunicipalityCriteria=%2B.landex.16&InstrumentCriteria=%2B.landex&DisplayItemsPerPage=250&MaximumMatches=250",

        ]

        for i in urls:
            yield scrapy.Request(

                url=i,
                callback=self.parse2,

                method='GET',
                dont_filter=True,)

    def parse2(self, response):
        open_in_browser(response)
        # total=response.xpath("(//a[@class='info']/@onclick)[3]").extract()
        total = response.xpath("(//a[@class='info']/@onclick)").getall()

        for i in range(1, (len(total) + 1)):

            iter = str(response.xpath(f"(//a[@class='info']/@onclick)[{i}]").extract())

            test = (re.search('[^\\n](.*)', iter)).group()
            test = str(test)
            # test=re.search('align=top>REGISTER OF WILLS MASTER',total)
            # test=(re.search('[^\\n](.*)',total)).group()
            # match=test.group()
            try:
                Recorded_Date = (
                    re.search('<STRONG>Recorded Date:<\/STRONG><\/td><td valign=top>(.*\n*, \d{4})',
                              test)).group(1)

            except:
                Recorded_Date = ""
            try:
                Instrument = (re.search('<STRONG>Instrument #:<\/STRONG><\/td><td valign=top>(\d*\n*\d*)<\/td>',
                                        test)).group(1)
            except:
                Instrument = ""
            try:
                Time = (re.search('<br>(\d{0,4}:\d{0,4}:\d{0,4}) PM', test)).group(1)
            except:
                Time = ""

            try:
                Instrument_Type = (re.search(
                    '<STRONG>Instrument Type:<\/STRONG><\/td><td(\n*)(\s*)valign=top>(.*)<\/td><\/tr><tr><td width=150 valign=top class=arial-black-14px-bold><STRONG>County',
                    test)).group(0)
                Instrument_Type = (re.search('valign=top>(.*)<\/td><\/tr><tr>', Instrument_Type)).group(1)
            except:
                Instrument_Type = ""
            try:
                Municipality = (re.search(
                    '<STRONG>Municipality:<\/STRONG><\/td><td\n*\s*valign=top>(.*)<\/td><\/tr><tr><td width=150\n*\s*valign=top class=arial-black-14px-bold><STRONG>Recording Status',
                    test)).group(1)
            except:
                Municipality = ""
            try:
                Recording_Status = (re.search(
                    '<STRONG>Recording Status:<\/STRONG><\/\n*\s*td><td valign=top>(\w*)<\/td><\/tr><\/table>',
                    test)).group(1)
            except:
                Recording_Status = ""
            try:
                DECEASED = (re.search(
                    '<STRONG>DECEASED<\/STRONG><\/td><\/tr><tr><td width=50% valign=top>(.*)<BR><\/td><td valign=top>',
                    test)).group(1)
            except:
                DECEASED = ""
            try:
                Book = (
                    re.search('<STRONG>Book:<\/STRONG><\/td><td valign=top>(.*)<\/td><\/tr><tr><td width=150',
                              test)).group(0)
                Book = (re.search(
                    '<STRONG>Book:<\/STRONG><\/td><td valign=top>(.*)<\/td><\/tr><tr><td width=150\n*\s*valign=top class=arial-black-14px-bold><STRONG>Page',
                    Book)).group(1)
            except:
                Book = ""
            try:
                Page = (re.search(
                    '<STRONG>Page:<\/STRONG><\/td><td valign=top>(.*)<\/td><\/tr><tr><td width=150 valign=top class=arial-black-14px-bold><STRONG>',
                    test)).group(1)
            except:
                Page = ""
            try:
                Total_Pages = (re.search(
                    '<STRONG>Total Pages:<\/STRONG><\/td><td valign=top>(.*)<\/td><\/tr><tr><td width=150 valign=top \n*\s*class=arial-black-14px-bold rowspan=2><STRONG>Parcel',
                    test)).group(1)
            except:
                Total_Pages = ""
            try:
                Parcel_Number = (re.search(
                    '><STRONG>Parcel Numbers:<\/STRONG><\/td><td valign=top rowspan=2>(.*)<\/td><\/tr><\/table><\/td><\/tr><tr><td colspan=2>\n*\s*<table width=100% border=0><tr><td width=150 valign=top class=arial-black-14px-bold><STRONG>Notes',
                    test)).group(1)
                Parcel_Number  = Parcel_Number.replace('<BR>',"")
            except:
                Parcel_Number = ""

            yield {"Instrument": Instrument,
                   "Recoded Date": Recorded_Date + "" + Time,
                   "County": "Blair",
                   "Instrument Type": Instrument_Type,
                   "Municipality": Municipality,
                   "Recording_Status": Recording_Status,
                   "DECEASED": DECEASED,
                   "Book": Book,
                   "Page": Page,
                   "Total Pages": Total_Pages,
                   'Parcel Numbers': Parcel_Number

                   }

        # for i in  range(2,6):
    #     while self.count<=5:
    #     #if (response.xpath("//option[@selected='selected']/following-sibling::option/@value").get()):
    #         header={
    #         "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9 ",
    #         "Accept-Encoding": "gzip, deflate",
    #         "Accept-Language": "en-US,en;q=0.9",
    #         "User-Agent" :"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.106 Safari/537.36" ,
    #          "Host":"www.landex.com",
    #     }
    #
    #         yield scrapy.FormRequest(
    #
    #             url=f"http://www.landex.com/webstore/jsp/cart/DocumentSearchResults.jsp?DisplayPage={self.count}",
    #             callback=self.parse2,
    #             method="GET",
    #             headers=header,
    #             # formdata=data,
    #             meta={'handle_httpstatus_list': [302]},
    #            # DisplayPage=f"{i}",
    #            #  i=self.count,
    #             dont_filter=True,
    #         )
    #
    #         self.count+=1
    #         if self.count>5:
    #             break
    #
    # def parse2(self, response):
    #     open_in_browser(response)
    #     header = {"DisplayPage":"2",
    # ":authority": "www.landex.com",
    # ":path": "webstore/jsp/cart/DocumentSearchResults.jsp?DisplayPage=2&DisplayPage={self.count}",
    # ":scheme": "https",
    # "accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9 ",
    # "accept-encoding": "gzip, deflate",
    # "accept-language": "en-US,en;q=0.9",
    # "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.106 Safari/537.36",
    # "Host": "www.landex.com",
    # "sec-ch-ua":'Not;A Brand";v="99", "Google Chrome";v="91", "Chromium";v="91"',
    # "sec-fetch-dest": "document",
    # "sec-fetch-mode": "navigate",
    # "sec-fetch-site": "cross-site",
    # "sec-fetch-user": "?1",
    # "upgrade-insecure-requests": "1",
    #     }
    #
    #     yield scrapy.FormRequest(
    #
    # # url=f"http://www.landex.com/webstore/jsp/cart/DocumentSearchResults.jsp?DisplayPage={self.count}",
    #
    #         url=f"https://www.landex.com/webstore/jsp/cart/DocumentSearchResults.jsp?DisplayPage=2&DisplayPage=2",
    #         callback=self.parse,
    #         method="GET",
    #         headers=header,
    #         # formdata=data,
    #         meta={'handle_httpstatus_list': [200]},
    #
    #         dont_filter=True,
    #                )

    # def parse3(self, response):
    #         open_in_browser(response)
    #         # total=response.xpath("(//a[@class='info']/@onclick)[3]").extract()
    #         total = response.xpath("(//a[@class='info']/@onclick)").getall()
    #
    #         for i in range(1, (len(total) + 1)):
    #
    #             iter = str(response.xpath(f"(//a[@class='info']/@onclick)[{i}]").extract())
    #
    #             test = (re.search('[^\\n](.*)', iter)).group()
    #             test = str(test)
    #             # test=re.search('align=top>REGISTER OF WILLS MASTER',total)
    #             # test=(re.search('[^\\n](.*)',total)).group()
    #             # match=test.group()
    #             try:
    #                 Recorded_Date = (
    #                     re.search('<STRONG>Recorded Date:<\/STRONG><\/td><td valign=top>(.*\n*, \d{4})', test)).group(1)
    #
    #             except:
    #                 Recorded_Date = ""
    #             try:
    #                 Instrument = (
    #                     re.search('<STRONG>Instrument #:<\/STRONG><\/td><td valign=top>(\d*\n*\d*)<\/td>', test)).group(
    #                     1)
    #             except:
    #                 Instrument = ""
    #             try:
    #                 Time = (re.search('<br>(\d{0,4}:\d{0,4}:\d{0,4}) PM', test)).group(1)
    #             except:
    #                 Time = ""
    #
    #             try:
    #                 Instrument_Type = (re.search(
    #                     '<STRONG>Instrument Type:<\/STRONG><\/td><td(\n*)(\s*)valign=top>(.*)<\/td><\/tr><tr><td width=150 valign=top class=arial-black-14px-bold><STRONG>County',
    #                     test)).group(0)
    #                 Instrument_Type = (re.search('valign=top>(.*)<\/td><\/tr><tr>', Instrument_Type)).group(1)
    #             except:
    #                 Instrument_Type = ""
    #             try:
    #                 Municipality = (re.search(
    #                     '<STRONG>Municipality:<\/STRONG><\/td><td\n*\s*valign=top>(.*)<\/td><\/tr><tr><td width=150\n*\s*valign=top class=arial-black-14px-bold><STRONG>Recording Status',
    #                     test)).group(1)
    #             except:
    #                 Municipality = ""
    #             try:
    #                 Recording_Status = (re.search(
    #                     '<STRONG>Recording Status:<\/STRONG><\/\n*\s*td><td valign=top>(\w*)<\/td><\/tr><\/table>',
    #                     test)).group(1)
    #             except:
    #                 Recording_Status = ""
    #             try:
    #                 DECEASED = (re.search(
    #                     '<STRONG>DECEASED<\/STRONG><\/td><\/tr><tr><td width=50% valign=top>(.*)<BR><\/td><td valign=top>',
    #                     test)).group(1)
    #             except:
    #                 DECEASED = ""
    #             try:
    #                 Book = (re.search('<STRONG>Book:<\/STRONG><\/td><td valign=top>(.*)<\/td><\/tr><tr><td width=150',
    #                                   test)).group(0)
    #                 Book = (re.search(
    #                     '<STRONG>Book:<\/STRONG><\/td><td valign=top>(.*)<\/td><\/tr><tr><td width=150\n*\s*valign=top class=arial-black-14px-bold><STRONG>Page',
    #                     Book)).group(1)
    #             except:
    #                 Book = ""
    #             try:
    #                 Page = (re.search(
    #                     '<STRONG>Page:<\/STRONG><\/td><td valign=top>(.*)<\/td><\/tr><tr><td width=150 valign=top class=arial-black-14px-bold><STRONG>',
    #                     test)).group(1)
    #             except:
    #                 Page = ""
    #             try:
    #                 Total_Pages = (re.search(
    #                     '<STRONG>Total Pages:<\/STRONG><\/td><td valign=top>(.*)<\/td><\/tr><tr><td width=150 valign=top \n*\s*class=arial-black-14px-bold rowspan=2><STRONG>Parcel',
    #                     test)).group(1)
    #             except:
    #                 Total_Pages = ""
    #             try:
    #                 Parcel_Number = (re.search(
    #                     '><STRONG>Parcel Numbers:<\/STRONG><\/td><td valign=top rowspan=2>(.*)<\/td><\/tr><\/table><\/td><\/tr><tr><td colspan=2>\n*\s*<table width=100% border=0><tr><td width=150 valign=top class=arial-black-14px-bold><STRONG>Notes',
    #                     test)).group(1)
    #             except:
    #                 Parcel_Number = ""
    #
    #             yield {"Instrument": Instrument,
    #                    "Recoded Date": Recorded_Date + "" + Time,
    #                    "County": "Blair",
    #                    "Instrument Type": Instrument_Type,
    #                    "Municipality": Municipality,
    #                    "Recording_Status": Recording_Status,
    #                    "DECEASED": DECEASED,
    #                    "Book": Book,
    #                    "Page": Page,
    #                    "Total Pages": Total_Pages,
    #                    'Parcel Numbers': Parcel_Number
    #
    #                    }
from scrapy.cmdline import execute
execute('scrapy crawl Blair_county -o Blair.csv'.split())