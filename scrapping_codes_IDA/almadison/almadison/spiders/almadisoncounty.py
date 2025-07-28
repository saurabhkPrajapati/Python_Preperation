import math
import scrapy
from scrapy.http import HtmlResponse
import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC



class Almadison(scrapy.Spider):
    name = 'almadisonspider'
    start_date = '08032021'
    end_date = '08032021'

    def start_requests(self):
        urls = "https://cotthosting.com/almadisonexternal/LandRecords/protected/SrchQuickName.aspx"
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
        # options.add_argument("--disable-gpu")
        # options.add_argument("--disable-extensions")
        # options.add_experimental_option("excludeSwitches",["enable-automation"])
        # options.add_experimental_option("useAutomationExtension", False)
        # options.add_argument("--proxy-server='direct://'")
        # options.add_argument("--proxy-bypass-list=*")
        options.add_argument("--start-maximized")
        driver = webdriver.Chrome(chrome_options=options,executable_path=r'C:\Users\Saurabh prajapati\PycharmProjects\selenium\chromedriver92\chromedriver.exe')
        driver.get(response.url)
        driver.implicitly_wait(6)
        ww = WebDriverWait(driver, 25)
        ww.until(EC.element_to_be_clickable((By.XPATH,"""//input[@value='Acknowledge']"""))).click()
        ww.until(EC.element_to_be_clickable((By.XPATH,"""//input[@value='Date Range']"""))).click()
        ww.until(EC.element_to_be_clickable((By.XPATH,"""//input[@name='ctl00$cphMain$SrchDates1$txtFiledFrom']"""))).send_keys(Keys.CONTROL,"a",Keys.BACK_SPACE)
        ww.until(EC.element_to_be_clickable((By.XPATH,"""//input[@name='ctl00$cphMain$SrchDates1$txtFiledFrom']"""))).send_keys(self.start_date)
        ww.until(EC.element_to_be_clickable((By.XPATH,"""//input[@name='ctl00$cphMain$SrchDates1$txtFiledFrom']/following-sibling::input"""))).send_keys(Keys.CONTROL,"a",Keys.BACK_SPACE)
        ww.until(EC.element_to_be_clickable((By.XPATH,"""//input[@name='ctl00$cphMain$SrchDates1$txtFiledFrom']/following-sibling::input"""))).send_keys(self.end_date)
        time.sleep(3)
        ww.until(EC.element_to_be_clickable((By.XPATH,"""//input[@id='ctl00_cphMain_btnSearch']"""))).click()

        total_records = ww.until(EC.presence_of_element_located((By.XPATH,"""//*[@id="ctl00_cphMain_lrrgResults_cgvResults"]/caption/strong[2]"""))).text
        total_pages = math.ceil(int(total_records)/500)
        total_pages = total_pages + 1
        print(total_pages)
        for j in range(1, total_pages):
            for i in range(0,500):
                time.sleep(3)
                if driver.find_element_by_xpath(f"""(//td/a[@href="javascript:__doPostBack('ctl00$cphMain$lrrgResults$cgvResults','Profile${i}')"])[1]"""):
                    ww.until(EC.element_to_be_clickable((By.XPATH,f"""(//td/a[@href="javascript:__doPostBack('ctl00$cphMain$lrrgResults$cgvResults','Profile${i}')"])[1]"""))).click()
                    time.sleep(6)
                    # response = HtmlResponse(url='https://www.example.com', body=driver.page_source.encode('utf-8'))
                    response = response.replace(body=driver.page_source)
                    if response.xpath("//tr/th[text()='Last Modified On']"):
                        yield{

                            "Instrument": response.xpath("//tr/th[text()='Instrument #']/../following-sibling::tr/td[1]/text()").get(default='').strip().strip("\xa0"),
                            "Last Modified On": response.xpath("//tr/th[text()='Last Modified On']/../following-sibling::tr/td[2]/text()").get(default='').strip().strip("\xa0"),
                            "Book/Pages": response.xpath("//tr/th[text()='Book/Page']/../following-sibling::tr/td[3]/text()").get(default='').strip().strip("\xa0"),
                            "Index Type": response.xpath("//tr/th[text()='Index Type']/../following-sibling::tr/td[4]/text()").get(default='').strip().strip("\xa0"),
                            "Kind": response.xpath("//tr/th[text()='Kind']/../following-sibling::tr/td[5]/text()").get(default='').strip().strip("\xa0"),
                            "Description(Not Warranted)": response.xpath("//tr/th[text()='Description (Not Warranted)']/../following-sibling::tr/td[6]/text()").get(default='').strip().strip("\xa0"),
                            "Date Field": response.xpath("//tr/th[text()='Date Filed']/../following-sibling::tr/td[7]/text()").get(default='').strip().strip("\xa0"),
                            "Instrument Date": response.xpath("//tr/th[text()='Instrument Date']/../following-sibling::tr/td[8]/text()").get(default='').strip().strip("\xa0"),
                            "Images": response.xpath("//tr/th[text()='Images']/../following-sibling::tr/td/a/text()").get(default='').strip().strip("\xa0"),
                            "Consideration Amt": response.xpath("//tr/th[text()='Consideration Amt']/../following-sibling::tr/td[10]/text()").get(default='').strip().strip("\xa0"),

                            "Returned To": response.xpath("//tr/th[text()='Returned To']/../following-sibling::tr/td[1]/text()").get(default='').strip().strip("\xa0"),
                            "Address": response.xpath("//tr/th[text()='Address']/../following-sibling::tr/td[2]/text()").get(default='').strip().strip("\xa0"),
                            "Address(2)": response.xpath("//tr/th[text()='Address (2)']/../following-sibling::tr/td[3]/text()").get(default='').strip().strip("\xa0"),
                            "City": response.xpath("//tr/th[text()='City']/../following-sibling::tr/td[4]/text()").get(default='').strip().strip("\xa0"),
                            "State": response.xpath("//tr/th[text()='State']/../following-sibling::tr/td[5]/text()").get(default='').strip().strip("\xa0"),
                            "ZIP": response.xpath("//tr/th[text()='ZIP']/../following-sibling::tr/td[6]/text()").get(default='').strip().strip("\xa0"),
                            "GRANTORS": "|".join(i.strip() for i in response.xpath("//tr/th[text()='GRANTORS']/../following-sibling::tr/td/text()").getall()).strip("|").strip("\xa0"),
                            "GRANTEES": "|".join(i.strip() for i in response.xpath("//tr/th[text()='GRANTEES']/../following-sibling::tr/td/text()").getall()).strip("|").strip("\xa0"),
                            # "INDEXED NAMES": "|".join(i.strip() for i in response.xpath("//tr/th[text()='INDEXED NAMES']/../following-sibling::tr/td/text()").getall()).strip("|").strip("\xa0"),
                            #  "OTHER NAMES": "|".join(i.strip() for i in response.xpath("//tr/th[text()='OTHER NAMES']/../following-sibling::tr/td/text()").getall()).strip("|").strip("\xa0"),
                             # "Property Information":"|".join(i.strip() for i in response.xpath("//tr/th[text()='Property Information']/../following-sibling::tr/td/text()").getall()).strip("|").strip("\xa0"),
                            "Property Information": "|".join(i.replace("/",'').replace("<td>",'').replace("<b>"," ",).replace("<br>",'|').strip().strip("|") for i in response.xpath("//tr/th[text()='Property Information']/../following-sibling::tr/td").getall()).strip("|").strip("\xa0"),
                             # "Property Information":response.xpath("//tr/th[text()='Property Information']/../following-sibling::tr/td").get(default='').replace("/",'').replace("td",'').replace("<b>"," ",).replace("br",'').replace('<>','').strip("|").strip("\xa0"),
                            "Reference Index": "|".join(i.strip() for i in response.xpath("//tr/th/a[text()='Index']/../../../following-sibling::tbody/tr/td[3]/text()").getall()).strip("|").strip("\xa0"),
                            "Reference Date Filled": "|".join(i.strip() for i in response.xpath("//tr/th/a[text()='Date Filed']/../../../following-sibling::tbody/tr/td[4]/text()").getall()).strip("|").strip("\xa0"),
                            "Reference Instrument Date": "|".join(i.strip() for i in response.xpath("//tr/th/a[text()='Instrument Date']/../../../following-sibling::tbody/tr/td[5]/text()").getall()).strip("|").strip("\xa0"),
                            "Reference Kind": "|".join(i.strip() for i in response.xpath("//tr/th/a[text()='Kind']/../../../following-sibling::tbody/tr/td[6]/text()").getall()).strip("|").strip("\xa0"),
                            "Reference Instrument": "|".join(i.strip() for i in response.xpath("//tr/th/a[text()='Instrument #']/../../../following-sibling::tbody/tr/td[10]/a/text()").getall()).strip("|").strip("\xa0"),
                            "Reference Book/Page": "|".join(i.strip() for i in response.xpath("//tr/th/a[text()='Book/Page']/../../../following-sibling::tbody/tr/td[11]/a/text()").getall()).strip("|").strip("\xa0"),
                            "Ref": "|".join(i.strip() for i in response.xpath("//tr/th[text()='Ref']/../../following-sibling::tbody/tr/td[12]/div/table/tbody/tr/td/text()").getall()).strip("|").strip("\xa0"),
                            "Reference Consideration Amt": "|".join(i.strip() for i in response.xpath("//tr/th/a[text()='Consideration Amt']/../../../following-sibling::tbody/tr/td[13]/text()").getall()).strip("|").strip("\xa0"),
                            "Reference Images": "|".join(i.strip() for i in response.xpath("//tr/th[text()='Images']/../../following-sibling::tbody/tr/td[14]/a/text()").getall()).strip("|").strip("\xa0"),

                        }
                    else:
                        yield {
                            "Instrument": response.xpath("//tr/th[text()='Instrument #']/../following-sibling::tr/td[1]/text()").get(default='').strip().strip("\xa0"),
                            "Last Modified On": response.xpath("//tr/th[text()='Last Modified On']/../following-sibling::tr/td[2]/text()").get(default='').strip().strip("\xa0"),
                            "Book/Pages": response.xpath("//tr/th[text()='Book/Page']/../following-sibling::tr/td[2]/text()").get(default='').strip().strip("\xa0"),
                            "Index Type": response.xpath("//tr/th[text()='Index Type']/../following-sibling::tr/td[3]/text()").get(default='').strip().strip("\xa0"),
                            "Kind": response.xpath("//tr/th[text()='Kind']/../following-sibling::tr/td[4]/text()").get(default='').strip().strip("\xa0"),
                            "Description(Not Warranted)": response.xpath("//tr/th[text()='Description (Not Warranted)']/../following-sibling::tr/td[5]/text()").get(default='').strip().strip("\xa0"),
                            "Date Field": response.xpath("//tr/th[text()='Date Filed']/../following-sibling::tr/td[6]/text()").get(default='').strip().strip("\xa0"),
                            "Instrument Date": response.xpath("//tr/th[text()='Instrument Date']/../following-sibling::tr/td[7]/text()").get(default='').strip().strip("\xa0"),
                            "Images": response.xpath("//tr/th[text()='Images']/../following-sibling::tr/td/a/text()").get(default='').strip().strip("\xa0"),
                            "Consideration Amt": response.xpath("//tr/th[text()='Consideration Amt']/../following-sibling::tr/td[9]/text()").get(default='').strip().strip("\xa0"),

                            "Returned To": response.xpath("//tr/th[text()='Returned To']/../following-sibling::tr/td[1]/text()").get(default='').strip().strip("\xa0"),
                            "Address": response.xpath("//tr/th[text()='Address']/../following-sibling::tr/td[2]/text()").get(default='').strip().strip("\xa0"),
                            "Address(2)": response.xpath("//tr/th[text()='Address (2)']/../following-sibling::tr/td[3]/text()").get(default='').strip().strip("\xa0"),
                            "City": response.xpath("//tr/th[text()='City']/../following-sibling::tr/td[4]/text()").get(default='').strip().strip("\xa0"),
                            "State": response.xpath("//tr/th[text()='State']/../following-sibling::tr/td[5]/text()").get(default='').strip().strip("\xa0"),
                            "ZIP": response.xpath("//tr/th[text()='ZIP']/../following-sibling::tr/td[6]/text()").get(default='').strip().strip("\xa0"),
                            "GRANTORS": "|".join(i.strip() for i in response.xpath("//tr/th[text()='GRANTORS']/../following-sibling::tr/td/text()").getall()).strip("|").strip("\xa0"),
                            "GRANTEES": "|".join(i.strip() for i in response.xpath("//tr/th[text()='GRANTEES']/../following-sibling::tr/td/text()").getall()).strip("|").strip("\xa0"),
                            # "INDEXED NAMES": "|".join(i.strip() for i in response.xpath("//tr/th[text()='INDEXED NAMES']/../following-sibling::tr/td/text()").getall()).strip("|").strip("\xa0"),
                            #  "OTHER NAMES": "|".join(i.strip() for i in response.xpath("//tr/th[text()='OTHER NAMES']/../following-sibling::tr/td/text()").getall()).strip("|").strip("\xa0"),
                             # "Property Information":"|".join(i.strip() for i in response.xpath("//tr/th[text()='Property Information']/../following-sibling::tr/td/text()").getall()).strip("|").strip("\xa0"),
                            "Property Information": "|".join(i.replace("/",'').replace("<td>",'').replace("<b>"," ",).replace("<br>",'|').strip().strip("|") for i in response.xpath("//tr/th[text()='Property Information']/../following-sibling::tr/td").getall()).strip("|").strip("\xa0"),
                             # "Property Information":response.xpath("//tr/th[text()='Property Information']/../following-sibling::tr/td").get(default='').replace("/",'').replace("td",'').replace("<b>"," ",).replace("br",'').replace('<>','').strip("|").strip("\xa0"),
                            "Reference Index": "|".join(i.strip() for i in response.xpath("//tr/th/a[text()='Index']/../../../following-sibling::tbody/tr/td[3]/text()").getall()).strip("|").strip("\xa0"),
                            "Reference Date Filled": "|".join(i.strip() for i in response.xpath("//tr/th/a[text()='Date Filed']/../../../following-sibling::tbody/tr/td[4]/text()").getall()).strip("|").strip("\xa0"),
                            "Reference Instrument Date": "|".join(i.strip() for i in response.xpath("//tr/th/a[text()='Instrument Date']/../../../following-sibling::tbody/tr/td[5]/text()").getall()).strip("|").strip("\xa0"),
                            "Reference Kind": "|".join(i.strip() for i in response.xpath("//tr/th/a[text()='Kind']/../../../following-sibling::tbody/tr/td[6]/text()").getall()).strip("|").strip("\xa0"),
                            "Reference Instrument": "|".join(i.strip() for i in response.xpath("//tr/th/a[text()='Instrument #']/../../../following-sibling::tbody/tr/td[10]/a/text()").getall()).strip("|").strip("\xa0"),
                            "Reference Book/Page": "|".join(i.strip() for i in response.xpath("//tr/th/a[text()='Book/Page']/../../../following-sibling::tbody/tr/td[11]/a/text()").getall()).strip("|").strip("\xa0"),
                            "Ref": "|".join(i.strip() for i in response.xpath("//tr/th[text()='Ref']/../../following-sibling::tbody/tr/td[12]/div/table/tbody/tr/td/text()").getall()).strip("|").strip("\xa0"),
                            "Reference Consideration Amt": "|".join(i.strip() for i in response.xpath("//tr/th/a[text()='Consideration Amt']/../../../following-sibling::tbody/tr/td[13]/text()").getall()).strip("|").strip("\xa0"),
                            "Reference Images": "|".join(i.strip() for i in response.xpath("//tr/th[text()='Images']/../../following-sibling::tbody/tr/td[14]/a/text()").getall()).strip("|").strip("\xa0"),

                        }


                    time.sleep(2)
                    # time.sleep(3)

                    WebDriverWait(driver, 25).until(EC.element_to_be_clickable((By.XPATH,"//input[@value='Return to Previous Page']"))).click()

                    # time.sleep(2)
                    # time.sleep(2)

            WebDriverWait(driver, 25).until(EC.element_to_be_clickable((By.XPATH,f"""(//td/a[@href="javascript:__doPostBack('ctl00$cphMain$lrrgResults$cgvResults','Page${i}')"])[1]"""))).click()
            j = j+1
            try:
                WebDriverWait(driver, 25).until(EC.element_to_be_clickable((By.XPATH, f"""(//td/a[@href="javascript:__doPostBack('ctl00$cphMain$lrrgResults$cgvResults','Page${j}')"])[1]"""))).click()
            except:
                print("Success")

        #     # time.sleep(6)


