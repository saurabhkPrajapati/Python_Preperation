import re
import time

import scrapy
from scrapy.http import HtmlResponse
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By




class Lovingtx(scrapy.Spider):
    name = 'lovingtxspider'

    def start_requests(self):
        urls = "https://lovingtx.countygovernmentrecords.com/LovingTXRecorder/web/"
        yield scrapy.Request(
            url=urls,
            callback=self.parse,
            dont_filter=True,
            method="GET"
        )

    def parse(self, response):
        options = webdriver.ChromeOptions()
        options.add_argument("--window-size=1920,1080")
        # options.add_argument("--headless")
        # options.add_argument("--disable-gpu")
        # options.add_argument("--disable-extensions")
        # options.add_experimental_option("excludeSwitches", ["enable-automation"])
        # options.add_experimental_option("useAutomationExtension", False)
        # options.add_argument("--proxy-server='direct://'")
        # options.add_argument("--proxy-bypass-list=*")
        # options.add_argument("--start-maximized")
        driver = webdriver.Chrome(chrome_options=options, executable_path=r'/chromedriver92/chromedriver.exe')
        driver.get(response.url)
        driver.implicitly_wait(6)
        wd = WebDriverWait(driver, 25)
        wd.until(EC.element_to_be_clickable((By.XPATH, """//input[@value='I Acknowledge']"""))).click()
        wd.until(EC.element_to_be_clickable((By.XPATH, """//input[@value='Public Login']"""))).click()
        wd.until(EC.element_to_be_clickable((By.XPATH, "//input[@id='RecDateIDStart']"))).send_keys(Keys.CONTROL,"a",Keys.BACK_SPACE)
        wd.until(EC.element_to_be_clickable((By.XPATH, "//input[@id='RecDateIDStart']"))).send_keys( "07/28/2021")
        wd.until(EC.element_to_be_clickable((By.XPATH, "//input[@id='RecDateIDEnd']"))).send_keys(Keys.CONTROL,"a",Keys.BACK_SPACE)
        wd.until(EC.element_to_be_clickable((By.XPATH, "//input[@id='RecDateIDEnd']"))).send_keys("07/29/2021")
        wd.until(EC.element_to_be_clickable((By.XPATH, "//select[@id='GrantorIDSearchType']/option[text()=' Advanced Searching ']"))).click()
        wd.until(EC.element_to_be_clickable((By.XPATH, "(//input[@value='Search'])[1]"))).click()
        wd.until(EC.element_to_be_clickable((By.XPATH, "//tr[@class='odd'][1]"))).click()
        # time.sleep(80)
        while True:
            time.sleep(2)
            try:
                Subdivision = driver.find_element_by_xpath( "//span[text()='Subdivision']/following-sibling::span/span").text
            except:
                Subdivision = ""
            try:
                Lot = driver.find_element_by_xpath("//span[text()='Lot']/following-sibling::span/span").text
            except:
                Lot = ""
            try:
                Block1 = driver.find_element_by_xpath("(//span[text()='Block']/following-sibling::span)[1]/span").text
            except:
                Block1 = ""
            try:
                Block2 = driver.find_element_by_xpath("(//span[text()='Block']/following-sibling::span)[2]/span").text
            except:
                Block2 =""
            try:
                Tract1= driver.find_element_by_xpath("(/span[text()='Tract']/following-sibling::span)[1]/span").text
            except:
                Tract1= ""
            try:
                Unit = driver.find_element_by_xpath("//span[text()='Unit']/following-sibling::span/span").text
            except:
                Unit = ""
            try:
                Abstract = driver.find_element_by_xpath("//span[text()='Abstract']/following-sibling::span/span").text
            except:
                Abstract = ""
            try:
                Survey = driver.find_element_by_xpath("//span[text()='Survey']/following-sibling::span/span").text
            except:
                Survey = ""
            try:
                Township = driver.find_element_by_xpath("//span[text()='Township']/following-sibling::span/span").text
            except:
                Township = ""
            try:
                Section = driver.find_element_by_xpath("//span[text()='Section']/following-sibling::span/span").text
            except:
                Section = ""
            try:
                Tract2 = driver.find_element_by_xpath("(//span[text()='Tract']/following-sibling::span)[2]/span").text
            except:
                Tract2 = ""
            try:
                Acres = driver.find_element_by_xpath("//span[text()='Acres']/following-sibling::span/span").text
            except:
                Acres = ""
            try:
                Legal_Remarks = driver.find_element_by_xpath("(//span[text()='Legal Remarks']/following-sibling::span)/span").text
            except:
                Legal_Remarks = ""

            # response = HtmlResponse(url='https://www.example.com', body=driver.page_source.encode('utf-8'))
            response = response.replace(body=driver.page_source)

            time.sleep(2)

            yield{
                "Document Type" :response.xpath("(//div[@id='middle']/h1/following-sibling::text())[1]").get(default='').replace("\xa0",' ').replace("\n",'').replace("\t",'').strip(),
                "Document Number" :response.xpath("//span[text()='Document Number']/following-sibling::span/span/text()").get(default='').replace("\xa0",' '),
                "Recording Date" :response.xpath("//span[text()='Recording Date']/following-sibling::span/span/text()").get(default='').replace("\xa0",' '),
                "Volume" :response.xpath("//span[text()='Volume']/following-sibling::span/span/text()").get(default='').replace("\xa0",' '),
                "Page" :response.xpath("//span[text()='Page']/following-sibling::span/span/text()").get(default='').replace("\xa0",' '),
                "Number of Pages" :response.xpath("//span[text()='Number of  Pages']/following-sibling::span/span/text()").get(default='').replace("\xa0",' '),
                "Recording Fee" :response.xpath("//span[text()='Recording Fee']/following-sibling::span/span/text()").get(default='').replace("\xa0",' '),
                "Mortgage Amount" :response.xpath("//span[text()='Mortgage Amount']/following-sibling::span/span/text()").get(default='').replace("\xa0",' '),
                "Document Date" :response.xpath("//span[text()='Document Date']/following-sibling::span/span/text()").get(default='').replace("\xa0",' '),
                "Return Address Name" :response.xpath("//span[text()='Name']/following-sibling::span/span/text()").get(default='').replace("\xa0",' '),
                "Return Address Address 1" :response.xpath("//span[text()='Address 1']/following-sibling::span/span/text()").get(default='').replace("\xa0",' '),
                "Return Address Address 2" :response.xpath("//span[text()='Address 2']/following-sibling::span/span/text()").get(default='').replace("\xa0",' '),
                "Return Address City" :response.xpath("//span[text()='City']/following-sibling::span/span/text()").get(default='').replace("\xa0",' '),
                "Return Address State" :response.xpath("//span[text()='State']/following-sibling::span/span/text()").get(default='').replace("\xa0",' '),
                "Return Address Zip" :response.xpath("//span[text()='Zip']/following-sibling::span/span/text()").get(default='').replace("\xa0",' '),
                "Return Address Mailback" :response.xpath("//span[text()='Mailback']/following-sibling::span/span/text()").get(default='').replace("\xa0",' '),
                "Return Address Destination" :response.xpath("//span[text()='Destination']/following-sibling::span/span/text()").get(default='').replace("\xa0",' '),
                "Return Address Prsented By" :response.xpath("//span[text()='Presented By']/following-sibling::span/span/text()").get(default='').replace("\xa0",' '),
                "Related Info Volume" :response.xpath("//th[text()='Volume']/../following-sibling::tr/td[1]/span/text()").get(default='').replace("\xa0",' '),
                "Related Info Page" :response.xpath("//th[text()='Page']/../following-sibling::tr/td[2]/span/text()").get(default='').replace("\xa0",' '),
                "Related Info Doc Num" :response.xpath("//th[text()='Doc Num']/../following-sibling::tr/td[3]/span/text()").get(default='').replace("\xa0",' '),

                "Grantor": "|".join(i.strip() for i in response.xpath("//th[text()='Grantor']/../following-sibling::tr/td/span/text()").getall()).strip("|").replace("\xa0",' '),
                "Grantee": "|".join(i.strip() for i in response.xpath("//th[text()='Grantee']/../following-sibling::tr/td/span/text()").getall()).strip("|").replace("\xa0",' '),

                # "Subdivision":response.xpath("//span[text()='Subdivision']/following-sibling::span/span/text()").get(default='').replace("\xa0", ' '),
                # "Lot":response.xpath("//span[text()='Lot']/following-sibling::span/span/text()").get(default='').replace("\xa0", ' '),
                # "Block ":response.xpath("(//span[text()='Block']/following-sibling::span)[1]/span/text()").get(default='').replace("\xa0", ' '),
                # "Tract":response.xpath("(//span[text()='Tract']/following-sibling::span)[1]/span/text()").get(default='').replace("\xa0", ' '),
                # "Unit":response.xpath("//span[text()='Unit']/following-sibling::span/span/text()").get(default='').replace("\xa0", ' '),
                # "Abstract":response.xpath("//span[text()='Abstract']/following-sibling::span/span/text()").get(default='').replace("\xa0", ' '),
                # "Survey":response.xpath("//span[text()='Survey']/following-sibling::span/span/text()").get(default='').replace("\xa0", ' '),
                # "Block":response.xpath("(//span[text()='Block']/following-sibling::span)[2]/span/text()").get(default='').replace("\xa0", ' '),
                # "Township":response.xpath("//span[text()='Township']/following-sibling::span/span/text()").get(default='').replace("\xa0", ' '),
                # "Section": response.xpath("//span[text()='Section']/following-sibling::span/span/text()").get(default='').replace("\xa0", ' '),
                # "Tract ":response.xpath("(//span[text()='Tract']/following-sibling::span)[2]/span/text()").get(default='').replace("\xa0", ' '),
                # "Acres":response.xpath("(//tr/td/span[text()='Acres']/following-sibling::span)/span/text()").get(default='').replace("\xa0", ' '),
                # "Legal Remarks":response.xpath("(//span[text()='Legal Remarks']/following-sibling::span)/span/text()").get(default='').replace("\xa0", ' '),
                "Subdivision": Subdivision,
                "Lot": Lot,
                "Block1": Block1,
                "Tract1": Tract1,
                "Unit": Unit,
                "Abstract": Abstract,
                "Survey":Survey,
                "Block2": Block2,
                "Township": Township,
                "Section": Section,
                "Tract2":Tract2,
                "Acres":Acres,
                "Legal Remarks": Legal_Remarks,

                "Document Remarks Submit Date": response.xpath("//span[text()='Submit Date']/following-sibling::span/span/text()").get(default='').replace("\xa0", ' '),
                "Document Remarks Packager": response.xpath("//span[text()='Packager']/following-sibling::span/span/text()").get(default='').replace("\xa0", ' '),
                "Document Remarks Tracking Number": response.xpath("//span[text()='Tracking Number']/following-sibling::span/span/text()").get(default='').replace("\xa0", ' '),
                "Document Remarks Rejected Reason'r": response.xpath("//span[text()='Rejected Reason']/following-sibling::span/span/text()").get(default='').replace("\xa0", ' '),
                "Related Links": "|".join(i.strip() for i in response.xpath("//tr/td/a[@class='selectable']/span/text()").getall()).strip("|").replace("\xa0",' '),

            }
            time.sleep(2)
            try:
                wd.until(EC.element_to_be_clickable((By.XPATH, '//a[contains(text(),"Next document")]'))).click()
            except:
                break


from scrapy.cmdline import execute
execute('scrapy crawl lovingtxspider -o TX.csv'.split())

