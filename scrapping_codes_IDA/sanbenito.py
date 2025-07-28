import scrapy
from scrapy import Request
from scrapy.utils.response import open_in_browser
import time
import re
from selenium import webdriver
from selenium.webdriver.common.keys import Keys

class San(scrapy.Spider):
    name = 'San'
    allowed_domains = []
    start_urls = ["https://sanbenitocountyca-web.tylerhost.net/web/user/disclaimer",
                  ]
    count=2
    def __init__(self):
        self.driver=webdriver.Chrome(r'C:\Users\Saurabh prajapati\PycharmProjects\selenium\chromedriver.exe')

    def parse(self, response):
        self.driver.get(response.url)
        self.driver.implicitly_wait(4)
        self.driver.find_element_by_tag_name('html').send_keys(Keys.PAGE_DOWN)
        self.driver.find_element_by_xpath("//button[@id='submitDisclaimerAccept']").click()# disclaimer
        time.sleep(4)
        self.driver.find_element_by_xpath("(//a[@class='ss-action ss-action-form ss-utility-box ss-action-page-search ui-link'])[1]").click()#official records search
        time.sleep(4)
        self.driver.find_element_by_xpath("(//div[@class='ss-action-internal'])[1]").click()#advanced Search
        time.sleep(4)
        self.driver.find_element_by_xpath("(//input[@onblur='selfservice.dateBlurCallback(event)'])[1]").click()
        time.sleep(2)
        self.driver.find_element_by_xpath("(//input[@onblur='selfservice.dateBlurCallback(event)'])[1]").send_keys("06172021")
        time.sleep(2)
        self.driver.find_element_by_xpath("(//input[@onblur='selfservice.dateBlurCallback(event)'])[2]").click()
        time.sleep(2)
        self.driver.find_element_by_xpath("(//input[@onblur='selfservice.dateBlurCallback(event)'])[2]").send_keys("06172021")
        time.sleep(2)
        self.driver.find_element_by_tag_name('html').send_keys(Keys.PAGE_DOWN)
        time.sleep(2)
        self.driver.find_element_by_xpath("//a[@id='searchButton']").click()
        time.sleep(12)
        link_ids = []
        # lists = driver.find_elements_by_xpath("//li[contains(@class,'ss-search-row ui-li-static ui-body-inherit')]")
        lists = self.driver.find_elements_by_xpath("/html/body/div[1]/div[2]/div/div[2]/div/div[2]/ul/li[3]/ul/li")
        for i in lists:
            link_ids.append(str(i.get_attribute("data-documentid")))
        print(link_ids)
        time.sleep(3)
        self.driver.find_element_by_xpath("//li[contains(@class,'ss-search-row ui-li-static ui-body-inherit')][1]").click()
        time.sleep(4)
        self.driver.find_element_by_xpath("(//p[@class='selfServiceSearchFullResult selfServiceSearchResultNavigation'])[1]").click()
        time.sleep(4)
        response = response.replace(body=self.driver.page_source)
        while True:

            Document_Type = response.xpath("(//li[@class='ui-li-divider ui-bar-a ui-first-child']/following-sibling::li)[1]/text()").get(default='')
            Document_Type = Document_Type.replace('\n', "").replace('\t', "")
            Document_Number = response.xpath("(//strong/../following-sibling::div)[1]/text()").get(default='')
            Recording_Date = response.xpath("(//strong/../following-sibling::div)[2]").get(default='')
            Recording_Date = Recording_Date.replace('<div>', '').replace('</div>', '')
            Number_Page = response.xpath("(//strong/../following-sibling::div)[3]").get(default='')
            Number_Page = Number_Page.replace('<div>', '').replace('</div>', '')
            Grantor= ""
            try:
                 Grantor = str(response.xpath("(//div/strong[text()='Grantor:']/../following-sibling::*)[1]").get(default=""))
                 Grantor=Grantor.replace('<div><ul class="ui-unbulleted-list"><li>',"").replace("</li>\n</ul>\n</div>","").replace('\n',"").replace("<li>","").replace("</li>","|")
                 Grantor = Grantor.replace('<div>','').replace('</div>','')

            except:
                Grantor=""

            try:
               Grantee =str(response.xpath("(//div/strong[text()='Grantee:']/../following-sibling::*)[1]").get(default=""))
               Grantee=Grantee.replace('<div><ul class="ui-unbulleted-list"><li>', "").replace("</li>\n</ul>\n</div>","").replace('\n', "").replace("<li>", "").replace("</li>", "|")
               Grantee=Grantee.replace('<div>', '').replace('</div>', '')
            except:
                Grantee=""


            Assessor_Parcel_Number = str(response.xpath("(//div/strong[text()='Assessor Parcel Number:']/../following-sibling::*)[1]").get(default=""))
            Assessor_Parcel_Number = Assessor_Parcel_Number.replace('<div><ul class="ui-unbulleted-list"><li>', "").replace("</li>\n</ul>\n</div>","").replace('\n', "").replace("<li>", "").replace("</li>", "|")
            Assessor_Parcel_Number=Assessor_Parcel_Number.replace('<div>', '').replace('</div>', '')
            Date = response.xpath("//td[text()='DEED OF TRUST']/following-sibling::*[1]/text()").get(default="")
            Number = response.xpath("//td[text()='DEED OF TRUST']/following-sibling::td[2]/a/text()").get(default="")
            if Date or Number:
                DEED_OF_TRUST = Date + " |" + Number
            else:
                DEED_OF_TRUST = ''

            yield {"Document Type": Document_Type,
                   "Document Number": Document_Number,
                   "Recording_Date": Recording_Date,
                   "Number Pages": Number_Page,
                   "Book Page": "",
                   "Book Type": "",
                    "Grantor": Grantor,
                    "Grantee": Grantee,
                   "Assessor Parcel Number": Assessor_Parcel_Number,
                   "DEED OF TRUST": DEED_OF_TRUST,
                   }
            time.sleep(12)
            Next=self.driver.find_element_by_xpath("//a[text()='Next Result']")
            if Next:

                Next.click()
                time.sleep(12)
                response = response.replace(body=self.driver.page_source)

            else:
                break
