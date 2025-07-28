import json

import scrapy
from scrapy.utils.response import open_in_browser


class SandiegoSpider(scrapy.Spider):
    name = 'sandiego'
    allowed_domains = []

    headers = {
        "User-Agent": "Mozilla/5.0 AppleWebKit/537.36 (KHTML, like Gecko; compatible; Googlebot/2.1; http://www.google.com/bot.html) Chrome/W.X.Y.Z‡ Safari/537.36"
    }

    def start_requests(self):
        yield scrapy.Request(
            url="http://arcc-acclaim.sdcounty.ca.gov/search/SearchTypeRecordDate/",
            callback=self.parse,
            headers=self.headers,
            dont_filter=True
        )

    def parse(self, response):
        data = {"disclaimer": "true"}
        yield scrapy.FormRequest(
            url="https://arcc-acclaim.sdcounty.ca.gov/search/Disclaimer?st=/search/SearchTypeRecordDate/",
            callback=self.parse2,
            headers=self.headers,
            formdata=data,
            method='POST',
            dont_filter=True,
            meta={'handle_httpstatus_list':[302]}
        )

    def parse2(self, response):
        yield scrapy.Request(
            url="https://arcc-acclaim.sdcounty.ca.gov/search/SearchTypeRecordDate/",
            callback=self.parse3,
            headers=self.headers,
            dont_filter=True
        )

    def parse3(self, response):
        data = {
            "RecordDate": str(self.dt),
            "X-Requested-With": "XMLHttpRequest"
        }
        yield scrapy.FormRequest(
            url="https://arcc-acclaim.sdcounty.ca.gov/search/SearchTypeRecordDate",
            callback=self.parse4,
            headers=self.headers,
            method='POST',
            formdata=data,
            dont_filter=True,
        )

    def parse4(self, response):
        header = {
            "Accept": "text/plain, */*; q=0.01",
            "Accept-Encoding": "gzip, deflate, br",
            "Accept-Language": "en-US,en;q=0.9",
            "Connection": "keep-alive",
            "Content-Type": "application/x-www-form-urlencoded",
            "Host": "arcc-acclaim.sdcounty.ca.gov",
            "Origin": "https://arcc-acclaim.sdcounty.ca.gov",
            "Referer": str(response.url),
            "Sec-Fetch-Dest": "empty",
            "Sec-Fetch-Mode": "cors",
            "Sec-Fetch-Site": "same-origin",
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/89.0.4389.90 Safari/537.36",
            "X-Requested-With": "XMLHttpRequest"
        }
        data = {
            "page": "1",
            "size": "500"
        }
        yield scrapy.FormRequest(
            url="https://arcc-acclaim.sdcounty.ca.gov/Search/GridResults",
            callback=self.parse5,
            headers=header,
            method='POST',
            formdata=data,
            dont_filter=True,
        )

    def parse5(self, response):
        json_data = json.loads(response.text)
        total_data = json_data['total']
        pages = int(total_data)/500
        for i in range(1, int(pages)+1):
            header = {
                "Accept": "text/plain, */*; q=0.01",
                "Accept-Encoding": "gzip, deflate, br",
                "Accept-Language": "en-US,en;q=0.9",
                "Connection": "keep-alive",
                "Content-Type": "application/x-www-form-urlencoded",
                "Host": "arcc-acclaim.sdcounty.ca.gov",
                "Origin": "https://arcc-acclaim.sdcounty.ca.gov",
                "Referer": "https://arcc-acclaim.sdcounty.ca.gov/search/SearchTypeRecordDate",
                "Sec-Fetch-Dest": "empty",
                "Sec-Fetch-Mode": "cors",
                "Sec-Fetch-Site": "same-origin",
                "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/89.0.4389.90 Safari/537.36",
                "X-Requested-With": "XMLHttpRequest"
            }
            data = {
                "page": str(i),
                "size": "500"
            }
            yield scrapy.FormRequest(
                url="https://arcc-acclaim.sdcounty.ca.gov/Search/GridResults",
                callback=self.parse6,
                headers=header,
                method='POST',
                formdata=data,
                dont_filter=True,
            )

    def parse6(self, response):
        json_data = json.loads(response.text)
        for i in range(0, 500):
            id = json_data['data'][i]['TransactionItemId']
            apn = json_data['data'][i]['ParcelNumber']
            if apn == None:
                apn = ''
            link = f"https://arcc-acclaim.sdcounty.ca.gov/details/documentdetails/{id}"
            yield scrapy.Request(
                url=link,
                callback=self.parse7,
                headers=self.headers,
                dont_filter=True,
                meta={'apn':apn}
            )

    def parse7(self, response):
        apn = response.meta['apn'].strip()

        rec_date = response.xpath('//div[contains(text(),"Record Date")]/following-sibling::div/text()').get(default='').strip()

        book_type = response.xpath('//div[contains(text(),"Book Type")]/following-sibling::div/text()').get(default='').replace('\r\n','').replace(' ','').strip()

        book_page = response.xpath('//div[contains(text(),"Book / Page")]/following-sibling::div/text()').get(default='').strip()
        if book_page == '/':
            book_page = ''

        doc_num = response.xpath('//div[contains(text(),"Document #")]/following-sibling::div/text()').get(default='').strip()

        sec_num = response.xpath('//div[contains(text(),"Secondary #")]/following-sibling::div/text()').get(default='').strip()

        no_of_pages = response.xpath('//div[contains(text(),"Number of Pages")]/following-sibling::div/text()').get(default='').strip()

        doc_type = response.xpath('//div[contains(text(),"Doc Type")]/following-sibling::div/text()').get(default='').strip()

        grantor = '|'.join(i.strip() for i in response.xpath('//div[contains(text(),"Grantor")]/following-sibling::div/span/text()').getall() if i!='')

        grantee = '|'.join(i.strip() for i in response.xpath('//div[contains(text(),"Grantee")]/following-sibling::div/span/text()').getall() if i!='')

        reel_num = response.xpath('//div[contains(text(),"Reel #")]/following-sibling::div/text()').get(default='').strip()

        img_num = response.xpath('//div[contains(text(),"Image #")]/following-sibling::div/text()').get(default='').strip()

        yield {
            "Record Date": rec_date,
            "Book Type": book_type,
            "Book / Page": book_page,
            "Document #": doc_num,
            "APN": apn,
            "Secondary #": sec_num,
            "Number of Pages": no_of_pages,
            "Doc Type": doc_type,
            "Grantor": grantor,
            "Grantee": grantee,
            "Reel #": reel_num,
            "Image #": img_num,
        }


# from scrapy.cmdline import execute
# execute('scrapy crawl sandiego -a dt=05/14/2021 -o CA-Sandiego-05142021.csv'.split())