from scrapy.cmdline import execute
execute('scrapy crawl almadisonspider -o test.csv'.split())

# "Refernce GRANTORS":"|".join(i.strip() for i in response.xpath("//tr/th[text()='GRANTORS']/../../following-sibling::tbody/tr/td[7]/div/table/tbody/tr/td/text()").getall()).strip("|").strip("\xa0"),
# "Refernce GRANTEES":"|".join(i.strip() for i in response.xpath("//tr/th[text()='GRANTEES']/../../following-sibling::tbody/tr/td[8]/div/table/tbody/tr/td/text()").getall()).strip("|").strip("\xa0"),
# "Reference INDEXED NAMES": response.xpath("//tr/th[text()='INDEXED NAMES']/../../following-sibling::tbody/tr/td[7]/div/table/tbody/tr/td/text()").get(default='').strip("\xa0"),
# "Reference  OTHER NAMES": response.xpath("//tr/th[text()='OTHER NAMES']/../../following-sibling::tbody/tr/td[8]/div/table/tbody/tr/td/text()").get(default='').strip("\xa0"),
# "Reference Description(Not Warranted)":"|".join(i.strip() for i in response.xpath("//tr/th[text()='Description (Not Warranted)']/../../following-sibling::tbody/tr/td[9]/div/table/tbody/tr/td/text()").getall()).strip("|").strip("\xa0"),
