import scrapy
import pandas_practice as pd
from scrapy.utils.response import open_in_browser


class JacksonSpider(scrapy.Spider):
    name = 'jackson_county'
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

    def parse5(self, response, **kwargs):

        print('Extraction Starts Here----------------------------------------')
        a = ["instrument", "multi", "record_date", "doc_type", "book", "pages", "grantor_1", "grantor_2", "grantee_1","grantee_2","returnee_name","address","city","state","zip", "legal_desc"]

        dic = {"instrument": "", "multi": "", "record_date": "", "doc_type": "", "book": "", "pages": "",
               "grantor_1": "","grantor_2": "", "grantee_1": "","grantee_2": "","returnee_name":"","returnee_address":"","returnee_city":"","returnee_state":"","returnee_zip":"", "legal_desc": ""}

        dic["instrument"] = response.xpath(
            "//span[@id='ctl00_cphNoMargin_f_oprTab_tmpl0_documentInfoList_ctl00_txtInstrumentNo']/text()").get()

        dic["multi"] = response.xpath(
            "//span[@id='ctl00_cphNoMargin_f_oprTab_tmpl0_documentInfoList_ctl00_Datalabel4']/text()").get()

        dic["record_date"] = response.xpath(
            "//span[@id='ctl00_cphNoMargin_f_oprTab_tmpl0_documentInfoList_ctl00_DataLabel3']/text()").get()

        dic["doc_type"] = response.xpath(
            "//span[@id='ctl00_cphNoMargin_f_oprTab_tmpl0_documentInfoList_ctl00_Datalabel2']/text()").get()

        dic["book"] = response.xpath(
            "//span[@id='ctl00_cphNoMargin_f_oprTab_tmpl0_documentInfoList_ctl00_DataLabel5']/text()").get()

        dic["pages"] = response.xpath(
            "//span[@id='ctl00_cphNoMargin_f_oprTab_tmpl0_documentInfoList_ctl00_DataLabel6']/text()").get()

        dic["grantor_1"] = response.xpath(
            "//span[@id='ctl00_cphNoMargin_f_oprTab_tmpl0_DataList11_ctl00_lblGrantorLastName']/text()").get()

        try:
            dic["grantor_2"] = response.xpath(
            "//span[@id='ctl00_cphNoMargin_f_oprTab_tmpl0_DataList11_ctl01_lblGrantorLastName']/text()").get()
        except:
            dic["grantor_2"] = "None"
        else:
            dic["grantor_2"] = response.xpath(
                "//span[@id='ctl00_cphNoMargin_f_oprTab_tmpl0_DataList11_ctl01_lblGrantorLastName']/text()").get()

        list1 = response.xpath(
            "//span[@id='ctl00_cphNoMargin_f_oprTab_tmpl0_Datalist1_ctl00_lblGranteeLastName']/text()|//span[@id='ctl00_cphNoMargin_f_oprTab_tmpl0_Datalist1_ctl00_lblGranteeFirstName']/text()").getall()
        str1 = ' '.join(list1)
        dic["grantee_1"] = str1

        try:
            list2 = response.xpath(
                "//span[@id='ctl00_cphNoMargin_f_oprTab_tmpl0_Datalist1_ctl01_lblGranteeLastName']/text()|//span[id='ctl00_cphNoMargin_f_oprTab_tmpl0_Datalist1_ctl01_lblGranteeFirstName']/text()").getall()
            str2 = ' '.join(list2)
            dic["grantee_2"] = str2

        except:
            dic["grantee_2"] = "None"

        else:
            list2 = response.xpath(
                "//span[@id='ctl00_cphNoMargin_f_oprTab_tmpl0_Datalist1_ctl01_lblGranteeLastName']/text()|//span[id='ctl00_cphNoMargin_f_oprTab_tmpl0_Datalist1_ctl01_lblGranteeFirstName']/text()").getall()
            str2 = ' '.join(list2)
            dic["grantee_2"] = str2



        dic["returnee_name"] = response.xpath(
            "//span[@id='ctl00_cphNoMargin_f_oprTab_tmpl0_DataList2_ctl00_Datalabel12']/text()").get()

        dic["returnee_address"] = response.xpath(
            "//span[@id='ctl00_cphNoMargin_f_oprTab_tmpl0_DataList2_ctl00_Datalabel14']/text()").get()

        dic["returnee_city"] = response.xpath(
            "//span[@id='ctl00_cphNoMargin_f_oprTab_tmpl0_DataList2_ctl00_Datalabel16']/text()").get()

        dic["returnee_state"] = response.xpath(
            "//span[@id='ctl00_cphNoMargin_f_oprTab_tmpl0_DataList2_ctl00_Datalabel17']/text()").get()

        dic["returnee_zip"] = response.xpath(
            "//span[@id='ctl00_cphNoMargin_f_oprTab_tmpl0_DataList2_ctl00_Datalabel18']/text()").get()

        dic["legal_desc"] = response.xpath(
            "// span[ @ id = 'ctl00_cphNoMargin_f_oprTab_tmpl1_LegalSubdivisions_ctl01_Label25'] / text()").get()

        self.full_data.append(dic)
        print(dic)

        yield self.full_data

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
        else:
            df = pd.DataFrame(self.full_data)
            df.index = df.index + 1
            df.to_csv(r"C:\Users\Vishwa\Desktop\Ida\scrapy\Completed task\Jackson\MO-Jackson-06012021-scrappy.csv",
                      mode='a', index=True, header=True, index_label="No")



