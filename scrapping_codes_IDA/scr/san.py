import scrapy
from scrapy.http import headers
from scrapy.utils.response import open_in_browser

class SanSpider(scrapy.Spider):
    name = 'san'
    headers= {'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.101 Safari/537.36'}

        
    def start_requests(self):

        urls="http://clerkrecorder.co.santa-cruz.ca.us/"

        yield scrapy.Request(
            url=urls,
            callback=self.parse1,
            headers=self.headers,
            dont_filter=True,
            method="GET"
        )
 
    def parse1(self, response):

        eventarg=response.xpath("//input[@id='__EVENTTARGET']/@value").get()
        viewstate=response.xpath("//input[@id='__VIEWSTATE']/@value").get()
        viewstategenerator=response.xpath("//input[@id='__VIEWSTATEGENERATOR']/@value").get()
        eventvalidation=response.xpath("//input[@id='__EVENTVALIDATION']/@value").get()
        
        
        data={
            "__EVENTTARGET":"ctl00$cph1$lnkAccept",
            "__EVENTARGUMENT": "",
            "__VIEWSTATE":viewstate,
            "__VIEWSTATEGENERATOR":viewstategenerator,
            "__EVENTVALIDATION":eventvalidation,

            "dlgOptionWindow_clientState": "[[[[null,3,null,null,'700px','550px',1,1,0,0,null,0]],[[[[[null,'Copy Options',null]],[[[[[]],[],null],[null,null],[null]],[[[[]],[],null],[null,null],[null]],[[[[]],[],null],[null,null],[null]]],[]],[{},[]],null],[[[[null,null,null,null]],[],[]],[{},[]],null]],[]],[{},[]],'3,0,,,700px,550px,0']",
            "RangeContextMenu_clientState": "[[[[null,null,null,null,1]],[[[[[null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null]],[],[]],[{},[]],null]],null],[{},[{},{}]],null]",
            "LoginForm1_txtLogonName_clientState": "|0|01||[[[[]],[],[]],[{},[]],'01']",
            "LoginForm1_txtLogonName": "",
            "LoginForm1_txtPassword_clientState": "|0|01||[[[[]],[],[]],[{},[]],'01']",
            "LoginForm1_txtPassword": "",
            "ctl00$LoginForm1$logonType": "rdoPubCpu"
        }

        request=scrapy.FormRequest(
            url="http://clerkrecorder.co.santa-cruz.ca.us/",
            callback=self.parse2,
            dont_filter=True,
            formdata=data,
            method="POST",
            headers=self.headers,
            #meta={'handle_httpstatus_list':[302]}
            )
        yield request

    def parse2(self,response):

        yield scrapy.Request(
            url="http://clerkrecorder.co.santa-cruz.ca.us/RealEstate/SearchEntry.aspx",
            callback=self.parse3,
            method="GET",
            dont_filter=True,
            headers=self.headers
        )

    def parse3(self,response):
        viewstate=response.xpath("//input[@id='__VIEWSTATE']/@value").get()
        viewstategenerator=response.xpath("//input[@id='__VIEWSTATEGENERATOR']/@value").get()
        eventvalidation=response.xpath("//input[@id='__EVENTVALIDATION']/@value").get()
        p1="|0|01"
        p2="1999-11-17"
        p3="-0-0-0-0||[[[[]],[],[]],[{},[]],'01"
        p4="1999-11-17"
        p5="-0-0-0-0']"
        start_date=p1+self.sd+p3+self.sd+p5
        end_date=p1+self.ed+p3+self.ed+p5
        print(start_date)
        data={
            "__EVENTTARGET":"ctl00$cphNoMargin$SearchButtons2$btnSearch",
            "__EVENTARGUMENT": "0",
            "__VIEWSTATE":viewstate,
            "__VIEWSTATEGENERATOR":viewstategenerator,
            "__EVENTVALIDATION":eventvalidation,
            "Header1_WebHDS_clientState":"", 
            "Header1_WebDataMenu1_clientState": "[[null,[[[null,[],null],[{},[]],null]],null],[{},[{},{}]],null]",
            "cphNoMargin_f_txtGrantor_clientState":"|0|01||[[[[]],[],[]],[{},[]],'01']",
            "cphNoMargin_f_txtGrantor":"Lastname+Firstname",
            "cphNoMargin_f_ddcDateFiledFrom_clientState": start_date,
            "cphNoMargin_f_ddcDateFiledTo_clientState": end_date,
            "cphNoMargin_f_txtInstrumentNoFrom_clientState":"|0|01||[[[[]],[],[]],[{},[]],'01']",
            "ctl00$LoginForm1$logonType": "rdoPubCpu"
    
            
        }
        yield scrapy.FormRequest(
            url="http://clerkrecorder.co.santa-cruz.ca.us/RealEstate/SearchEntry.aspx",
            callback=self.parse4,
            method="POST",
            dont_filter=True,
            formdata=data,
            headers=self.headers

        )    

    def parse4(self, response):    


        viewstate=response.xpath("//input[@id='__VIEWSTATE']/@value").get()
        viewstategenerator=response.xpath("//input[@id='__VIEWSTATEGENERATOR']/@value").get()
        eventvalidation=response.xpath("//input[@id='__EVENTVALIDATION']/@value").get()
        
        
        data={
            "__EVENTTARGET":"ctl00$ctl00$cphNoMargin$cphNoMargin$SearchCriteriaTop$FullCount1",
            "__EVENTARGUMENT": "",
            "__VIEWSTATE":viewstate,
            "__VIEWSTATEGENERATOR":viewstategenerator,
            "__EVENTVALIDATION":eventvalidation,
            "ctl00$ctl00$LoginForm1$logonType": "rdoPubCpu",
            "dlgOptionWindow_clientState": "[[[[null,3,null,null,'700px','550px',1,1,0,0,null,0]],[[[[[null,'Copy Options',null]],[[[[[]],[],null],[null,null],[null]],[[[[]],[],null],[null,null],[null]],[[[[]],[],null],[null,null],[null]]],[]],[{},[]],null],[[[[null,null,null,null]],[],[]],[{},[]],null]],[]],[{},[]],'3,0,,,700px,550px,0']",
            "RangeContextMenu_clientState": "[[[[null,null,null,null,1]],[[[[[null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null]],[],[]],[{},[]],null]],null],[{},[{},{}]],null]",
            "LoginForm1_txtLogonName_clientState": "|0|01||[[[[]],[],[]],[{},[]],'01']",
            "LoginForm1_txtLogonName": "",
            "LoginForm1_txtPassword_clientState": "|0|01||[[[[]],[],[]],[{},[]],'01']",
            "LoginForm1_txtPassword": "",
            "ctl00$LoginForm1$logonType": "rdoPubCpu"
        }

        request=scrapy.FormRequest(
            url="http://clerkrecorder.co.santa-cruz.ca.us/RealEstate/SearchResults.aspx",
            callback=self.parse5,
            dont_filter=True,
            formdata=data,
            method="POST",
            headers=self.headers,
            )
        yield request


    def parse5(self, response):

       
        for i in range(1,6):
            yield scrapy.Request(
                url="http://clerkrecorder.co.santa-cruz.ca.us/RealEstate/SearchResults.aspx?pg="+str(i),
                callback=self.parse6,
                method="GET",
                dont_filter=True,
                headers=self.headers,
                meta={'page':str(i)}

            )         

    def parse6(self,response):
        d=response.xpath("//td[@id='cphNoMargin_cphNoMargin_TDSearchResults']/div/div/table/tr[2]/td/table/tbody[2]/tr/td/div/table/tbody/tr[1]/td[25]/text()").get()
        

        url1="http://clerkrecorder.co.santa-cruz.ca.us/RealEstate/SearchResults.aspx?global_id="+str(d)+"&type=dtl"
        print("*"*100)
        print("parse6 ->"+url1)
        print("*"*100)
        yield scrapy.Request(
            url=url1,
            method="GET",
            callback=self.parse7,
            headers=self.headers,
            dont_filter=True,
            meta={'page':response.meta['page'].strip()}
        )
    def parse7(self,response):
        #a=["instrument","Multi","Date_record","doc_type","Book","page","remark"]
        #dic={"instrument":"","Multi":"","Date_record":"","doc_type":"","Book":"","page":"","remark":"","grantor":"","grantee":"","name":"","address":"",}
        

        open_in_browser(response)
        page = response.meta['page'].strip()
        instrument=response.xpath("(//table[@id='Table1'])[2]/tr[2]/td/table/tr[1]/td[2]/span/text()").get()
        Multi=response.xpath("(//table[@id='Table1'])[2]/tr[2]/td/table/tr[2]/td[2]/span/text()").get()
        Date_record=response.xpath("(//table[@id='Table1'])[2]/tr[2]/td/table/tr[3]/td[2]/span/text()").get()
        doc_type=response.xpath("(//table[@id='Table1'])[2]/tr[2]/td/table/tr[4]/td[2]/span/text()").get()
        Book=response.xpath("(//table[@id='Table1'])[2]/tr[2]/td/table/tr[5]/td[2]/span/text()").get()
        page=response.xpath("(//table[@id='Table1'])[2]/tr[2]/td/table/tr[6]/td[2]/span/text()").get()
        remark=response.xpath("(//table[@id='Table1'])[2]/tr[2]/td/table/tr[7]/td[2]/span/text()").get()

        
        yield{
            "instrument":instrument,
            "Multi":Multi,
            "Date_record":Date_record,
            "doc_type":doc_type,
            "Book":Book,
            "page":page,
            "page": page,
            "remark":remark

        } 



