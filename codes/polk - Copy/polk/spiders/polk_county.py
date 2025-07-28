import math
import scrapy
from scrapy.http import HtmlResponse
import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC



class Polk(scrapy.Spider):
    name = 'polk_county'
    start_date = '07292021'
    end_date ='07292021'

    def start_requests(self):
        urls = "https://landrecords.polkcountyiowa.gov/LandRecords/protected/SrchDateRange.aspx"
        yield scrapy.Request(
            url=urls,
            callback=self.parse,
            dont_filter=True,
            method="GET"
        )

    def parse(self, response):
        options = webdriver.ChromeOptions()
        # options.add_argument("--window-size=1920,1080")
        options.add_argument("--headless")
        options.add_argument("--disable-gpu")
        options.add_argument("--disable-extensions")
        options.add_experimental_option("excludeSwitches",["enable-automation"])
        options.add_experimental_option("useAutomationExtension", False)
        options.add_argument("--proxy-server='direct://'")
        options.add_argument("--proxy-bypass-list=*")
        options.add_argument("--start-maximized")
        driver = webdriver.Chrome(chrome_options=options,executable_path=r'C:\Users\Saurabh prajapati\PycharmProjects\selenium\chromedriver92\chromedriver.exe')
        driver.get(response.url)
        driver.implicitly_wait(6)
        # date range
        driver.find_element_by_xpath("//input[contains(@value,'Date Range') and (@id='ctl00_NavMenuIdxRec_btnNav_IdxRec_Date')]").click()
        time.sleep(5)
        #enter start date
        driver.find_element_by_xpath("//input[@onchange='finalizeDate(this)'][1]").click()
        driver.find_element_by_xpath("//input[@onchange='finalizeDate(this)'][1]").send_keys(Keys.CONTROL,"a",Keys.BACK_SPACE)
        driver.find_element_by_xpath("//input[@onchange='finalizeDate(this)'][1]").send_keys(self.start_date)
        #enter end date
        driver.find_element_by_xpath("//input[@onchange='finalizeDate(this)'][2]").click()
        driver.find_element_by_xpath("//input[@onchange='finalizeDate(this)'][2]").send_keys(Keys.CONTROL,"a",Keys.BACK_SPACE)
        driver.find_element_by_xpath("//input[@onchange='finalizeDate(this)'][2]").send_keys(self.end_date)
        driver.find_element_by_xpath("//input[contains(@value,'Search') and (@id='ctl00_cphMain_btnSearch')]").click()
        time.sleep(6)
        total_records = driver.find_element_by_xpath('//*[@id="ctl00_cphMain_lrrgResults_cgvResults"]/caption/strong[2]').text
        total_pages = math.ceil(int(total_records)/500)
        total_pages = total_pages + 1
        print(total_pages)
        for j in range(1,total_pages):
            for i in range(0,500):
                if driver.find_element_by_xpath(f"""//td/a[@href="javascript:__doPostBack('ctl00$cphMain$lrrgResults$cgvResults','Profile${i}')"]"""):
                    # driver.find_element_by_xpath(f"""//td/a[@href="javascript:__doPostBack('ctl00$cphMain$lrrgResults$cgvResults','Profile${i}')"]""").click()
                    File_Number = driver.find_element_by_xpath(f"""//td/a[@href="javascript:__doPostBack('ctl00$cphMain$lrrgResults$cgvResults','Profile${i}')"]""").text
                    WebDriverWait(driver,25).until(EC.element_to_be_clickable((By.XPATH,f"""//td/a[@href="javascript:__doPostBack('ctl00$cphMain$lrrgResults$cgvResults','Profile${i}')"]"""))).click()
                    time.sleep(4)
                    response = HtmlResponse(url='https://www.example.com', body=driver.page_source.encode('utf-8'))
                    yield{
                        "File Number":File_Number,
                        "Book/Pages":response.xpath("//tr/th[text()='Book/Page']/../following-sibling::tr/td[1]/text()").get(default='').strip().strip("\xa0"),
                        "Index Type":response.xpath("//tr/th[text()='Index Type']/../following-sibling::tr/td[2]/text()").get(default='').strip().strip("\xa0"),
                        "Kind":response.xpath("//tr/th[text()='Kind']/../following-sibling::tr/td[3]/text()").get(default='').strip().strip("\xa0"),
                        "Remarks(Not Warranted)":response.xpath("//tr/th[text()='Remarks']/../following-sibling::tr/td[4]/text()").get(default='').strip().strip("\xa0"),
                        "Description": response.xpath("//tr/th[text()='Description']/../following-sibling::tr/td[4]/text()").get(default='').strip().strip("\xa0"),
                        "Date Recorded":response.xpath("//tr/th[text()='Date Recorded']/../following-sibling::tr/td[5]/text()").get(default='').strip().strip("\xa0"),
                        "FileDate":response.xpath("//tr/th[text()='FileDate']/../following-sibling::tr/td[5]/text()").get(default='').strip().strip("\xa0"),
                        "Instrument Date":response.xpath("//tr/th[text()='Instrument Date']/../following-sibling::tr/td[6]/text()").get(default='').strip().strip("\xa0"),
                        "Images":response.xpath("//tr/th[text()='Images']/../following-sibling::tr/td[7]/a/text()").get(default='').strip().strip("\xa0"),
                        "Amount":response.xpath("//tr/th[text()='Amount']/../following-sibling::tr/td[8]/text()").get(default='').strip().strip("\xa0"),

                        "Returned To":response.xpath("//tr/th[text()='Returned To']/../following-sibling::tr/td[1]/text()").get(default='').strip().strip("\xa0"),
                        "Address":response.xpath("//tr/th[text()='Address']/../following-sibling::tr/td[2]/text()").get(default='').strip().strip("\xa0"),
                        "Address(2)":response.xpath("//tr/th[text()='Address (2)']/../following-sibling::tr/td[3]/text()").get(default='').strip().strip("\xa0"),
                        "City":response.xpath("//tr/th[text()='City']/../following-sibling::tr/td[4]/text()").get(default='').strip().strip("\xa0"),
                        "State":response.xpath("//tr/th[text()='State']/../following-sibling::tr/td[5]/text()").get(default='').strip().strip("\xa0"),
                        "ZIP":response.xpath("//tr/th[text()='ZIP']/../following-sibling::tr/td[6]/text()").get(default='').strip().strip("\xa0"),
                        "GRANTORS":"|".join(i.strip() for i in response.xpath("//tr/th[text()='GRANTORS']/../following-sibling::tr/td/text()").getall()).strip("|").strip("\xa0"),
                        "GRANTEES":"|".join(i.strip() for i in response.xpath("//tr/th[text()='GRANTEES']/../following-sibling::tr/td/text()").getall()).strip("|").strip("\xa0"),
                        "INDEXED NAMES":"|".join(i.strip() for i in response.xpath("//tr/th[text()='INDEXED NAMES']/../following-sibling::tr/td/text()").getall()).strip("|").strip("\xa0"),
                        "OTHER NAMES": "|".join(i.strip() for i in response.xpath("//tr/th[text()='OTHER NAMES']/../following-sibling::tr/td/text()").getall()).strip("|").strip("\xa0"),
                        # "Property Information":"|".join(i.strip() for i in response.xpath("//tr/th[text()='Property Information']/../following-sibling::tr/td/text()").getall()).strip("|").strip("\xa0"),
                        "Property Information":"|".join(i.replace("/",'').replace("<td>",'').replace("<b>"," ",).replace("<br>",'|').strip().strip("|") for i in response.xpath("//tr/th[text()='Property Information']/../following-sibling::tr/td").getall()).strip("|").strip("\xa0"),
                        # "Property Information":response.xpath("//tr/th[text()='Property Information']/../following-sibling::tr/td").get(default='').replace("/",'').replace("td",'').replace("<b>"," ",).replace("br",'').replace('<>','').strip("|").strip("\xa0"),
                        "Reference Index":"|".join(i.strip() for i in response.xpath("//tr/th/a[text()='Index']/../../../following-sibling::tbody/tr/td[3]/text()").getall()).strip("|").strip("\xa0"),
                        "Refernce Date Recorded":"|".join(i.strip() for i in response.xpath("//tr/th/a[text()='Date Recorded']/../../../following-sibling::tbody/tr/td[4]/text()").getall()).strip("|").strip("\xa0"),
                        "Reference Instrument Date": "|".join(i.strip() for i in response.xpath("//tr/th/a[text()='Instrument Date']/../../../following-sibling::tbody/tr/td[5]/text()").getall()).strip("|").strip("\xa0"),
                        "Referncce Kind":"|".join(i.strip() for i in response.xpath("//tr/th/a[text()='Kind']/../../../following-sibling::tbody/tr/td[6]/text()").getall()).strip("|").strip("\xa0"),
                        # "Reference INDEXED NAMES": response.xpath("//tr/th[text()='INDEXED NAMES']/../../following-sibling::tbody/tr/td[7]/div/table/tbody/tr/td/text()").get(default='').strip("\xa0"),
                        # "Reference  OTHER NAMES": response.xpath("//tr/th[text()='OTHER NAMES']/../../following-sibling::tbody/tr/td[8]/div/table/tbody/tr/td/text()").get(default='').strip("\xa0"),
                        # "Reference Remarks(Not Warranted)":"|".join(i.strip() for i in response.xpath("//tr/th[text()='Remarks']/../../following-sibling::tbody/tr/td[9]/div/table/tbody/tr/td/text()").getall()).strip("|").strip("\xa0"),
                        "Reference File Number":"|".join(i.strip() for i in response.xpath("//tr/th/a[text()='File Number']/../../../following-sibling::tbody/tr/td[10]/a/text()").getall()).strip("|").strip("\xa0"),
                        "Reference Book/Page": "|".join(i.strip() for i in response.xpath("//tr/th/a[text()='Book/Page']/../../../following-sibling::tbody/tr/td[11]/a/text()").getall()).strip("|").strip("\xa0"),
                        "Ref": "|".join(i.strip() for i in response.xpath("//tr/th[text()='Ref']/../../following-sibling::tbody/tr/td[12]/div/table/tbody/tr/td/text()").getall()).strip("|").strip("\xa0"),
                        # "Ref":'',
                        "Reference Amount": "|".join(i.strip() for i in response.xpath("//tr/th/a[text()='Amount']/../../../following-sibling::tbody/tr/td[13]/text()").getall()).strip("|").strip("\xa0"),
                        "Reference Images": "|".join(i.strip() for i in response.xpath("//tr/th[text()='Images']/../../following-sibling::tbody/tr/td[14]/a/text()").getall()).strip("|").strip("\xa0"),

                    }

                    # driver.find_element_by_xpath("//input[@value='Retun to Previous Page']").click()
                    WebDriverWait(driver,25).until(EC.element_to_be_clickable((By.XPATH,"//input[@value='Return to Previous Page']"))).click()

                    # time.sleep(4)

            # driver.find_element_by_xpath(f"""(//td/a[@href="javascript:__doPostBack('ctl00$cphMain$lrrgResults$cgvResults','Page${i}')"])[1]""").click()
            j=j+1
            try:
                WebDriverWait(driver, 25).until(EC.element_to_be_clickable((By.XPATH, f"""(//td/a[@href="javascript:__doPostBack('ctl00$cphMain$lrrgResults$cgvResults','Page${j}')"])[1]"""))).click()
            except:
                print("Success")

            # time.sleep(6)


