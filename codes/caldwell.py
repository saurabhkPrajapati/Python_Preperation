import scrapy
from scrapy import Request
from scrapy.utils.response import open_in_browser
from time import sleep as s
import re
from selenium import webdriver
from selenium.webdriver.common.keys import Keys

class Caldwell(scrapy.Spider):
    name = 'caldwell'
    allowed_domains = []
    start_urls = ["http://72.15.246.185/CaldwellNCNW/application.asp?resize=true",
                  ]
    count=2
    def __init__(self):
        # self.driver=webdriver.Chrome(r'C:\Users\Saurabh prajapati\PycharmProjects\selenium\chromedriver.exe')
        options = webdriver.ChromeOptions()
        options.add_argument("--incognito")
        self.driver=webdriver.Chrome(r'C:\Users\Saurabh prajapati\PycharmProjects\selenium\chromedriver.exe',options=options)

    def parse(self, response):
        self.driver.get(response.url)
        self.driver.switch_to.default_content()
        self.driver.switch_to.frame("tabframe0")
        s(5)
        self.driver.find_element_by_xpath("(//input[@id='fromdate'])[1]").click()
        self.driver.find_element_by_xpath("(//input[@id='fromdate'])[1]").send_keys("06/18/2021")
        self.driver.find_element_by_xpath("(//input[@id='todate'])[1]").click()
        self.driver.find_element_by_xpath("(//input[@id='todate'])[1]").send_keys("06/18/2021")


        self.driver.find_element_by_xpath("//select[@id='availablebooktypes']/option[text()='All']").click()
        self.driver.find_element_by_xpath("//input[@value='matchcontains']").click()
        self.driver.find_element_by_xpath("(//input[@value='1' and @id='resultstyletype'])[1]").click()
        self.driver.find_element_by_xpath("//a[@id='search'][1]").click()
        s(5)
        self.driver.switch_to.default_content()
        self.driver.switch_to.frame("tabframe0")
        # self.driver.find_element_by_xpath("//tr[@id='0']").click()
        # # response = response.replace(body=self.driver.page_source)
        # s(3)
        # self.driver.switch_to.default_content()
        # self.driver.switch_to.frame("tabframe0")
        response = response.replace(body=self.driver.page_source)
        total_rows = response.xpath("(//tbody)[1]//tr[contains(@class,'row')]").getall()
        print(total_rows)
        # print(len(total_rows))
        while True:
            for i in range(0,15):
                self.driver.switch_to.default_content()
                self.driver.switch_to.frame("tabframe0")
                try:
                    self.driver.find_element_by_xpath(f"//tr[@id='{i}']").click()
                except:
                    break
                self.driver.switch_to.default_content()
                self.driver.switch_to.frame("tabframe0")
                s(4)


                response = response.replace(body=self.driver.page_source)
                Date = response.xpath("//span[text()='Date:']/following-sibling::text()").get(default='')
                Doc = response.xpath("//span[text()='Doc #:']/following-sibling::text()").get(default='')
                Kind = response.xpath("//span[text()='Kind:']/following-sibling::text()").get(default='')
                Book = response.xpath("//span[text()='Book:']/following-sibling::text()").get(default='')
                Page = response.xpath("//span[text()='Page:']/following-sibling::text()").get(default='')
                Instrument =""
                for i in range(5):
                    ins=response.xpath(f"(//div[text()='Description']/following-sibling::div){[i]}/text()").get(default='')
                    if ins != "":
                        Instrument=Instrument + " "+ ins
                        Instrument.strip("|")
                Tax = response.xpath("//span[text()='Tax:']/following-sibling::text()").get(default='')
                Grantors = ""
                for i in range(1,8):
                    gns = response.xpath(f"(//span[text()='Grantors']/../following-sibling::div){[i]}/text()").get(default='')
                    if gns != "":
                        Grantors = Grantors  + "|" + gns
                        Grantors = Grantors.strip("|")
                Grantees = ""
                for i in range(1,8):
                    gns = response.xpath(f"(//span[text()='Grantees']/../following-sibling::div){[i]}/text()").get(default='')
                    if gns != "":
                        Grantees = Grantees + "|" + gns
                        Grantees = Grantees.strip("|")
                yield {
                    'Date':Date,
                    "Doc":Doc,
                    "Kind":Kind,
                    "Book":Book,
                    "Page":Page,
                    "Description":Instrument,
                    "Tax":Tax,
                    "Grantors": Grantors,
                    "Grantees": Grantees,
                }

                s(4)

            try:
                self.driver.find_element_by_xpath("(//a[@id='nextpage'])[1]").click()
                response = response.replace(body=self.driver.page_source)

            except:
                break


        s(20)






from scrapy.cmdline import execute
execute('scrapy crawl caldwell -o 06199992021.csv '.split())
