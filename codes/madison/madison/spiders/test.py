import re
import time

import scrapy
from scrapy.http import HtmlResponse
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By




class Macomb(scrapy.Spider):
    name = 'macomb'

    def start_requests(self):
        urls = "https://searchiqs.com/NYMAD/Login.aspx"
        yield scrapy.Request(
            url=urls,
            callback=self.parse,
            dont_filter=True,
            method="GET"
        )

    def parse(self, response):
        options = webdriver.ChromeOptions()
        # options.add_argument("--window-size=1920,1080")
        # options.add_argument("--headless")
        options.add_argument("--disable-gpu")
        options.add_argument("--disable-extensions")
        options.add_experimental_option("excludeSwitches", ["enable-automation"])
        options.add_experimental_option("useAutomationExtension", False)
        options.add_argument("--proxy-server='direct://'")
        options.add_argument("--proxy-bypass-list=*")
        options.add_argument("--start-maximized")
        driver = webdriver.Chrome(chrome_options=options,executable_path=r'C:\Users\Saurabh prajapati\PycharmProjects\selenium\chromedriver92\chromedriver.exe')

        driver.get(response.url)
        driver.implicitly_wait(6)
        wd=WebDriverWait(driver,25)
        wd.until(EC.element_to_be_clickable((By.XPATH,"""//button[contains(@id,"btnGuestLogin")]"""))).click()
        wd.until(EC.element_to_be_clickable((By.XPATH,"//input[@id='ContentPlaceHolder1_txtFromDate']"))).send_keys("07/29/2021")
        wd.until(EC.element_to_be_clickable((By.XPATH,"//input[@tabindex='6']"))).send_keys("07/29/2021")
        wd.until(EC.element_to_be_clickable((By.XPATH,"//input[@id='ContentPlaceHolder1_cmdSearch']"))).click()
        # Total_Records= response.xpath("//span[@id='ContentPlaceHolder1_lblSearchCount']/text()").get(default='').strip().strip("\xa0"),
        text = wd.until(EC.visibility_of_element_located((By.XPATH,"//span[@id='ContentPlaceHolder1_lblSearchCount']"))).text
        total_records = re.search('of\s*(\d*)',text).group(1)
        total_records =int(total_records)
        wd.until(EC.element_to_be_clickable((By.XPATH,"""//input[@id='ContentPlaceHolder1_grdResults_btnView_0']"""))).click()

        i=0
        # count=30
        while i<total_records:
            i+=1
            response = HtmlResponse(url='https://www.example.com', body=driver.page_source.encode('utf-8'))
            time.sleep(5)
            # if response.xpath("//font[contains(text(),'Less Payments:')]"):
            #     Less_Payments=response.xpath("//font[contains(text(),'Less Payments:')]/../following-sibling::font[1]/text()").get(
            #         default='').replace("&nbsp;", ' ').replace('<br>', '').replace("<nobr>", '|').replace("</nobr>", "")
            # if response.xpath("//font[contains(text(),'Where Perfected')]"):
            #     Where_Perfected = response.xpath("//font[contains(text(),'Where Perfected')]/../following-sibling::font[1]/text()").get(
            #         default='').replace("&nbsp;", ' ').replace('<br>', '').replace("<nobr>", '|').replace("</nobr>", "")
            # if response.xpath("//font[contains(text(),'Part. Sat')]"):
            #     Part_Sat = response.xpath("//font[contains(text(),'Part. Sat']/../following-sibling::font[1]/text()").get(
            #         default='').replace("&nbsp;", ' ').replace('<br>', '').replace("<nobr>", '|').replace("</nobr>", "")
            #
            # if response.xpath("//font[contains(text(),'Fully Sat')]"):
            #     Fully_Sat= response.xpath("//font[contains(text(),'Fully Sat']/../following-sibling::font[1]/text()").get(
            #         default='').replace("&nbsp;", ' ').replace('<br>', '').replace("<nobr>", '|').replace("</nobr>", "")


            yield {
                "Case #": response.xpath("//font[contains(text(),'Instr')]/../following-sibling::font[1]/text()").get(default='').strip().replace("\xa0",' '),
                "Instr #": response.xpath("//font[contains(text(),'Case')]/../following-sibling::font[1]/text()").get(default='').strip().replace("\xa0",' '),
                "Court": response.xpath("//font[contains(text(),'Court')]/../following-sibling::font[1]/text()").get(default='').strip().replace("\xa0",' '),
                "Rec Date": response.xpath("//font[contains(text(),'Rec')]/../following-sibling::font[1]/text()").get(default='').strip().replace("\xa0",' '),
                "Doc Grp/Desc": response.xpath("//font[contains(text(),'Doc')]/../following-sibling::font[1]/text()").get(default='').strip().replace("\xa0",' '),
                "OR PARTY": response.xpath("//font[contains(text(),'OR ')]/../following-sibling::font[1]").get(default='').replace("&nbsp;",' ').replace('<br>','').replace("<nobr>",'|').replace("</nobr>","").replace("\xa0",' ').replace('<font size="2">','').replace('</font>','').strip("|"),
                # "OR PARTY": "|".join(i.strip() for i in response.xpath("//font[contains(text(),'OR ')]/../following-sibling::font[1]/nobr/text()").getall()).strip("|").replace("\xa0",' '),
                "EE PARTY": response.xpath("//font[contains(text(),'EE ')]/../following-sibling::font[1]").get(default='').replace("&nbsp;",' ').replace('<br>','').replace("<nobr>",'|').replace("</nobr>","").replace("\xa0",' ').replace('<font size="2">','').replace('</font>','').strip("|"),
                # "EE PARTY": "|".join(i.strip() for i in response.xpath("//font[contains(text(),'EE ')]/../following-sibling::font[1]/nobr/text()").getall()).strip("|").replace("\xa0",' '),
                "Owner Name": response.xpath("//font[contains(text(),'Owner ')]/../following-sibling::font[1]").get(default='').replace("&nbsp;",' ').replace('<br>','').replace("<nobr>",'|').replace("</nobr>","").replace("\xa0",' ').replace('<font size="2">','').replace('</font>','').strip("|"),
                "Business Name": response.xpath("//font[contains(text(),'Business Name:')]/../following-sibling::font[1]").get(default='').replace("&nbsp;",' ').replace('<br>','').replace("<nobr>",'|').replace("</nobr>","").replace("\xa0",' ').replace('<font size="2">','').replace('</font>','').strip("|"),
                "Business Type": response.xpath("//font[contains(text(),'Business Type:')]/../following-sibling::font[1]/text()").get(default='').replace("&nbsp;",' ').replace('<br>','').replace("<nobr>",'|').replace("</nobr>","").replace("\xa0",' ').replace('<font size="2">','').replace('</font>','').strip("|"),
                "Plaintiff": response.xpath("//font[contains(text(),'Plaintiff:')]/../following-sibling::font[1]").get(default='').replace("&nbsp;",' ').replace('<br>','').replace("<nobr>",'|').replace("</nobr>","").replace("\xa0",' ').replace('<font size="2">','').replace('</font>','').strip("|"),
                "Defendant": response.xpath("//font[contains(text(),'Defendant:')]/../following-sibling::font[1]").get(default='').replace("&nbsp;",' ').replace('<br>','').replace("<nobr>",'|').replace("</nobr>","").replace("\xa0",' ').replace('<font size="2">','').replace('</font>','').strip("|"),
                "Court Name": response.xpath("//font[contains(text(),'Court Name:')]/../following-sibling::font[1]/text()").get(default='').replace("&nbsp;",' ').replace('<br>','').replace("<nobr>",'|').replace("</nobr>","").replace("\xa0",' ').replace('<font size="2">','').replace('</font>','').strip("|"),
                # "Where Perfected": response.xpath("//font[contains(text(),':')]/../following-sibling::font[1]/text()").get(default='').replace("&nbsp;",' ').replace('<br>','').replace("<nobr>",'|').replace("</nobr>","").replace("\xa0",' '),
                "Perfected Date": response.xpath("//font[contains(text(),'Perfected Date')]/../following-sibling::font[1]/text()").get(default='').replace("&nbsp;",' ').replace('<br>','').replace("<nobr>",'|').replace("</nobr>",""),
                "Part. Sat. Date": response.xpath("//font[contains(text(),'Part. Sat.')]/../following-sibling::font[1]/text()").get(default='').replace("&nbsp;",' ').replace('<br>','').replace("<nobr>",'|').replace("</nobr>",""),
                "Fully. Sat. Date": response.xpath("//font[contains(text(),'Fully. Sat.')]/../following-sibling::font[1]/text()").get(default='').replace("&nbsp;",' ').replace('<br>','').replace("<nobr>",'|').replace("</nobr>",""),
                "Satisfied Status": response.xpath("//font[contains(text(),'Satisfied')]/../following-sibling::font[1]/text()").get(default='').replace("&nbsp;",' ').replace('<br>','').replace("<nobr>",'|').replace("</nobr>",""),
                "Discontinued Date": response.xpath("//font[contains(text(),'Discontinued Date')]/../following-sibling::font[1]/text()").get(default='').replace("&nbsp;",' ').replace('<br>','').replace("<nobr>",'|').replace("</nobr>",""),
                "Destroyed Date": response.xpath("//font[contains(text(),'Destroyed Date:')]/../following-sibling::font[1]/text()").get(default='').replace("&nbsp;",' ').replace('<br>','').replace("<nobr>",'|').replace("</nobr>",""),
                "Amended Date 1": response.xpath("//font[contains(text(),'Amended Date 1:')]/../following-sibling::font[1]/text()").get(default='').replace("&nbsp;",' ').replace('<br>','').replace("<nobr>",'|').replace("</nobr>",""),
                "Amended Date 2": response.xpath("//font[contains(text(),'Amended Date 2:')]/../following-sibling::font[1]/text()").get(default='').replace("&nbsp;",' ').replace('<br>','').replace("<nobr>",'|').replace("</nobr>",""),
                "Less_Payments":"",
                #       response.xpath("//font[contains(text(),'Less Payments:')]/../following-sibling::font[1]/text()").get(
                # default='').replace("&nbsp;", ' ').replace('<br>', '').replace("<nobr>", '|').replace("</nobr>", ""),


                "Case Description": response.xpath("//font[contains(text(),'Case Description')]/../following-sibling::font[1]/text()").get(default='').strip().replace("\xa0",' '),
                "Plaintifff Attorney": response.xpath("//font[contains(text(),'Plaintiff Attor')]/../following-sibling::font[1]/text()").get(default='').strip().replace("\xa0",' '),
                "Property Information": response.xpath("//font[contains(text(),'Property ')]/../following-sibling::font[1]/text()").get(default='').strip().replace("\xa0",' '),
                "Consideration": response.xpath("//font[contains(text(),'Consideration')]/../following-sibling::font[1]/text()").get(default='').strip().replace("\xa0",' '),
                "Description": response.xpath("//font[contains(text(),'Description')]/../following-sibling::font[1]/text()").get(default='').strip().replace("\xa0",' '),
                "Document Date": response.xpath("//font[contains(text(),'Document')]/../following-sibling::font[1]/text()").get(default='').strip().replace("\xa0",' '),
                "Return Name/Address": response.xpath("//font[contains(text(),'Return')]/../following-sibling::font[1]/text()").get(default='').strip().replace("\xa0",' '),
                "Notes": response.xpath("//font[contains(text(),'Notes')]/../following-sibling::font[1]/text()").get(default='').strip().replace( "\xa0", ' '),

                "Related": response.xpath("""//*[@id="ContentPlaceHolder1_lblRelated"]/nobr[1]/a/text()""").get(default='').strip().replace("\xa0",' '),

            }
            wd.until(EC.element_to_be_clickable((By.XPATH,"""//li[@id='mnuSearchResults']"""))).click()
            wd.until(EC.element_to_be_clickable((By.XPATH,f"""//input[@id='ContentPlaceHolder1_grdResults_btnView_{i}']"""))).click()





from scrapy.cmdline import execute
execute('scrapy crawl macomb -o test.csv'.split())
# driver.find_element_by_xpath("""//button[contains(@id,"btnGuestLogin")]""").click()
# driver.find_element_by_xpath("//input[@id='ContentPlaceHolder1_txtFromDate']").send_keys("07/29/2020")
# driver.find_element_by_xpath("//input[@tabindex='6']").send_keys("07/29/2020")
# driver.find_element_by_xpath("//input[@id='ContentPlaceHolder1_cmdSearch']").click()




