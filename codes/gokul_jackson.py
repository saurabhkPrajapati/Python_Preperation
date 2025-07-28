import scrapy
from scrapy.http import headers
from scrapy.utils.response import open_in_browser
import pandas_practice as pd
import re


class AumentwebSpider(scrapy.Spider):
    name = 'Aument'
    id = 1
    full_data = []
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.101 Safari/537.36'}

    def start_requests(self):
        urls = ["http://aumentumweb.jacksongov.org/RealEstate/SearchEntry.aspx"]

        for url in urls:
            yield scrapy.Request(
                url=url,
                callback=self.parse,
                headers=self.headers,
                dont_filter=True,
                method="GET"
            )

    def parse(self, response):
        urls = response.request.url
        eventarg = response.xpath("//input[@id='__EVENTTARGET']/@value").get()
        viewstate = response.xpath("//input[@id='__VIEWSTATE']/@value").get()
        viewstategenerator = response.xpath("//input[@id='__VIEWSTATEGENERATOR']/@value").get()
        eventvalidation = response.xpath("//input[@id='__EVENTVALIDATION']/@value").get()

        p1 = "|0|01"
        p2 = "1999-11-17"
        p3 = "-0-0-0-0||[[[[]],[],[]],[{},[]],'01"
        p4 = "1999-11-17"
        p5 = "-0-0-0-0']"
        # start_date = p1 + self.sd + p3 + self.sd + p5
        # end_date = p1 + self.ed + p3 + self.ed + p5
        # print(start_date)
        data = {
            "__EVENTTARGET": "ctl00$cphNoMargin$SearchButtons2$btnSearch",
            "__EVENTARGUMENT": "0",
            "__VIEWSTATE": viewstate,
            "__VIEWSTATEGENERATOR": viewstategenerator,
            "__EVENTVALIDATION": eventvalidation,
            "Header1_WebHDS_clientState": "",
            "Header1_WebDataMenu1_clientState": "[[null,[[[null,[],null],[{},[]],null]],null],[{},[{},{}]],null]",
            "ctl00$cphNoMargin$f$NameSearchMode": "rdoCombine",
            "cphNoMargin_f_txtParty_clientState": "|0|01||[[[[]],[],[]],[{},[]],'01']",
            "cphNoMargin_f_txtParty": "Lastname Firstname",
            "ctl00$cphNoMargin$f$drbPartyType": "",
            "cphNoMargin_f_txtGrantor_clientState": "|0|00||[[[[]],[],[]],[{},[]],'00']",
            "cphNoMargin_f_txtGrantee_clientState": "|0|00||[[[[]],[],[]],[{},[]],'00']",
            "cphNoMargin_f_ddcDateFiledFrom_clientState": "|0|012021-6-1-0-0-0-0||[[[[]],[],[]],[{},[]],'012021-6-1-0-0-0-0']",
            "cphNoMargin_f_ddcDateFiledTo_clientState": "|0|012021-6-1-0-0-0-0||[[[[]],[],[]],[{},[]],'012021-6-1-0-0-0-0']",
            "cphNoMargin_f_txtInstrumentNoFrom_clientState": "|0|01||[[[[]],[],[]],[{},[]],'01']"

        }

        request = scrapy.FormRequest(
            url=urls,
            callback=self.parse2,
            dont_filter=True,
            formdata=data,
            method="POST",
            headers=self.headers,
            # meta={'handle_httpstatus_list':[302]}
        )
        yield request

    def parse2(self, response):
        # d=response.xpath("//td[@id='cphNoMargin_cphNoMargin_TDSearchResults']/div/div/table/tbody/tr[2]/td/table/tbody[2]/tr/td/div[2]/table/tbody/tr[2]/td[25]").get()

        d = response.xpath(
            "//td[@id='cphNoMargin_cphNoMargin_TDSearchResults']/div/div/table/tr[2]/td/table/tbody[2]/tr/td/div/table/tbody/tr[1]/td[25]/text()").get()

        # "http://aumentumweb.jacksongov.org/RealEstate/SearchResults.aspx?global_id=OPR95482920&type=dtl"
        print(d)
        url = response.request.url + "?global_id=" + str(d) + "&type=dtl"
        yield scrapy.Request(
            url=url,
            method="GET",
            callback=self.parse3,
            headers=self.headers,
            dont_filter=True,
        )

    def parse3(self, response):
        a = ["instrument", "Multi", "Date_record", "doc_type", "Book", "page", "remark"]
        dic = {"instrument": "", "Multi": "", "Date_record": "", "doc_type": "", "Book": "", "page": "", "remark": "",
               "grantor": "", "grantee": "", "name": "", "address": "", }

        for i in range(1, 8):
            dic[a[i - 1]] = response.xpath(
                "(//table[@id='Table1'])[2]/tr[2]/td/table/tr[%s]/td[2]/span/text()" % i).get()

        check = 1
        d1 = ''
        while (response.xpath("(//table[@id='Table1'])[2]/tr[4]/td/table/tr[%s]/td[3]/span/text()" % check).get()):
            d1 += str(response.xpath(
                "(//table[@id='Table1'])[2]/tr[4]/td/table/tr[%s]/td[3]/span/text()" % check).get()) + ', '
            check += 1
        dic["grantor"] = d1

        check = 1
        d1 = ''
        while (response.xpath("(//table[@id='Table1'])[2]/tr[6]/td/table/tr[%s]/td[3]/span/text()" % check).get()):
            d1 += str(response.xpath(
                "(//table[@id='Table1'])[2]/tr[6]/td/table/tr[%s]/td[3]/span/text()" % check).get()) + ', '
            check += 1
        dic["grantee"] = d1

        d1 = ''
        d1 = str(response.xpath("(//table[@id='Table1'])[2]/tr[8]/td/table/tr[1]/td[2]/span[1]/text()").get(default=''))
        d1 += str(
            response.xpath("(//table[@id='Table1'])[2]/tr[8]/td/table/tr[1]/td[2]/span[2]/text()").get(default=''))
        dic["name"] = d1

        dic["address"] = response.xpath("(//table[@id='Table1'])[2]/tr[8]/td/table/tr[2]/td[2]/span/text()").get(
            default='')
        dic["city"] = response.xpath("(//table[@id='Table1'])[2]/tr[8]/td/table/tr[3]/td[2]/span[1]/text()").get(
            default='')
        dic["state"] = response.xpath("(//table[@id='Table1'])[2]/tr[8]/td/table/tr[3]/td[2]/span[1]/text()").get(
            default='')
        dic["zip"] = response.xpath("(//table[@id='Table1'])[2]/tr[8]/td/table/tr[3]/td[2]/span[1]/text()").get(
            default='')

        print(dic)
        self.full_data.append(dic)
        self.id += 1

        if (response.xpath("//option[@selected='selected']/following-sibling::option/@value").get()):
            data = {
                "__EVENTTARGET": "ctl00$cphNoMargin$OptionsBar1$ItemList",
                "__VIEWSTATE": response.xpath("//input[@id='__VIEWSTATE']/@value").get(),
                "__VIEWSTATEGENERATOR": response.xpath("//input[@id='__VIEWSTATEGENERATOR']/@value").get(),
                "__EVENTVALIDATION": response.xpath("//input[@id='__EVENTVALIDATION']/@value").get(),
                "ctl00$cphNoMargin$OptionsBar1$ItemList": response.xpath(
                    "//option[@selected='selected']/following-sibling::option/@value").get(),
                "ctl00$LoginForm1$logonType": "rdoPubCpu"
            }

            yield scrapy.FormRequest(
                url=response.request.url,
                callback=self.parse3,
                method="POST",
                headers=self.headers,
                formdata=data,
                dont_filter=True,
            )
        else:
            print("sucessfull data scraped")
            df = pd.DataFrame(self.full_data)
            df.index = df.index + 1
            # self.sd = re.sub("-", "", self.sd)
            finename = "aumentumweb-" +""+ ".csv"
            df.to_csv(finename, mode='a', index=True, header=True, index_label="No")