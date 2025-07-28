import scrapy
from scrapy.http import headers
from scrapy.utils.response import open_in_browser
import re


class Peoria(scrapy.Spider):
    name = 'peoria'
    headers = {'Accept': 'application/json, text/javascript, */*; q=0.01', 'Accept-Encoding': 'gzip, deflate, br',
               'Accept-Language': 'en-US,en;q=0.9', 'ajaxRequest': 'true', 'Connection': 'keep-alive',
               'Host': 'macombcountymi-web.tylerhost.net', 'Origin': 'https://macombcountymi-web.tylerhost.net',
               'Referer': 'https://macombcountymi-web.tylerhost.net/web/user/disclaimer', 'sec-ch-ua': '" Not;A Brand";v="99", "Google Chrome";v="91", "Chromium";v="91"',
               'sec-ch-ua-mobile': '?0', 'Sec-Fetch-Dest': 'empty', 'Sec-Fetch-Mode': 'cors', 'Sec-Fetch-Site': 'same-origin',
               'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36',
               'X-Requested-With': 'XMLHttpRequest'
               }
    start_date='01/02/2020'
    end_date='01/02/2020'


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
            url="https://macombcountymi-web.tylerhost.net/web/user/disclaimer",
            callback=self.parse2,
            dont_filter=True,
            method="POST",
            headers=self.headers,
        )

    def parse2(self, response):
        # open_in_browser(response)
        yield scrapy.Request(
            url="https://macombcountymi-web.tylerhost.net/web/action/ACTIONGROUP95S1?_=1626245352681",
            callback=self.parse3,
            dont_filter=True,
            method="GET",
            headers=self.headers,
        )

    def parse3(self, response):
        # open_in_browser(response)
        yield scrapy.Request(
            url="https://macombcountymi-web.tylerhost.net/web/search/DOCSEARCH95S8?_=1626245352695",
            callback=self.parse4,
            dont_filter=True,
            method="GET",
            headers=self.headers,
        )

    def parse4(self, response):
        # open_in_browser(response)
        data = { 'field_BothNamesID-containsInput': 'Contains Any', 'field_GrantorID-containsInput': 'Contains Any', 'field_GranteeID-containsInput': 'Contains Any',
               'field_RecordingDateID_DOT_StartDate': self.start_date, 'field_RecordingDateID_DOT_EndDate': self.end_date,
               'field_selfservice_documentTypes-containsInput': 'Contains Any'
               }


        yield scrapy.FormRequest(
            url="https://macombcountymi-web.tylerhost.net/web/searchPost/DOCSEARCH95S8",
            callback=self.parse5,
            formdata=data,
            dont_filter=True,
            method="POST",
            headers=self.headers,
            meta={'handle_httpstatus_list': [200]}
        )

    def parse5(self, response):
        open_in_browser(response)
        res = response.json()
        total=res['totalPages']
        for i in range(1,int(total)+1):
            yield scrapy.Request(
                url=f"https://macombcountymi-web.tylerhost.net/web/searchResults/DOCSEARCH95S8?page={i}",
                    # "&_=1626247619295",
                callback=self.parse6,
                dont_filter=True,
                method="GET",
                headers=self.headers,
                meta={'handle_httpstatus_list': [200]}
            )

    def parse6(self, response):
        # open_in_browser(response)
        total_records = response.xpath("//li/@data-documentid").getall()
        print(total_records)
        count=1
        for i in total_records:
            count+=1
            if count==6:
                pass
            yield scrapy.Request(
                url=f"https://macombcountymi-web.tylerhost.net/web/document/{i}?search=DOCSEARCH95S8",
                callback=self.parse7,
                dont_filter=True,
                method="GET",
                headers=self.headers,
                meta={'handle_httpstatus_list': [200]}
            )
    def parse7(self, response):
        # open_in_browser(response)
        Document_Type= response.xpath("//li[contains(text(),'Document Type')]/following-sibling::li/text()").get(default='')
        Document_Number= response.xpath("//strong[contains(text(),'Document Number')]/../following-sibling::div/text()").get(default='')
        Recording_Date= response.xpath("//strong[contains(text(),'Recording Date:')]/../following-sibling::div/text()").get(default='')
        Number_Pages= response.xpath("//strong[contains(text(),'Number Pages')]/../following-sibling::div/text()").get(default='')
        Recording_Fee= response.xpath("//strong[contains(text(),'Recording Fee')]/../following-sibling::div/text()").get(default='')

        Liber=''
        for i in range(1,30):
            lb = response.xpath(f"(//th[text()='Liber']/../following-sibling::tr{[i]}/td)[1]/text()").get(default='')
            # lb = response.xpath(f"(//b[contains(text(),'Liber')]){[i]}/following-sibling::text()").get(default='')

            # if lb != "":
            Liber = Liber + "|" + lb
            Liber = Liber.strip().strip("|")

        Page = ''
        for i in range(1,30):
            lb = response.xpath(f"(//th[text()='Liber']/../following-sibling::tr{[i]}/td)[2]/text()").get(default='')
            # lb = response.xpath(f"(//b[contains(text(),'Page')])[{i}]/following-sibling::text()").get(default='')

            if lb != "":
                Page = Page + "|" + lb
                Page = Page.strip().strip("|")


        Grantor1 = response.xpath(
                "//strong[contains(text(),'Grantor')]/../following-sibling::div/text()").get(default='')

        Grantor2 = ""
        for i in range(1,10):
            gn = response.xpath(
                f"//strong[contains(text(),'Grantor')]/../following-sibling::div/ul/li[{i}]/text()").get(
                default='')
            if gn != " ":
                Grantor2 = Grantor2 + "|" + gn
                Grantor2 = Grantor2.strip().strip("|")
        Grantor = Grantor1+Grantor2

        Grantee_Notation1= response.xpath("//strong[contains(text(),'Grantee/Notation')]/../following-sibling::div/text()").get(default='')
        Grantee_Notation2 = ""
        for i in range(1,10):
            gn=response.xpath(f"//strong[contains(text(),'Grantee/Notation')]/../following-sibling::div/ul/li[{i}]/text()").get(default='')
            Grantee_Notation2 = Grantee_Notation2 + "|" + gn
            Grantee_Notation2 = Grantee_Notation2.strip().strip("|")
        Grantee_Notation =Grantee_Notation1 + Grantee_Notation2
        Document_Date=response.xpath("//strong[text()='Document Date:']/../following-sibling::div/text()").get(default='')
        Parcel = response.xpath("//div[contains(text(),'Parcel')]/text()").get(default='')
        Property = response.xpath("//div[contains(text(),'Property')]/text()").get(default='')
        Legal1 =response.xpath("//div[contains(text(),'Property')]/text()").get(default='')
        Legal = ''
        for i in range(6):
            tt = response.xpath(f"((//ul[contains(@class,'ui-unbulleted-list')])[2]/li){[i]}/text()").get(
                default='')
            Legal = Legal + "|" + tt
            Legal = Legal.strip().strip("|")

        # Legal = Parcel + "|" + Property + "|" + Legal
        Legal = Legal1 + "|" + Legal
        Legal = Legal.strip("|")
        #
        # yield{
        #     "Document Number":Document_Number,
        #     "Document Type":Document_Type.strip('\n\t'),
        #     "Recording Date":Recording_Date,
        #     "Number Pages":Number_Pages,
        #     "Recording Fees":Recording_Fee,
        #     "Liber":Liber,
        #     "Page":Page,
        #     "Grantor":Grantor.replace('\n',''),
        #     "Grantee/Notation":Grantee_Notation.replace('\n',''),
        #     "Document Date":Document_Date,
        #     "Legal":Legal
        #
        #
        # }
        new_url = response.request.url
        doc_id= (re.search('document\/(.*)\?',new_url)).group(1)
        # print(doc_id)
        yield scrapy.Request(
            url=f"https://macombcountymi-web.tylerhost.net/web/document/relatedDocuments/{doc_id}?queryId=ec4d2a45-a81f-4acf-9fba-f401eccf994f&search=DOCSEARCH95S8",
            # url=f"https://macombcountymi-web.tylerhost.net/web/document/relatedDocuments/DOCCLND-2020-2000620-MA?queryId=ec4d2a45-a81f-4acf-9fba-f401eccf994f&search=DOCSEARCH95S8&_=1626347617329",
            callback=self.parse8,
            dont_filter=True,
            method="GET",
            headers=self.headers,
            meta={
                "Document Number": Document_Number,
                "Document Type":Document_Type.strip('\n\t'),
                "Recording Date":Recording_Date,
                "Number Pages":Number_Pages,
                "Recording Fees":Recording_Fee,
                "Liber":Liber,
                "Page":Page,
                "Grantor":Grantor.replace('\n',''),
                "Grantee/Notation":Grantee_Notation.replace('\n',''),
                "Document Date":Document_Date,
                "Legal":Legal

            }
        )
    def parse8(self,response):
        type=response.xpath("//td[@class='related-doc-type truncate']/text()").get(default='')
        date=response.xpath("//td[@class='related-doc-recording-date elipsis']/text()").get(default='')
        doc=response.xpath("//a[@class='document-link']/text()").get(default='')

        gran=response.xpath("(//div[@class='related-data-panel']/div)[1]/text()").getall()
        tgran=''
        for i in gran:
            tgran=tgran+"|"+i
            tgran=tgran.strip().strip("|")


        grane=response.xpath("(//div[@class='related-data-panel']/div)[2]/text()").getall()
        tgrane=''
        for i in grane:
            tgrane=tgrane+"|"+i
            tgrane=tgrane.strip().strip("|")


        # print(gran)
        # print(type)
        # print(date)
        Related=''
        for i in [type,date,doc,tgran,tgrane]:
            if i !='':
                Related = Related + "|" + i
                Related=Related.strip().strip("|")
        yield{
            "Document Number": response.request.meta["Document Number"],
            "Document Type": response.request.meta["Document Type"],
            "Recording Date": response.request.meta["Recording Date"],
            "Number Pages": response.request.meta["Number Pages"],
            "Recording Fees": response.request.meta["Recording Fees"],
            "Liber": response.request.meta["Liber"],
            "Page": response.request.meta["Page"],
            "Grantor": response.request.meta["Grantor"],
            "Grantee/Notation": response.request.meta["Grantee/Notation"],
            "Document Date": response.request.meta["Document Date"],
            "Legal": response.request.meta["Legal"],
            "Related Documents": Related.replace('\n', '').replace('\t', ''),

              }







from scrapy.cmdline import execute
execute('scrapy crawl peoria -o ex.csv'.split())
# -o 01022020.csv


