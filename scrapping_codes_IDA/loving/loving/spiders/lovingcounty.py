import urllib
import scrapy
from scrapy import Spider
from scrapy.http import Request, FormRequest
from scrapy.utils.response import open_in_browser
import json
import configparser as cp
import re
import csv
import math
from random import randint

class LovingSpider(scrapy.Spider):
    name = 'lovingspider'
    start_date = '07/29/2021'
    headers = {'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
               'Accept-Encoding': 'gzip, deflate, br', 'Accept-Language': 'en-US,en;q=0.9', 'Cache-Control': 'max-age=0',
               'Connection': 'keep-alive',"Host": "lovingtx.countygovernmentrecords.com"
                 ,"Referer": "https://lovingtx.countygovernmentrecords.com/LovingTXRecorder/web/",
               'sec-ch-ua': '"Chromium";v="92", " Not A;Brand";v="99", "Google Chrome";v="92"', 'sec-ch-ua-mobile': '?0', 'Sec-Fetch-Dest': 'document',
               'Sec-Fetch-Mode': 'navigate', 'Sec-Fetch-Site': 'same-origin', 'Sec-Fetch-User': '?1', 'Upgrade-Insecure-Requests': '1',
               'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/92.0.4515.107 Safari/537.36'
               }

    def start_requests(self):
        urls = "https://lovingtx.countygovernmentrecords.com/LovingTXRecorder/web/"

        yield scrapy.Request(
            url=urls,
            callback=self.parse1,
            headers=self.headers,
            dont_filter=True,
            method="GET"
        )
    #disclaimer
    def parse1(self, response):
        # open_in_browser(response)
        yield scrapy.Request(
            url="https://lovingtx.countygovernmentrecords.com/LovingTXRecorder/web/login.jsp?submit=I+Acknowledge",
            callback=self.parse2,
            dont_filter=True,
            # formdata=data,
            method="GET",
            headers=self.headers,
            meta={'handle_httpstatus_list': [200]}
        )
    def parse2(self, response):
        open_in_browser(response)
        yield scrapy.Request(
            url="https://lovingtx.countygovernmentrecords.com/LovingTXRecorder/web/loginPOST.jsp?submit=Public+Login&guest=true",
            callback=self.parse3,
            dont_filter=True,
            # formdata=data,
            method="POST",
            headers=self.headers,
            meta={'handle_httpstatus_list': [302]}
        )
        # "https://lovingtx.countygovernmentrecords.com/LovingTXRecorder/web/loginPOST.jsp?submit=Public+Login&guest=true"
    def parse3(self, response):
        open_in_browser(response)
        # data = {'RecDateIDStart': '07/29/2021', 'RecDateIDEnd': '07/29/2021',
        #         'GrantorIDSearchType': 'Advanced Searching', 'GranteeIDSearchType': 'Basic Searching', 'BothNamesIDSearchType': 'Basic Searching', 'LegalRemarksIDSearchType': 'Starts With', 'AllDocuments': 'ALL', 'docTypeTotal': '275'}
        data = {'RecDateIDStart': '07/29/2021', 'RecDateIDEnd': '07/29/2021', 'GrantorIDSearchType': 'Advanced Searching',
         'GranteeIDSearchType': 'Basic Searching', 'BothNamesIDSearchType': 'Basic Searching',
         'LegalRemarksIDSearchType': 'Starts With', 'AllDocuments': 'ALL', 'docTypeTotal': '275'}

        yield scrapy.FormRequest(
            url="https://lovingtx.countygovernmentrecords.com/LovingTXRecorder/eagleweb/docSearchPOST.jsp",
            callback=self.parse4,
            dont_filter=True,
            formdata=data,
            method="POST",
            headers=self.headers,
            meta={'handle_httpstatus_list': [302]}
        )
    def parse4(self, response):
        open_in_browser(response)
        yield scrapy.Request(
            url="https://lovingtx.countygovernmentrecords.com/LovingTXRecorder/eagleweb/docSearchResults.jsp?searchId=0",
            callback=self.parse5,
            dont_filter=True,
            # formdata=data,
            method="POST",
            headers=self.headers,
            meta={'handle_httpstatus_list': [200]}
        )
    def parse5(self, response):
        open_in_browser(response)
    # def parse5(self, response):
        open_in_browser(response)
        header = {'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9', 'Accept-Encoding': 'gzip, deflate, br', 'Accept-Language': 'en-US,en;q=0.9', 'Cache-Control': 'max-age=0', 'Connection': 'keep-alive', 'Host': 'lovingtx.countygovernmentrecords.com', 'Referer': 'https://lovingtx.countygovernmentrecords.com/LovingTXRecorder/eagleweb/docSearchResults.jsp?searchId=1', 'sec-ch-ua': '"Chromium";v="92", " Not A;Brand";v="99", "Google Chrome";v="92"', 'sec-ch-ua-mobile': '?0', 'Sec-Fetch-Dest': 'document', 'Sec-Fetch-Mode': 'navigate', 'Sec-Fetch-Site': 'same-origin', 'Sec-Fetch-User': '?1', 'Upgrade-Insecure-Requests': '1', 'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/92.0.4515.107 Safari/537.36'}

        total = response.xpath("""//strong/a[contains(@href,"../eagleweb/viewDoc.jsp?node=DOC")]/@href""").getall()
        for text in total:
            text = text.strip("..")
            url = f"https://lovingtx.countygovernmentrecords.com/LovingTXRecorder{text}"

            yield scrapy.Request(
                url =url,
                callback=self.parse6,
                dont_filter=True,
                # formdata=data,
                method="POST",
                headers=header,
                meta={'handle_httpstatus_list': [200]}
            )
    def parse6(self, response):
        open_in_browser(response)
        yield{
            # "Document Type" :response.xpath("//div[@id='middle']/h1/following-sibling::text()[1]").get(default='').replace("\xa0",' '),
            "Document Number" :response.xpath("//span[text()='Document Number']/following-sibling::span/span/text()").get(default='').replace("\xa0",' '),
            "Recording Date" :response.xpath("//span[text()='Recording Date']/following-sibling::span/span/text()").get(default='').replace("\xa0",' '),
            "Volume" :response.xpath("//span[text()='Volume']/following-sibling::span/span/text()").get(default='').replace("\xa0",' '),
            "Page" :response.xpath("//span[text()='Page']/following-sibling::span/span/text()").get(default='').replace("\xa0",' '),
            "Number of Pages" :response.xpath("//span[text()='Number of  Pages']/following-sibling::span/span/text()").get(default='').replace("\xa0",' '),
            "Recording Fee" :response.xpath("//span[text()='Recording Fee']/following-sibling::span/span/text()").get(default='').replace("\xa0",' '),
            "Mortgage Amount" :response.xpath("//span[text()='Mortgage Amount']/following-sibling::span/span/text()").get(default='').replace("\xa0",' '),
            "Document Date" :response.xpath("//span[text()='Document Date']/following-sibling::span/span/text()").get(default='').replace("\xa0",' '),
            "Return Address Name" :response.xpath("//span[text()='Name']/following-sibling::span/span/text()").get(default='').replace("\xa0",' '),
            "Return Address Address 1" :response.xpath("//span[text()='Address 1']/following-sibling::span/span/text()").get(default='').replace("\xa0",' '),
            "Return Address Address 2" :response.xpath("//span[text()='Address 2']/following-sibling::span/span/text()").get(default='').replace("\xa0",' '),
            "Return Address City" :response.xpath("//span[text()='City']/following-sibling::span/span/text()").get(default='').replace("\xa0",' '),
            "Return Address State" :response.xpath("//span[text()='State']/following-sibling::span/span/text()").get(default='').replace("\xa0",' '),
            "Return Address Zip" :response.xpath("//span[text()='Zip']/following-sibling::span/span/text()").get(default='').replace("\xa0",' '),
            "Return Address Mailback" :response.xpath("//span[text()='Mailback']/following-sibling::span/span/text()").get(default='').replace("\xa0",' '),
            "Return Address Destination" :response.xpath("//span[text()='Destination']/following-sibling::span/span/text()").get(default='').replace("\xa0",' '),
            "Return Address Prsented By" :response.xpath("//span[text()='Presented By']/following-sibling::span/span/text()").get(default='').replace("\xa0",' '),
            "Volume " :response.xpath("//th[text()='Volume']/../following-sibling::tr/td[1]/span/text()").get(default='').replace("\xa0",' '),
            "Page " :response.xpath("//th[text()='Page']/../following-sibling::tr/td[2]/span/text()").get(default='').replace("\xa0",' '),
            "Doc Num" :response.xpath("//th[text()='Doc Num']/../following-sibling::tr/td[3]/span/text()").get(default='').replace("\xa0",' '),

            "Grantor": "|".join(i.strip() for i in response.xpath("//th[text()='Grantor']/../following-sibling::tr/td/span/text()").getall()).strip("|").replace("\xa0",' '),
            "Grantee": "|".join(i.strip() for i in response.xpath("//th[text()='Grantee']/../following-sibling::tr/td/span/text()").getall()).strip("|").replace("\xa0",' '),
            "Document Remarks Submit Date": response.xpath("//span[text()='Submit Date']/following-sibling::span/span/text()").get(default='').replace("\xa0", ' '),
            "Document Remarks Packager": response.xpath("//span[text()='Packager']/following-sibling::span/span/text()").get(default='').replace("\xa0", ' '),
            "Document Remarks Tracking Number": response.xpath("//span[text()='Tracking Number']/following-sibling::span/span/text()").get(default='').replace("\xa0", ' '),
            "Document Remarks Rejected Reason'r": response.xpath("//span[text()='Rejected Reason']/following-sibling::span/span/text()").get(default='').replace("\xa0", ' '),
            "Related Links": "|".join(i.strip() for i in response.xpath("//tr/td/a[@class='selectable']/span/text()").getall()).strip("|").replace("\xa0",' '),

        }



from scrapy import cmdline
cmdline.execute("scrapy crawl lovingspider ".split())