from scrapy.cmdline import execute
execute('scrapy crawl polk_county -o FL-POLK-07322021.csv'.split())
# # execute('scrapy crawl peoria -o ex.csv'.split())
#
#
#
#
# import scrapy
# from scrapy.http import headers
# from scrapy.utils.response import open_in_browser
# import re
#
#
# class Polk(scrapy.Spider):
#     name = 'polk_county'
#     headers = {'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9', 'accept-encoding': 'gzip, deflate, br',
#                'accept-language': 'en-US,en;q=0.9', 'cache-control': 'max-age=0', 'content-type': 'application/x-www-form-urlencoded',
#                'origin': 'https://landrecords.polkcountyiowa.gov', 'referer': 'https://landrecords.polkcountyiowa.gov/LandRecords/protected/SrchDateRange.aspx',
#                'sec-ch-ua': '"Chromium";v="92", " Not A;Brand";v="99", "Google Chrome";v="92"',
#                'sec-ch-ua-mobile': '?0', 'sec-fetch-dest': 'document', 'sec-fetch-mode': 'navigate', 'sec-fetch-site': 'same-origin', 'sec-fetch-user': '?1', 'upgrade-insecure-requests': '1',
#                'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/92.0.4515.107 Safari/537.36'
#                }
#     start_date='07/20/2021'
#     end_date='07/20/2021'
#
#
#     def start_requests(self):
#         urls = "https://landrecords.polkcountyiowa.gov/LandRecords/protected/SrchQuickName.aspx"
#
#         yield scrapy.Request(
#             url=urls,
#             callback=self.parse1,
#             headers=self.headers,
#             dont_filter=True,
#             method="GET"
#         )
#
#     def parse1(self, response):
#         open_in_browser(response)
#         viewstate = response.xpath("//input[@id='ctl00_smScriptMan_HiddenField']/@value").get()
#
#         data= {
#                 'ctl00_smScriptMan_HiddenField': viewstate ,
#                 # 'ctl00_smScriptMan_HiddenField': ';;AjaxControlToolkit, Version=4.1.7.123, Culture=neutral, PublicKeyToken=28f01b0e84b6d53e:en-US:44981e4a-f654-4c69-b806-cb922fc13d56:de1feab2:f9cec9bc:35576c48:fcf0e993:f2c8e708:720a52bf:589eaa30:698129cf:fb9b4c57:ccb96cf9:987bb99b:a4b66312:a67c2700:59fb9c6f:934b0945:8613aea7:3202a5a2:ab09e3fe:87104b7c:be6fb298',
#                 '__SCROLLPOSITIONX': '0',
#                 '__SCROLLPOSITIONY': '0',
#                 'ctl00$cphMain$SrchDates1$txtFiledFrom': self.start_date,
#                 'ctl00$cphMain$SrchDates1$txtFiledThru': self.end_date,
#                 'ctl00$cphMain$btnSearch': 'Search'
#         }
#         yield scrapy.FormRequest(
#             url="https://landrecords.polkcountyiowa.gov/LandRecords/protected/SrchDateRange.aspx",
#             callback=self.parse2,
#             formdata=data,
#             dont_filter=True,
#             method="POST",
#             headers=self.headers,
#             meta={'handle_httpstatus_list': [200]}
#         )
#     def parse2(self, response):
#         open_in_browser(response)
#         print(response.xpath('//*[@id="ctl00_cphMain_lrrgResults_cgvResults"]/tbody/tr[2]/td[6]/text()').get(default=''))
# 167,,,,in mobile