import scrapy
from scrapy.http import headers
from scrapy.utils.response import open_in_browser


class Pima(scrapy.Spider):
    name = 'prima'
    headers ={'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
              'Accept-Encoding': 'gzip, deflate, br', 'Accept-Language': 'en-US,en;q=0.9', 'Cache-Control': 'max-age=0',
              'Connection': 'keep-alive', 'Content-Type': 'application/x-www-form-urlencoded', 'Host': 'www.recorder.pima.gov', 'Origin': 'https://www.recorder.pima.gov',
              'Referer': 'https://www.recorder.pima.gov/PublicServices/PublicSearch', 'sec-ch-ua': '" Not;A Brand";v="99", "Google Chrome";v="91", "Chromium";v="91"', 'sec-ch-ua-mobile': '?0',
              'Sec-Fetch-Dest': 'document', 'Sec-Fetch-Mode': 'navigate', 'Sec-Fetch-Site': 'same-origin', 'Sec-Fetch-User': '?1', 'Upgrade-Insecure-Requests': '1',
              'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36'}

    def start_requests(self):
        urls = "https://www.recorder.pima.gov/PublicServices/PublicSearch"
        yield scrapy.Request(
            url=urls,
            callback=self.parse1,
            headers=self.headers,
            dont_filter=True,
            method="GET"
        )
    def parse1(self, response):
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
            'ctl00$ContentPlaceHolder1$rblSearchType': 'DOC',
             'ContentPlaceHolder1_txtStartDate_clientState': '|0|012021-6-19-0-0-0-0||[[[[]],[],[]],[{},[]],"012021-6-18-0-0-0-0"]',
             'ContentPlaceHolder1_txtStartDate': '6/18/2021',
             'ContentPlaceHolder1_txtEndDate_clientState': '|0|012021-6-19-0-0-0-0||[[[[]],[],[]],[{},[]],"012021-6-18-0-0-0-0"]',
             'ContentPlaceHolder1_txtEndDate': '6/18/2021', 'ctl00$ContentPlaceHolder1$btnDocumentSearch': 'Search',
             'ctl00$ContentPlaceHolder1$ddlMapType': '0',
             'ctl00$ContentPlaceHolder1$_IG_CSS_LINKS_': '../ig_res/Default/ig_texteditor.css|../ig_res/Default/ig_shared.css',

        }
        yield scrapy.FormRequest(
            url="https://www.recorder.pima.gov/PublicServices/PublicSearch",
            callback=self.parse2,
            formdata=data,
            dont_filter=True,
            method="POST",
            headers=self.headers,
            meta={'handle_httpstatus_list': [302]}
        )

    def parse2(self,response):
        # open_in_browser(response)
    #     # eventarg = response.xpath("//input[@id='__EVENTTARGET']/@value").get()
    #     viewstate = response.xpath("//input[@id='__VIEWSTATE']/@value").extract()
    #     viewstategenerator = response.xpath("//input[@id='__VIEWSTATEGENERATOR']/@value").get()
    #     eventvalidation = response.xpath("//input[@id='__EVENTVALIDATION']/@value").get()
    #     print(viewstate)
        data = {
            "__EVENTTARGET": "ctl00$ContentPlaceHolder1$gvDocuments",
            "__EVENTARGUMENT": "Page$2",
            "__VIEWSTATE":"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",
            "__VIEWSTATEGENERATOR": "26BB63E8",
            # "__EVENTVALIDATION": eventvalidation,
            "__SCROLLPOSITIONX": "0",
            "__SCROLLPOSITIONY": "330",
            "__VIEWSTATEENCRYPTED":"",
            "ctl00$ContentPlaceHolder1$hfInstrumentId": "0"
        }

        yield scrapy.FormRequest(
            url="https://www.recorder.pima.gov/PublicServices/PublicDocView",
            callback=self.parse3,
            formdata=data,
            dont_filter=True,
            method="POST",
            headers=self.headers,
            meta={'handle_httpstatus_list': [200]}
        )

    def parse3(self,response):
        open_in_browser(response)
        #without open_in_browser viewstate not working
        # count=3
        count=0
        while count<51:
            count+=1
            viewstate = response.xpath("//input[@id='__VIEWSTATE']/@value").get()

            data = {
                "__EVENTTARGET": "ctl00$ContentPlaceHolder1$gvDocuments",
                "__EVENTARGUMENT": f"Page${count}",
                "__VIEWSTATE":   viewstate,
                # "__VIEWSTATE": "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",
                "__VIEWSTATEGENERATOR": "26BB63E8",
                # "__EVENTVALIDATION": eventvalidation,
                "__SCROLLPOSITIONX": "0",
                "__SCROLLPOSITIONY": "330",
                "__VIEWSTATEENCRYPTED": "",
                "ctl00$ContentPlaceHolder1$hfInstrumentId": "0"
            }

            yield scrapy.FormRequest(
                url="https://www.recorder.pima.gov/PublicServices/PublicDocView",
                callback=self.parse4,
                formdata=data,
                dont_filter=True,
                method="POST",
                headers=self.headers,
                meta={'handle_httpstatus_list': [200]}
            )

    def parse4(self,response):
        # open_in_browser(response)
        count=-1
        while count<10:
            count+=1
            viewstate = response.xpath("//input[@id='__VIEWSTATE']/@value").get()
            for i in [
                # "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",
                # "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",
                      "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"
                      ]:

                data = {
                    "__EVENTTARGET": "ctl00$ContentPlaceHolder1$gvDocuments",
                    "__EVENTARGUMENT": f"Select${count}",
                    "__VIEWSTATE": viewstate,
                    # "__VIEWSTATE":"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",
                    "__VIEWSTATEGENERATOR": "26BB63E8",
                    # "__EVENTVALIDATION": eventvalidation,
                    "__SCROLLPOSITIONX": "0",
                    "__SCROLLPOSITIONY": "417",
                    # "__SCROLLPOSITIONY": "330",
                    "__VIEWSTATEENCRYPTED": "",
                    "ctl00$ContentPlaceHolder1$hfInstrumentId": ""
                }

                yield scrapy.FormRequest(
                    url="https://www.recorder.pima.gov/PublicServices/PublicDocView",
                    callback=self.parse5,
                    formdata=data,
                    dont_filter=True,
                    method="POST",
                    headers=self.headers,
                    meta={'handle_httpstatus_list': [200]}
                )


    def parse6(self,response):
        open_in_browser(response)
    def parse5(self,response):
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






from scrapy.cmdline import execute
execute('scrapy crawl prima -o AZ-PRIMA-0612021.csv'.split())
# -o AZ-PRIMA-06182021.csv