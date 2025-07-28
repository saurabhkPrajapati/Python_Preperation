import scrapy
from scrapy.utils.response import open_in_browser


class jacksoncounty(scrapy.Spider):
    name = 'Jackson'
    allowed_domains = []
    start_urls = ["http://aumentumweb.jacksongov.org/RealEstate/SearchEntry.aspx"]


    headers= {
        "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9",
        "Accept-Encoding": "gzip, deflate",
        "Accept-Language": "en-GB,en-US;q=0.9,en;q=0.8",
        "Cache-Control": "max-age=0",
        "Content-Type": "application/x-www-form-urlencoded",
        "Host": "aumentumweb.jacksongov.org",
        "Origin": "http://aumentumweb.jacksongov.org",
        "Referer": "http://aumentumweb.jacksongov.org/RealEstate/SearchEntry.aspx?e=newSession",
        "Upgrade-Insecure-Requests": "1",
        'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.101 Safari/537.36'
    }

    full_data = []

    def parse(self, response):
        #event_target = response.xpath("//input[@id='__EVENTTARGET'].text()").getall()
        #event_argument = response.xpath("//input[@id='__EVENTARGUMENT'].text()").getall()
        view_state = response.xpath("//input[@id='__VIEWSTATE']/@value").getall()
        view_gen = response.xpath("//input[@id='__VIEWSTATEGENERATOR']/@value").getall()
        event_valid = response.xpath("//input[@id='__EVENTVALIDATION']/@value").getall()

        data = {
                "__EVENTTARGET": "ctl00$cphNoMargin$SearchButtons2$btnSearch",
                "__EVENTARGUMENT":"0",
                "__VIEWSTATE": view_state,
                "__VIEWSTATEGENERATOR": view_gen,
                "__EVENTVALIDATION": event_valid,
                "cphNoMargin_f_ddcDateFiledFrom_clientState": "|0|012021-6-1-0-0-0-0||[[[[]],[],[]],[{},[]],'012021-6-1-0-0-0-0']",
                "cphNoMargin_f_ddcDateFiledTo_clientState": "|0|012021-6-1-0-0-0-0||[[[[]],[],[]],[{},[]],'012021-6-1-0-0-0-0']",
                }
        yield scrapy.FormRequest(
            url="http://aumentumweb.jacksongov.org/RealEstate/SearchEntry.aspx",
            formdata=data,
            headers=self.headers,
            callback=self.parse2,
            method="POST",
            dont_filter=True,
            meta={'handle_httpstatus_list': [302]}
        )

    def parse2(self, response):
        yield scrapy.Request(
        url = "http://aumentumweb.jacksongov.org/RealEstate/SearchResults.aspx",
        method = 'GET',
        headers=self.headers,
        callback=self.parse3,
        )


    def parse3(self, response):
        header = {
            "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9",
            "Accept-Encoding": "gzip, deflate",
            "Accept-Language": "en-GB,en-US;q=0.9",
            "Host": "aumentumweb.jacksongov.org",
            "Referer": "http://aumentumweb.jacksongov.org/RealEstate/SearchEntry.aspx",
            "Upgrade-Insecure-Requests": "1",
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) "
                          "Chrome/91.0.4472.101 Safari/537.36",
            "Connection": "keep-alive",

        }
        yield scrapy.Request(
        url = "http://aumentumweb.jacksongov.org/RealEstate/SearchResults.aspx?global_id=OPR295198080&type=dtl",
        method = 'POST',
        headers=header,
        callback=self.parse4,
        meta={'handle_httpstatus_list': [302]}
        )

    def parse4(self, response):
        yield scrapy.Request(
        url = "http://aumentumweb.jacksongov.org/RealEstate/SearchDetail.aspx",
        method = 'GET',
        headers=self.headers,
        callback=self.parse5,
        )

    def parse5(self, response):
        Inst_no = response.xpath('//span[contains(text(), "Instrument")]/../following-sibling::td/span/text()').get(
            default='').strip()

        Multi_seq = response.xpath('//span[contains(text(), "Multi Seq:")]/../following-sibling::td/span/text()').get(
            default='').strip()

        Data_recorded = response.xpath('//span[contains(text(),"Date Recorded:")]/../following-sibling::td/span/text()').get(
            default='').strip()

        Document_type = response.xpath('//span[contains(text(),"Document Type:")]/../following-sibling::td/span/text()').get(
            default='').strip()

        Book = response.xpath('//span[contains(text(),"Book:")]/../following-sibling::td/span/text()').get(default='').strip()

        Pages = response.xpath('//span[contains(text(),"Page:")]/../following-sibling::td/span/text()').get(default='').strip()

        Remarks = response.xpath('//span[contains(text(),"Remarks:")]/../following-sibling::td/span/text()').get(default='').strip()

        Pages_in_img = response.xpath('//span[contains(text(),"Pages in Image:")]/../following-sibling::td/span/text()').get(default='').strip()

        #Grantors = '|'.join(i.strip() for i in response.xpath('').getall() if i != '')

        #Grantees = '|'.join(i.strip() for i in response.xpath('').getall() if i != '')

        Returnee_name = response.xpath('//span[contains(text(),"Name")]/../following-sibling::td/span/text()').get(default='').strip()

        Returnee_address = response.xpath('//span[contains(text(),"Address")]/../following-sibling::td/span/text()').get(default='').strip()

        Returnee_city = response.xpath('//span[contains(text(),"City")]/../following-sibling::td/span/text()').get(default='').strip()

        Returnee_state = response.xpath('//span[contains(text(),"State")]/../following-sibling::td/span[2]/text()').get(default='').strip()

        Returnee_zip = response.xpath('//span[contains(text(),"Zip")]/../following-sibling::td/span[3]/text()').get(default='').strip()
        grantor_1 = response.xpath(
            "//span[@id='ctl00_cphNoMargin_f_oprTab_tmpl0_DataList11_ctl00_lblGrantorLastName']/text()").get(default='')
        grantor_2 = response.xpath(
            "//span[@id='ctl00_cphNoMargin_f_oprTab_tmpl0_DataList11_ctl01_lblGrantorLastName']/text()").get(default='')

        if grantor_2:
            grantors = grantor_1 + "|" + grantor_2
        else:
            grantors = grantor_1

        granteefirst1 = response.xpath(
            "//span[@id='ctl00_cphNoMargin_f_oprTab_tmpl0_Datalist1_ctl00_lblGranteeLastName']/text()").get(default='')
        granteelast1 = response.xpath(
            "//span[@id='ctl00_cphNoMargin_f_oprTab_tmpl0_Datalist1_ctl00_lblGranteeFirstName']/text()").get(default='')
        granteefirst = granteefirst1 + "" + granteelast1
        granteelast2 = response.xpath(
            "//span[@id='ctl00_cphNoMargin_f_oprTab_tmpl0_Datalist1_ctl01_lblGranteeLastName']/text()").get(default='')
        granteefirst2 = response.xpath(
            "//span[id='ctl00_cphNoMargin_f_oprTab_tmpl0_Datalist1_ctl01_lblGranteeFirstName']/text()").get(default='')
        granteesecond = granteelast2 + "" + granteefirst2
        if granteesecond:
            grantees = grantees = granteefirst + "|" + granteesecond
        else:
            grantees = grantees = granteefirst
        yield{
            "instrument_number": Inst_no,
            "multi_seq": Multi_seq,
            "data_record": Data_recorded,
            "Doc_type": Document_type,
            "book": Book,
            "no_of_pages": Pages,
            "remark": Remarks,
            "POI": Pages_in_img,
            "Grantors": grantors,
            "Grantees": grantees,
            "returnee_name": Returnee_name,
            "returnee_address": Returnee_address,
            "returnee_city": Returnee_city,
            "returnee_state": Returnee_state,
            "returnee_zip": Returnee_zip,
        }
        header = {
            "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9",
            "Accept-Encoding": "gzip, deflate",
            "Accept-Language": "en-GB,en-US;q=0.9",
            "Host": "aumentumweb.jacksongov.org",
            "Referer": "http://aumentumweb.jacksongov.org/RealEstate/SearchEntry.aspx",
            "Upgrade-Insecure-Requests": "1",
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) "
                          "Chrome/91.0.4472.101 Safari/537.36",
            "Connection": "keep-alive",

        }
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
                callback=self.parse5,
                method="POST",
                headers=header,
                formdata=data,
                dont_filter=True,
            )

from scrapy.cmdline import execute
execute('scrapy crawl Jackson -o jackson.csv'.split())

