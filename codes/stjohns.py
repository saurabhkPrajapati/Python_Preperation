import scrapy
from scrapy import Request
from scrapy.utils.response import open_in_browser
import time
import re
from selenium import webdriver
from selenium.webdriver.common.keys import Keys

class Stjohn(scrapy.Spider):
    name = 'stjohns'
    allowed_domains = []
    start_urls = ["https://apps.stjohnsclerk.com/Landmark/Home/Index",
                  ]

    def __init__(self):
        self.driver=webdriver.Chrome(r'C:\Users\Saurabh prajapati\PycharmProjects\selenium\chromedriver.exe')

    def parse(self, response):
        count = 0
        self.driver.get(response.url)
        self.driver.maximize_window()
        self.driver.implicitly_wait(4)
        self.driver.find_element_by_xpath("""//a[@onclick="LaunchDisclaimerFromMenu('searchCriteriaLegal');"]""").click()
        self.driver.find_element_by_xpath("""(//a[@href="javascript:void(0);"])[1]""").click()
        self.driver.find_element_by_xpath("""(//a[text()="Record Date"])[1]""").click()
        self.driver.find_element_by_xpath("""(//input[@id="beginDate-RecordDate"])[1]""").click()
        self.driver.find_element_by_xpath("""(//input[@id="beginDate-RecordDate"])[1]""").send_keys(Keys.CONTROL, "a", Keys.BACK_SPACE)
        self.driver.find_element_by_xpath("""(//input[@id="beginDate-RecordDate"])[1]""").send_keys("06/16/2021")
        self.driver.find_element_by_xpath("""(//input[@id="endDate-RecordDate"])[1]""").click()
        self.driver.find_element_by_xpath("""(//input[@id="endDate-RecordDate"])[1]""").send_keys(Keys.CONTROL, "a", Keys.BACK_SPACE)
        self.driver.find_element_by_xpath("""(//input[@id="endDate-RecordDate"])[1]""").send_keys("06/16/2021")
        self.driver.find_element_by_xpath("(//select[@id='numberOfRecords-RecordDate'])[1]/option[@value='2000']").click()
        self.driver.find_element_by_xpath("""(//a[@id="submit-RecordDate"])[1]""").click()
        time.sleep(4)
        self.driver.find_element_by_xpath("(//select[@name='resultsTable_length'])[1]/option[@value='-1']").click()
        time.sleep(6)
        self.driver.find_element_by_xpath("(//tr[@class='result odd'])[1]").click()
        while True:

            response = response.replace(body=self.driver.page_source)
            Instrument = response.xpath("""//label[text()=" Instrument #"]/../following-sibling::td/text()[1]""").get(default='')
            Book_page = response.xpath("""//label[text()=" Book/Page"]/../following-sibling::td/text()[1]""").get(default='')
            Record_Date = response.xpath("""//label[text()=" Record Date"]/../following-sibling::td/text()[1]""").get(default='')
            Book_Type = response.xpath("""//label[text()=" Book Type"]/../following-sibling::td/text()[1]""").get(default='')
            Doc_Type = response.xpath("""//label[text()=" Doc Type"]/../following-sibling::td/text()[1]""").get(default='')
            Number_of_Pages = response.xpath("""//label[text()=" Number of Pages"]/../following-sibling::td/text()[1]""").get(default='')
            Direct_Name = ""
            for i in range(6):
                try:
                    add = response.xpath(f"""//label[text()=" Direct Name"]/../following-sibling::td/text()[{i}]""").get(default='')
                    Direct_Name = Direct_Name + "|" + add
                    Direct_Name = Direct_Name.strip().strip("|")
                except:
                    pass
            # Direct_Name= Direct_Name.strip().strip("|").strip().rstrip("|")
            # Direct_Name = response.xpath("""//label[text()=" Direct Name"]/../following-sibling::td/text()""").get()
            # Reverse_Name = response.xpath("""//label[text()=" Reverse Name"]/../following-sibling::td/text()""").get()
            Reverse_Name = ""
            for i in range(6):
                try:
                    add = response.xpath(f"""//label[text()=" Reverse Name"]/../following-sibling::td/text()[{i}]""").get(default='')
                    Reverse_Name = Reverse_Name + "|" + add
                    Reverse_Name = Reverse_Name.strip().strip("|")
                except:
                    pass
            # Reverse_Name = Reverse_Name.strip().strip("|").strip().rstrip("|")
            Indirect_Names = ""
            for i in range(6):
                try:
                    add = response.xpath(
                        f"""//label[text()=" Indirect Names"]/../following-sibling::td/text()[{i}]""").get(default='')
                    Indirect_Names = Indirect_Names + "|" + add
                    Indirect_Names = Indirect_Names.strip().strip("|")
                except:
                    pass

            Number_of_Names = response.xpath("""//label[text()=" Number of Names "]/../following-sibling::td/text()[1]""").get(default='')
            Legal_Description = ""
            for i in range(6):
                try:
                    add = response.xpath(f"""//label[text()=" Legal Description"]/../following-sibling::td/text()[{i}]""").get(default='')
                    Legal_Description = Legal_Description + "|" + add
                    Legal_Description = Legal_Description.strip().strip("|")
                except:
                    pass
            # Legal_Description = response.xpath("""//label[text()=" Legal Description"]/../following-sibling::td/text()[1]""").get(default='')
            Doc_Link = ""
            for i in range(8):
                try:
                    add = response.xpath(
                        f"""//label[text()=" DocLink"]/../following-sibling::td/a[{i}]/text()""").get(default='')
                    Doc_Link= Doc_Link + "|" + add
                    Doc_Link = Doc_Link.strip().strip("|")
                except:
                    pass
            # Doc_Link = response.xpath("""//label[text()=" DocLink"]/../following-sibling::td/text()[1]""").get(default='')
            Comments = response.xpath("""//label[text()=" Comments"]/../following-sibling::td/text()[1]""").get(default='')
            Name = response.xpath("""//label[text()=" Name"]/../following-sibling::td/text()[1]""").get(default='')
            Address1 = response.xpath("""//label[text()=" Address1"]/../following-sibling::td/text()[1]""").get(default='')
            Address2 = response.xpath("""//label[text()=" Address2"]/../following-sibling::td/text()[1]""").get(default='')
            Zip = response.xpath("""//label[text()=" Zip"]/../following-sibling::td/text()[1]""").get(default='')
            Required_for_Indexing = response.xpath("""//label[text()=" Required for Indexing"]/../following-sibling::td/text()[1]""").get(default='')
            Consideration = response.xpath("""//label[text()=" Consideration"]/../following-sibling::td/text()[1]""").get(default='')
            Docs_Legal = response.xpath("""//label[text()=" Doc. Legals"]/../following-sibling::td/text()[1]""").get(default='')

            yield{"Instrument":Instrument.replace('\n',''),
                  "Book Page":Book_page.replace('\n',''),
                  "Record Date":Record_Date.replace('\n',''),
                  "Book Type": Book_Type.replace('\n',''),
                  "Doc Type":Doc_Type.replace('\n',''),
                  "Number of Pages":Number_of_Pages.replace('\n',''),
                  "Direct_Name":Direct_Name.replace('\n',''),
                  "Reverse Name":Reverse_Name.replace('\n',''),
                  "Indirect Names":Indirect_Names.replace('\n',''),
                  "Number of Names":Number_of_Names.replace('\n',''),
                  "Consideration":Consideration.replace('\n',''),
                  "Legal Description":Legal_Description.replace('\n',''),
                  "Doc link":Doc_Link.replace('\n',''),
                  "comments":Comments.replace('\n',''),
                  "Name":Name.replace('\n',''),
                  "Address":Address1.replace('\n',''),
                  "Address2":Address2.replace('\n',''),
                  "Zip":Zip.replace('\n',''),
                  "Required For Indexing":Required_for_Indexing.replace('\n',''),
                  "Docs Legal":Docs_Legal,

            }
            #fg
            # if count > 4:
            #     break
            # else:
            #     pass

            try:
                self.driver.find_element_by_xpath("//a[@id='directNavNext']").click()
                time.sleep(3)
            except:
                break




from scrapy.cmdline import execute
execute('scrapy crawl stjohns  -o FL-STJOHN-06162021.csv'.split())

