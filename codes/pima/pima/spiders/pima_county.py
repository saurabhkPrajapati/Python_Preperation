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

class PimaSpider(scrapy.Spider):
    name = 'costa'
    headers = {'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
                'Accept-Encoding': 'gzip, deflate, br', 'Accept-Language': 'en-US,en;q=0.9', 'Cache-Control': 'max-age=0',
                'Connection': 'keep-alive', 'Content-Type': 'application/x-www-form-urlencoded',
                 'Host': 'www.recorder.pima.gov', 'Origin': 'https://www.recorder.pima.gov',
                'Referer': 'https://www.recorder.pima.gov/PublicServices/PublicSearch',
                'sec-ch-ua': '" Not;A Brand";v="99", "Google Chrome";v="91", "Chromium";v="91"', 'sec-ch-ua-mobile': '?0',
                'Sec-Fetch-Dest': 'document', 'Sec-Fetch-Mode': 'navigate', 'Sec-Fetch-Site': 'same-origin',
                'Sec-Fetch-User': '?1', 'Upgrade-Insecure-Requests': '1',
                'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36'}

    # def start_requests(self):
    #     urls = "https://www.recorder.pima.gov/PublicServices/PublicSearch"
    #
    #     yield scrapy.Request(
    #         url=urls,
    #         callback=self.parse1,
    #         headers=self.headers,
    #         dont_filter=True,
    #         method="GET"
    #     )
    allowed_domains = []
    start_urls = ["https://www.recorder.pima.gov/PublicServices/PublicSearch"]

    # def random_with_N_digits(self, n):
    #     range_start = 10 ** (n - 1)
    #     range_end = (10 ** n) - 1
    #     return randint(range_start, range_end)

    toCSV = []
    parser = cp.ConfigParser()
    parser.read('config.ini')
    status = str(parser.get("General", "status"))
    startdate = str(parser.get("General", "startdate"))
    start_doc_num = str(parser.get("General", "start_doc_num"))
    # str_doc1, sttr_doc2 = start_doc_num.split('-')
    ending_doc_num = str(parser.get("General", "ending_doc_num"))
    # end_doc1, end_doc2 = ending_doc_num.split('-')

    def parse(self, response):
        open_in_browser(response)
        doc_num = int(self.start_doc_num) - 1
        # if (self.status == "True"):
            # for doc in range(int(self.start_doc_num ), int(self.ending_doc_num)):
            #     doc = str(self.start_doc_num )
        while doc_num <= (int(self.ending_doc_num)-1):
            # print(self.start_doc_num)
            doc_num = doc_num + 1
            eventarg = response.xpath("//input[@id='__EVENTTARGET']/@value").get()
            viewstate = response.xpath("//input[@id='__VIEWSTATE']/@value").get()
            viewstategenerator = response.xpath("//input[@id='__VIEWSTATEGENERATOR']/@value").get()
            eventvalidation = response.xpath("//input[@id='__EVENTVALIDATION']/@value").get()

            data = {
                "__EVENTTARGET": "",
                "__EVENTARGUMENT": "",
                "__VIEWSTATE": viewstate,
                "__VIEWSTATEGENERATOR": viewstategenerator,
                "__EVENTVALIDATION": eventvalidation,
                "ctl00$ContentPlaceHold er1$rblSearchType": "DOC",
                "ContentPlaceHolder1_txtStartDate_clientState": '|0|011982-7-12-0-0-0-0||[[[[]],[],[]],[{},[]],"011982 - 7 - 12 - 0 - 0 - 0 - 0"]',
                "ContentPlaceHolder1_txtEndDate_clientState": '|0|012021-7-21-0-0-0-0||[[[[]],[],[]],[{},[]],"012021 - 7 - 21 - 0 - 0 - 0 - 0"]',
                "ctl00$ContentPlaceHolder1$txtSeq1": f"{str(doc_num)}",
                "ctl00$ContentPlaceHolder1$btnDocumentSearch": "Search",
                "ctl00$ContentPlaceHolder1$ddlMapType": "0",
            "ctl00$ContentPlaceHolder1$_IG_CSS_LINKS_": "../ig_res/Default/ig_texteditor.css|../ig_res/Default/ig_shared.css",

            }

            yield scrapy.FormRequest(
                url="https://www.recorder.pima.gov/PublicServices/PublicSearch",
                callback=self.parse2,
                dont_filter=True,
                formdata=data,
                method="POST",
                headers=self.headers,
                meta={'handle_httpstatus_list':[302]}
            )
        else:
            print("\n\n\n\n\t\t\t The status of the script is Failed\n\n\n")

    def parse2(self, response):
        # open_in_browser(response)
        yield scrapy.Request(
            url="https://www.recorder.pima.gov/PublicServices/PublicDocView",
            callback=self.parse3,
            dont_filter=True,
            # formdata=data,
            method="GET",
             headers=self.headers,
            meta={'handle_httpstatus_list': [200]}
        )
    # def parse3_(selfself,response):
    #     open_in_browser(response)

    def parse3(self,response):
        # open_in_browser(response)
        viewstate = response.xpath("//input[@id='__VIEWSTATE']/@value").get()
        scrollpositiony = response.xpath("//input[@id='__SCROLLPOSITIONY']/@value").get()
        ins = response.xpath("//input[@name='ctl00$ContentPlaceHolder1$hfInstrumentId']/@value").get(default = '0')
        data = {
        "__EVENTTARGET": "ctl00$ContentPlaceHolder1$gvDocuments",
        "__EVENTARGUMENT": "Select$0",
        # "__VIEWSTATE": "pl9WKPdjiJVb6CkTFCY+sSUzO7m+8Tq9mVdF5IvgqDMHS1lpiGGfknTz7g5vdGja17ootjS0EPRCoew/vdWWEC3fPjLFuv/jW8CfpTVBGb8rh+WITwMt0pth0NhH5lYoaaN19yS5HBixEcYDM62s31c+us9FfkfDY37Ou+f1vLQdSL5zaBl6ZUzI2PnwFLqNQqW6b0SETQmbRqcV4cFiTSC5vbP5ns7X5z+Nn9kUPIn6mJsCXhUlDqUl8NcInvzKNoyMYzASWdbAuxJutpMYUapC1aMiWt73T6Gxv6Djqr2HCw7N8A39SdunsOzCLBYIqxn98LKFHXpCZ6OWl0MpfRUVY2mOLnyQIhHS0zywJ8oagCb3Jstpl6ata4hIxiYAHOrx6Txz2MAsdguArizQylkGe9brJ4TujLyComOC2rcFiO9JIILRwtser375BHWa+nHd4uN4Z/UHTpqurOw6eCvQqyoWnz3RmAGcUl7SaSa/euxtgxfA6cRSCpTvD9wu3k2H+r55MGj0Lr4Nrm1+BKqgRHYI3DGSm1kyx3rtYB90vooYEtQIRGX2yYMZWFf52duTOSWYp9/EB4NchAGPrg9JE6ArvIjrPhEUYsMpo/zsub+tZd9i7fkOPano4KkQDzPid63wWyyv9hM8u66BYF6yUSRIebvl60MGeaYPMX//Xt1YMiurKeIil5kAEJ5ep8mML2FKhTMkgt7Sp/AraLQ5XaQARIZ8a8MGP7NKNSwN6k1eWcQ0CAl14T7mndbCu/xwgdfJN2aWXbeC2MMYMSy8y+0Njy6zdQZGbe/1YW3QqbH/9ZwOJ796bhdXGnd7ATYiNg+9wKxUZTwSIBvhMrn7vozMQuL16rF931cD9iF2Oy6uc5Sqikx0gAqcQ/Hs21O0SZAyIs/876FORWAwBYWkgJZtdvqt5rxVHrVBP2WjJHHpOy2XDNVkbG/pr5Z6KDT9kXvtUQSoOIibVGYMPHC+2lkANqyFxqKzDID2wFqk4aGUXEmMR+sHgZFxN7KCWyXXT+y2no84ym+3oZRSoAOOCZjAzJY6jybxXAQwp9nIdA5cMK8SYNmSY8XhGWYz6KPGcsKor/rCwPsZy1bKo6xoKFYL0b0C86cd/KEvPCGfusYLQnUdaZ7XHeO+pVB4+v+mmO/waYlwh8ZD8Cb+QotN0YCRJY4eBEPdTGKRDcnu7ecXr9ZnbRM8JAgZbwzna/zpJaWMN5dgfL+QKZTqOMYrmYTe8aSv9wcU0efxugil66vFSufO+q9U21eg/VfY2Nff8BhflO+AXeJtl1/8CIzSihaeVZZQmVhzVkLOHWIdHKvmnC/Vqfmp/HJZjOeGbqu/uFrxKiqzPQWNynBWnl/PTBQIfGz80MSu7uR5MDwAAQPybd5fSeBnlwSIgMQRyijr/FxEGkPb9aabq78wWutiYUbeJbb5mF6icarqlW1DVP8KUlo8ZCas28SXLisuSxSUi2q2ISE9QdXiqfjXt9Sp5yyfQUgUhz+9VKUvR/Q7rREjtqFlS/48TPF+lDGknbgbjtBFVWc+4UacAMHcQYdDm2Ctl4qxj3Ns4yXDo1ngY1rjvrrijJcwKhmNc/Ymm4Mrvt2qFuYUYcTlOxEPiU7XDxISwnelxcbCtjZJZqRxLv2V5x2D9RTRq2+L1XDOYTRWtluqTSc2kcIKZ4v76mcx3GL5K8U2CMhg1GFMNdeTv1Tilqx6m7b30ozNL8iR7DJvj+m7deAe+a/jEBZx+6hMg0o8mgqwbAKEF7IuH/WluYbtcey3kBRC4h4Qp4AE",
        "__VIEWSTATE": viewstate,
        "__VIEWSTATEGENERATOR": "26BB63E8",
        "__SCROLLPOSITIONX": "0",
        "__SCROLLPOSITIONY": scrollpositiony,
        # "__SCROLLPOSITIONY": "330",
        "ctl00$ContentPlaceHolder1$hfInstrumentId": ins,
        # "ctl00$ContentPlaceHolder1$hfInstrumentId": "0",
        }

        request = scrapy.FormRequest(
            url="https://www.recorder.pima.gov/PublicServices/PublicDocView",
            callback=self.parse4,
            dont_filter=True,
            formdata=data,
            method="POST",
            headers=self.headers,
            #meta={'handle_httpstatus_list': [200]}
        )
        yield request

    def parse4(self,response):
        # open_in_browser(response)

        Docket = response.xpath("//td[text()='Docket:']/following-sibling::td/text()").get(default='')
        Page = response.xpath("//td[text()='Page:']/following-sibling::td/text()").get(default='')
        Pages = response.xpath("//td[text()='Pages:']/following-sibling::td/text()").get(default='')
        Sequence = response.xpath("//td[text()='Sequence:']/following-sibling::td/text()").get(default='')
        Recorded = response.xpath("//td[text()='Recorded:']/following-sibling::td/text()").get(default='')
        Customer_Code = response.xpath("//td[text()='Customer Code:']/following-sibling::td/text()").get(default='')
        Affidavit = response.xpath("//td[text()='Affidavit:']/following-sibling::td/text()").get(default='')
        Exemption = response.xpath("//td[text()='Exemption:']/following-sibling::td/text()").get(default='')
        From = ""
        for i in range(1, 25):
            fr = response.xpath(f"(//tr/td[text()='From']){[i]}/following-sibling::td[1]/text()").get(
                default='') + " " + \
                 response.xpath(f"(//tr/td[text()='From']){[i]}/following-sibling::td[2]/text()").get(default='')
            if fr != " ":
                From = From + "|" + fr
            From = From.strip('|')
        # From= response.xpath("(//tr/td[text()='From'])[1]/following-sibling::td[1]/text()").get(default='') + " " + \
        #      response.xpath("(//tr/td[text()='From'])[1]/following-sibling::td[2]/text()").get(default='')
        To = ""
        for i in range(1, 25):
            to = response.xpath(f"(//tr/td[text()='To']){[i]}/following-sibling::td[1]/text()").get(default='') + " " + \
                 response.xpath(f"(//tr/td[text()='To']){[i]}/following-sibling::td[2]/text()").get(default='')
            if to != " ":
                To = To + "|" + to

            To = To.strip('|')

        Cross_Refrence_To_From = response.xpath(
            "//table[@id='ContentPlaceHolder1_gvCrossReferences']/tbody/tr[2]/td[1]/text()").get(default='')
        Cross_Refrence_Sequence = response.xpath(
            "//table[@id='ContentPlaceHolder1_gvCrossReferences']/tbody/tr[2]/td[2]/text()").get(default='')
        Cross_Refrence_Docket_Page = response.xpath(
            "//table[@id='ContentPlaceHolder1_gvCrossReferences']/tbody/tr[2]/td[3]/text()").get(default='')
        Cross_Refrence_Type = response.xpath(
            "//table[@id='ContentPlaceHolder1_gvCrossReferences']/tbody/tr[2]/td[4]/text()").get(default='')
        yield {
            "Docket": Docket.replace("\xa0", ''),
            "Page": Page.replace("\xa0", ''),
            "Pages": Pages.replace("\xa0", ''),
            "Sequence": Sequence.replace("\xa0", ''),
            "Recorded": Recorded.replace("\xa0", ''),
            "Customer Code": Customer_Code.replace("\xa0", ''),
            "Affidavit": Affidavit.replace("\xa0", ''),
            "Exemption": Exemption.replace("\xa0", ''),
            "From": From.replace("\xa0", ''),
            "To": To.replace("\xa0", ''),
            "Cross Refrence To/From": Cross_Refrence_To_From.replace("\xa0", ''),
            "Cross Refrence Sequence": Cross_Refrence_Sequence.replace("\xa0", ''),
            "Docket Page": Cross_Refrence_Docket_Page.replace("\xa0", ''),
            "Cross Refrence Type ": Cross_Refrence_Type.replace("\xa0", ''),

        }

# from scrapy import cmdline
# cmdline.execute("scrapy crawl pima_county".split())