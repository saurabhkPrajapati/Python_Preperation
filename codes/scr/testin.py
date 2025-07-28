import scrapy
from scrapy.utils.response import open_in_browser


class Santac(scrapy.Spider):
    name ='Sun'
    # allowed_domains = []
    # start_urls = ["http://clerkrecorder.co.santa-cruz.ca.us/"]


    headers= {
            'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
            'Accept-Encoding': 'gzip, deflate', 'Accept-Language': 'en-US,en;q=0.9', 'Cache-Control': 'max-age=0',
            'Connection': 'keep-alive', 'Content-Type': 'application/x-www-form-urlencoded',
            'Host': 'clerkrecorder.co.santa-cruz.ca.us', 'Origin': 'http://clerkrecorder.co.santa-cruz.ca.us',
            'Referer': 'http://clerkrecorder.co.santa-cruz.ca.us/', 'Upgrade-Insecure-Requests': '1',
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36',
    }

    def start_requests(self):
        urls = "http://clerkrecorder.co.santa-cruz.ca.us/"

        yield scrapy.Request(
            url=urls,
            callback=self.parse1,
            headers=self.headers,
            dont_filter=True,
            method="GET"
        )

    def parse1(self, response):
        # open_in_browser(response)
        # print(response.xpath('/html/body/div[2]/table/tbody/tr/td[2]/div[1]').get())

        view_state = response.xpath("//input[@id='__VIEWSTATE']/@value").get()
        # print(response.xpath("//input[@id='__VIEWSTATE']/@value").getall()[0])
        view_gen = response.xpath("//input[@id='__VIEWSTATEGENERATOR']/@value").get()
        # print(response.xpath("//input[@id='__VIEWSTATEGENERATOR']/@value").get())
        event_valid = response.xpath("//input[@id='__EVENTVALIDATION']/@value").get()
        # print(response.xpath("//input[@id='__EVENTVALIDATION']/@value").get())




        data = {
                "__EVENTTARGET":"ctl00$cph1$lnkAccept",
                # "__EVENTARGUMENT":EVENTARGUMENT ,
                "__EVENTARGUMENT":"" ,
                "__VIEWSTATE": view_state,
                "__VIEWSTATEGENERATOR": view_gen,
                "__EVENTVALIDATION": event_valid,
                'dlgOptionWindow_clientState': '[[[[null,3,null,null,"700px","550px",1,1,0,0,null,0]],[[[[[null,"Copy Options",null]],[[[[[]],[],null],[null,null],[null]],[[[[]],[],null],[null,null],[null]],[[[[]],[],null],[null,null],[null]]],[]],[{},[]],null],[[[[null,null,null,null]],[],[]],[{},[]],null]],[]],[{},[]],"3,0,,,700px,550px,0"]',
                'RangeContextMenu_clientState': '[[[[null,null,null,null,1]],[[[[[null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null]],[],[]],[{},[]],null]],null],[{},[{},{}]],null]',
                'LoginForm1_txtLogonName_clientState': '|0|01||[[[[]],[],[]],[{},[]],"01"]',
                'LoginForm1_txtPassword_clientState': '|0|01||[[[[]],[],[]],[{},[]],"01"]',
                'ctl00$LoginForm1$logonType': 'rdoPubCpu',
                'ctl00$_IG_CSS_LINKS_': '~/localization/style.css|~/localization/styleforsearch.css|~/favicon.ico|~/localization/styleFromCounty.css|ig_res/Default/ig_texteditor.css|ig_res/Default/ig_datamenu.css|ig_res/ElectricBlue/ig_dialogwindow.css|ig_res/ElectricBlue/ig_shared.css|ig_res/Default/ig_shared.css',
        }
        yield scrapy.FormRequest(
            url="http://clerkrecorder.co.santa-cruz.ca.us/",
            formdata=data,
            headers=self.headers,
            callback=self.parse2,
            method="POST",
            dont_filter=True,
            meta={'handle_httpstatus_list': [302]}
        )


    def parse2(self, response):
        # print(response.xpath('/html/body/div[2]/table/tbody/tr/td[2]/div[1]').get())
        # open_in_browser(response)
        yield scrapy.Request(
            url="http://clerkrecorder.co.santa-cruz.ca.us/RealEstate/SearchEntry.aspx",
            method='GET',
            headers=self.headers,
            dont_filter=True,
            callback=self.parse3,
        )
    def parse3(self,response):
        # open_in_browser(response)
        headers={'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
                 'Accept-Encoding': 'gzip, deflate', 'Accept-Language': 'en-US,en;q=0.9', 'Cache-Control': 'max-age=0', 'Connection': 'keep-alive',
                'Content-Type': 'application/x-www-form-urlencoded', 'Host': 'clerkrecorder.co.santa-cruz.ca.us', 'Origin': 'http://clerkrecorder.co.santa-cruz.ca.us',
                'Referer': 'http://clerkrecorder.co.santa-cruz.ca.us/RealEstate/SearchEntry.aspx', 'Upgrade-Insecure-Requests': '1',
                'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36'
                }

        viewstate = response.xpath("//input[@id='__VIEWSTATE']/@value").get()
        viewstategenerator = response.xpath("//input[@id='__VIEWSTATEGENERATOR']/@value").get()
        eventvalidation = response.xpath("//input[@id='__EVENTVALIDATION']/@value").get()

        data = {
            "__EVENTTARGET": "ctl00$cphNoMargin$SearchButtons2$btnSearch",
            "__EVENTARGUMENT": "0",
            "__VIEWSTATE": viewstate,
            "__VIEWSTATEGENERATOR": viewstategenerator,
            "__EVENTVALIDATION": eventvalidation,
            'Header1_WebDataMenu1_clientState': '[[null,[[[null,[],null],[{},[]],null]],null],[{},[{},{}]],null]',
             'cphNoMargin_f_txtGrantor_clientState': '|0|01||[[[[]],[],[]],[{},[]],"01"]',
             'cphNoMargin_f_txtGrantor': 'Lastname Firstname',
             'cphNoMargin_f_ddcDateFiledFrom_clientState': '|0|012021-6-18-0-0-0-0||[[[[]],[],[]],[{},[]],"012021-6-18-0-0-0-0"]',
             'cphNoMargin_f_ddcDateFiledTo_clientState': '|0|012021-6-18-0-0-0-0||[[[[]],[],[]],[{},[]],"012021-6-18-0-0-0-0"]',
             'cphNoMargin_f_txtInstrumentNoFrom_clientState': '|0|01||[[[[]],[],[]],[{},[]],"01"]',
             'cphNoMargin_f_txtInstrumentNoTo_clientState': '|0|01||[[[[]],[],[]],[{},[]],"01"]',
             'cphNoMargin_f_txtBook_clientState': '|0|01||[[[[]],[],[]],[{},[]],"01"]',
             'cphNoMargin_f_txtPage_clientState': '|0|01||[[[[]],[],[]],[{},[]],"01"]',
             'cphNoMargin_f_busZip_clientState': '|0|01\x15\x15\x15-\x15\x15\x15-\x15\x15\x15-\x15\x15\x15||[[[[]],[],[]],[{},[]],"01\x15\x15\x15-\x15\x15\x15-\x15\x15\x15-\x15\x15\x15"]',
             'cphNoMargin_dlgPopup_clientState': '[[[[null,3,null,null,null,null,1,1,0,0,null,0]],[[[[[null,"Document Image",null]],[[[[[]],[],null],[null,null],[null]],[[[[]],[],null],[null,null],[null]],[[[[]],[],null],[null,null],[null]]],[]],[{},[]],null],[[[[null,null,null,null]],[],[]],[{},[]],null]],[]],[{},[]],"3,0,,,,,0"]',
             'dlgOptionWindow_clientState': '[[[[null,3,null,null,"700px","550px",1,1,0,0,null,0]],[[[[[null,"Copy Options",null]],[[[[[]],[],null],[null,null],[null]],[[[[]],[],null],[null,null],[null]],[[[[]],[],null],[null,null],[null]]],[]],[{},[]],null],[[[[null,null,null,null]],[],[]],[{},[]],null]],[]],[{},[]],"3,0,,,700px,550px,0"]',
             'RangeContextMenu_clientState': '[[[[null,null,null,null,1]],[[[[[null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null]],[],[]],[{},[]],null]],null],[{},[{},{}]],null]',
             'LoginForm1_txtLogonName_clientState': '|0|01||[[[[]],[],[]],[{},[]],"01"]',
             'LoginForm1_txtPassword_clientState': '|0|01||[[[[]],[],[]],[{},[]],"01"]',
             'ctl00$LoginForm1$logonType': 'rdoPubCpu',
             '_ig_def_dp_cal_clientState': '|0|15,2021,06,2021,6,18||[[null,[],null],[{},[]],"11,2021,06,2021,6,18"]',
             'ctl00$_IG_CSS_LINKS_': '~/localization/style.css|~/localization/styleforsearch.css|~/favicon.ico|~/localization/styleFromCounty.css|../ig_res/Default/ig_monthcalendar.css|../ig_res/ElectricBlue/ig_texteditor.css|../ig_res/Default/ig_texteditor.css|../ig_res/Default/ig_datamenu.css|../ig_res/ElectricBlue/ig_dialogwindow.css|../ig_res/ElectricBlue/ig_datamenu.css|../ig_res/ElectricBlue/ig_shared.css|../ig_res/Default/ig_shared.css',
             'ctl00$cphNoMargin$SearchButtons2$btnSearch__10': ':0'

        }
        yield scrapy.FormRequest(
            url="http://clerkrecorder.co.santa-cruz.ca.us/RealEstate/SearchEntry.aspx",
            # url="http://clerkrecorder.co.santa-cruz.ca.us/RealEstate/SearchEntry.aspx?e=newSession",
            callback=self.parse4,
            method="POST",
            dont_filter=True,
            formdata=data,
            headers=headers,
        meta = {'handle_httpstatus_list': [302]}

        )

    def parse4(self, response):
        open_in_browser(response)

        yield scrapy.Request(
            url="http://clerkrecorder.co.santa-cruz.ca.us/RealEstate/SearchResults.aspx",
            callback=self.parse5,
            method="GET",
            dont_filter=True,
            headers=self.headers,
            # meta={'handle_httpstatus_list': [302]},

        )
    def parse5(self, response):
        yield{
            'a':response.xpath('//*[@id="ctl00_ctl00_cphNoMargin_cphNoMargin_g_G1_ctl00_it3_0_Label1"]/text()').get()
              }
    #
    # def parse5(self, response):
    #     open_in_browser(response)
    #
    #     yield scrapy.Request(
    #         url="http://clerkrecorder.co.santa-cruz.ca.us/RealEstate/SearchEntry.aspx",
    #         callback=self.parse6,
    #         method="GET",
    #         dont_filter=True,
    #         headers=self.headers,
    #
    #     )
    #
    #
    # def parse6(self, response):
    #     yield{
    #         "instrument":response.xpath("(//table[@id='Table1'])[2]/tr[2]/td/table/tr[1]/td[2]/span/text()").get()
    #           }
