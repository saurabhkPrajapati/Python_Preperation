import scrapy
from scrapy import Request
from scrapy.utils.response import open_in_browser
import time
import re
from selenium import webdriver
from selenium.webdriver.common.keys import Keys

class Prima(scrapy.Spider):
    name = 'prima'
    allowed_domains = []
    start_urls = [
        "https://www.recorder.pima.gov/PublicServices/PublicSearch",
                  ]

    def __init__(self):
        self.driver = webdriver.Chrome(r'C:\Users\Saurabh prajapati\PycharmProjects\selenium\chromedriver.exe')

    def parse(self, response):
        self.driver.get(response.url)
        self.driver.implicitly_wait(6)
        self.driver.find_element_by_xpath("//div/input[@name='ContentPlaceHolder1_txtStartDate']").click()
        # not wroking self.driver.find_element_by_xpath("//div/input[@name='ContentPlaceHolder1_txtStartDate']").send_keys(Keys.CONTROL, "a", Keys.BACK_SPACE)
        self.driver.find_element_by_xpath("//div/input[@name='ContentPlaceHolder1_txtStartDate']").send_keys("6/18/2021")
        time.sleep(4)
        self.driver.find_element_by_xpath("//div/input[@name='ContentPlaceHolder1_txtEndDate']").click()
        # not working self.driver.find_element_by_xpath("//div/input[@name='ContentPlaceHolder1_txtEndDate']").send_keys(Keys.CONTROL, "a", Keys.BACK_SPACE)
        self.driver.find_element_by_xpath("//div/input[@name='ContentPlaceHolder1_txtEndDate']").send_keys("6/18/2021")

        time.sleep(4)
        self.driver.find_element_by_tag_name('html').send_keys(Keys.PAGE_DOWN)
        self.driver.find_element_by_xpath("//input[@name='ctl00$ContentPlaceHolder1$btnDocumentSearch']").click()
        time.sleep(7)
        self.driver.find_element_by_xpath("//button[text()='Ok']").click()
        time.sleep(4)
        count=1
        temp=0
        while True:

            count+=1
            for i in range(1,11):
                self.driver.find_element_by_xpath(f"(//input[@type='button']){[i]}").click()
                time.sleep(6)
                response = response.replace(body=self.driver.page_source)
                Docket = response.xpath("//td[text()='Docket:']/following-sibling::td/text()").get(default='')
                Page= response.xpath("//td[text()='Page:']/following-sibling::td/text()").get(default='')
                Pages= response.xpath("//td[text()='Pages:']/following-sibling::td/text()").get(default='')
                Sequence= response.xpath("//td[text()='Sequence:']/following-sibling::td/text()").get(default='')
                Recorded= response.xpath("//td[text()='Recorded:']/following-sibling::td/text()").get(default='')
                Customer_Code= response.xpath("//td[text()='Customer Code:']/following-sibling::td/text()").get(default='')
                Affidavit= response.xpath("//td[text()='Affidavit:']/following-sibling::td/text()").get(default='')
                Exemption= response.xpath("//td[text()='Exemption:']/following-sibling::td/text()").get(default='')
                From=""
                for i in range(1,25):
                    fr = response.xpath(f"(//tr/td[text()='From']){[i]}/following-sibling::td[1]/text()").get(default='')+ " "+\
                         response.xpath(f"(//tr/td[text()='From']){[i]}/following-sibling::td[2]/text()").get(default='')
                    if fr != " ":
                        From = From + "|" + fr
                    From = From.strip('|')
                # From= response.xpath("(//tr/td[text()='From'])[1]/following-sibling::td[1]/text()").get(default='') + " " + \
                #      response.xpath("(//tr/td[text()='From'])[1]/following-sibling::td[2]/text()").get(default='')
                To=""
                for i in range(1, 25):
                    to= response.xpath(f"(//tr/td[text()='To']){[i]}/following-sibling::td[1]/text()").get(default='') + " " + \
                           response.xpath(f"(//tr/td[text()='To']){[i]}/following-sibling::td[2]/text()").get(default='')
                    if to != " ":
                        To = To +"|"+ to

                    To = To.strip('|')

                Cross_Refrence_To_From = response.xpath("//table[@id='ContentPlaceHolder1_gvCrossReferences']/tbody/tr[2]/td[1]/text()").get(default='')
                Cross_Refrence_Sequence= response.xpath("//table[@id='ContentPlaceHolder1_gvCrossReferences']/tbody/tr[2]/td[2]/text()").get(default='')
                Cross_Refrence_Docket_Page = response.xpath("//table[@id='ContentPlaceHolder1_gvCrossReferences']/tbody/tr[2]/td[3]/text()").get(default='')
                Cross_Refrence_Type = response.xpath("//table[@id='ContentPlaceHolder1_gvCrossReferences']/tbody/tr[2]/td[4]/text()").get(default='')
                yield{
                    "Docket":Docket.replace("\xa0",''),
                    "Page":Page.replace("\xa0",''),
                    "Pages":Pages.replace("\xa0",''),
                    "Sequence":Sequence.replace("\xa0",''),
                    "Recorded":Recorded.replace("\xa0",''),
                    "Customer Code":Customer_Code.replace("\xa0",''),
                    "Affidavit":Affidavit.replace("\xa0",''),
                    "Exemption":Exemption.replace("\xa0",''),
                    "From":From.replace("\xa0",''),
                    "To":To.replace("\xa0",''),
                    "Cross Refrence To/From":Cross_Refrence_To_From.replace("\xa0",''),
                    "Cross Refrence Sequence":Cross_Refrence_Sequence.replace("\xa0",''),
                    "Docket Page":Cross_Refrence_Docket_Page.replace("\xa0",''),
                    "Cross Refrence Type ":Cross_Refrence_Type.replace("\xa0",''),

                }
            try:
                self.driver.find_element_by_xpath(f"//a[text()='{count}']").click()
                time.sleep(6)


            except:
                temp+=1
                if temp > 4:
                    break
                try:
                    self.driver.find_element_by_xpath("(//a[text()='...'])[2]").click()
                    time.sleep(6)

                except:
                    self.driver.find_element_by_xpath("(//a[text()='...'])[1]").click()
                    time.sleep(6)


from scrapy.cmdline import execute
execute('scrapy crawl prima -o AZ-PRIMA-06182021.csv'.split())
