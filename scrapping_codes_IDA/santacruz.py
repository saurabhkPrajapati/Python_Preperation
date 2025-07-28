import time

import scrapy
from scrapy.utils.response import open_in_browser
from selenium import webdriver
from selenium.webdriver.common.keys import Keys


class Santacruz(scrapy.Spider):
    name = 'Santacruz'
    allowed_domains = []
    start_urls = ["http://clerkrecorder.co.santa-cruz.ca.us/"]

    count = 2

    def __init__(self):
        self.driver = webdriver.Chrome(r'C:\Users\Saurabh prajapati\PycharmProjects\selenium\chromedriver.exe')

    def parse(self, response):
        self.driver.get(response.url)
        self.driver.implicitly_wait(4)
        self.driver.find_element_by_xpath("//a[text()='Click here to acknowledge the disclaimer and enter the site.']").click()  # disclaimer
        self.driver.find_element_by_xpath("//span[text()='Real Estate']").click()  # disclaimer
        self.driver.find_element_by_xpath("//span[text()='Search Real Estate Index']").click()  # disclaimer
        time.sleep(6)
        self.driver.find_element_by_xpath("(//td[@class='igte_ElectricBlueInner'])[1]").click()
        time.sleep(3)
        self.driver.find_element_by_xpath("//input[contains(@class,'igte_ElectricBlueEditInContainer')][1]").send_keys("_6/18/2021")
        time.sleep(4)

        self.driver.find_element_by_xpath("(//td[contains(@class,'igte_ElectricBlueInner')])[2]").click()
        time.sleep(3)
        self.driver.find_element_by_xpath("(//input[contains(@class,'igte_ElectricBlueEditInContainer')])[2]").send_keys("_6/18/2021")
        time.sleep(2)

        self.driver.find_element_by_tag_name('html').send_keys(Keys.PAGE_DOWN)
        time.sleep(2)
        self.driver.find_element_by_xpath("//span[@id='cphNoMargin_SearchButtons2_btnSearch__3']").click()
        time.sleep(6)
        self.driver.find_element_by_xpath("//a[text()='get full count']").click()
        time.sleep(8)

       #clicks on page 6  [@value='6']
        self.driver.find_element_by_xpath("(//select[@onchange='itemChange(this)'])[1]/option[@value='6']").click()
        self.driver.find_element_by_xpath("(//td[@class=' fauxDetailLink'])[2]").click()




        while True:
            while True:
                response = response.replace(body=self.driver.page_source)
                Instrument = response.xpath("(//span[text()='Instrument #:'])/../following-sibling::td/span/text()").get(default='')
                # Instrument = response.xpath("(//span[contains(@class,'SearchDetailField')])[1]/text()").get(default='')
                Multi_Seq= response.xpath("(//span[text()='Multi Seq:'])/../following-sibling::td/span/text()").get(default='')
                # Multi_Seq= response.xpath("(//span[contains(@class,'SearchDetailField')])[2]/text()").get(default='')
                Date_Filed= response.xpath("(//span[text()='Date Filed:'])/../following-sibling::td/span/text()").get(default='')
                # Date_Filed= response.xpath("(//span[contains(@class,'SearchDetailField')])[3]/text()").get(default='')
                Document_Type = response.xpath("(//span[text()='Document Type:'])/../following-sibling::td/span/text()").get(default='')
                # Document_Type = response.xpath("(//span[contains(@class,'SearchDetailField')])[4]/text()").get(default='')
                Book= response.xpath("(//span[text()='Book:'])/../following-sibling::td/span/text()").get(default='')
                # Book= response.xpath("(//span[contains(@class,'SearchDetailField')])[5]/text()").get(default='')
                Page= response.xpath("(//span[text()='Page:'])/../following-sibling::td/span/text()").get(default='')
                # Page= response.xpath("(//span[contains(@class,'SearchDetailField')])[6]/text()").get(default='')
                Remarks= response.xpath("(//span[text()='Remarks:']/../following-sibling::td/span)[1]/text()").get(default='')
                Pages_in_Image= response.xpath("(//span[text()='# Pages in Image:'])/../following-sibling::td/span/text()").get(default='')
                # Pages_in_Image= response.xpath("(//span[contains(@class,'SearchDetailField')])[8]/text()").get(default='')
                # Image= response.xpath("(//span[text()='Image:'])/../following-sibling::td/span/text()").get(default='')
                Grantor=""
                for i in range(6):
                    try:
                        GrantorFirst= response.xpath(f"(//span[contains(@id,'GrantorFirstName')])[{i}]/text()").get(default="")
                        GrantorLast= response.xpath(f"(//span[contains(@id,'GrantorLastName')])[{i}]/text()").get(default="")

                        Grantor+=GrantorLast+" "+GrantorFirst+"|"
                    except:
                        pass
                Grantor=Grantor.strip(" | ")
                Grantee = ""
                for i in range(6):
                    try:
                        GranteeFirst = response.xpath(f"(//span[contains(@id,'GranteeFirstName')])[{i}]/text()").get(default="")
                        GranteeLast = response.xpath(f"(//span[contains(@id,'GranteeLastName')])[{i}]/text()").get(default="")

                        Grantee += GranteeLast + " " + GranteeFirst + "|"
                        # Grantor=Grantor+""+Grantor_value+"|"
                    except:
                        pass
                Grantee = Grantee.strip(" | ")

                Name =response.xpath("(//span[text()='Name:'])/../following-sibling::td/span[1]/text()").get(default='')+" "+response.xpath("(//span[text()='Name:'])/../following-sibling::td/span[2]/text()").get(default='')
                # Name = ""
                Address =response.xpath("(//span[text()='Address:'])/../following-sibling::td/span[1]/text()").get(default='')
                # City_Zip_State =response.xpath("//span[@id='ctl00_cphNoMargin_f_oprTab_tmpl0_DataList2_ctl00_Label16']/../following-sibling::*/span").getall()
                City_Zip_State=response.xpath("(//span[text()='City, State, Zip:'])/../following-sibling::td/span[1]/text()").get(default='')+" "+response.xpath("(//span[text()='City, State, Zip:'])/../following-sibling::td/span[2]/text()").get(default='')+" "+response.xpath("(//span[text()='City, State, Zip:'])/../following-sibling::td/span[3]/text()").get(default='')
                Remarks_Legal=response.xpath("(//span[text()='Remarks:']/../following-sibling::td/span)[2]/text()").get(default='')
                Type=response.xpath("(//span[text()='Type:'])/../following-sibling::td/span/text()").get(default='')
                APN=response.xpath("(//span[text()='APN:'])/../following-sibling::td/span/span/text()").get(default='')
                yield{
                            "Instrument":Instrument,
                        "Multi Seq":  Multi_Seq,
                        "Date Filed": Date_Filed,
                        "Document_Type": Document_Type,
                        "Book":Book,
                       "Page": Page,
                        "Remarks":Remarks,
                        "Pages in Image":Pages_in_Image,

                        "Image":"",
                        "Grantor":Grantor,
                         "Grantee":Grantee,
                        "Name":Name,
                        "Address":Address,
                            "City Zip State":City_Zip_State,
                            "Type": Type,
                            "APN":APN,
                            "Legal Remarks":Remarks_Legal
                }


                try:
                    # self.driver.find_element_by_xpath("//input[@title='Next' and not(contains(@src,'disabled'))]"):
                    self.driver.find_element_by_xpath("//input[@title='Next' and not(contains(@src,'disabled'))]").click()
                    time.sleep(3)
                except:
                    break


            self.driver.find_element_by_xpath("//a[text()='Back to Results']").click()
            time.sleep(5)
            self.driver.find_element_by_xpath("(//input[@onclick='changeSelect(1);return false;'])[1]").click()
            self.driver.find_element_by_xpath("(//td[@class=' fauxDetailLink'])[2]").click()
            # next.sendkeys(Keys.ARROW_DOWN,Keys.RETURN)
            time.sleep(4)





