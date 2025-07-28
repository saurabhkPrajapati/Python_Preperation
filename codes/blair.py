import scrapy
from scrapy.utils.response import open_in_browser
import time
import re
from selenium import webdriver
from selenium.webdriver.common.keys import Keys

class Blair(scrapy.Spider):
    name = 'Blair'
    allowed_domains = []
    start_urls = ["https://www.landex.com/webstore/jsp/cart/DocumentSearchResults.jsp?LastName=&FirstName=&StartDate=07%2F12%2F2020&EndDate=07%2F20%2F2020&MunicipalityCriteria=%2B.landex.16&InstrumentCriteria=%2B.landex&DisplayItemsPerPage=250&MaximumMatches=250",
                       ]
    count=2
    def __init__(self):
        self.driver=webdriver.Chrome(r'/chromedriver.exe')

    def parse(self, response):
#######scrapy also run before below statement
        self.driver.get(response.url)
        response = response.replace(body=self.driver.page_source)
        total = response.xpath("(//a[@class='info']/@onclick)").getall()

        for i in range(1, (len(total) + 1)):

            iter = str(response.xpath(f"(//a[@class='info']/@onclick)[{i}]").extract())

            test = (re.search('[^\\n](.*)', iter)).group()
            test = str(test)

            try:
                Recorded_Date = (
                    re.search('<STRONG>Recorded Date:<\/STRONG><\/td><td valign=top>(.*\n*, \d{4})',
                              test)).group(1)

            except:
                Recorded_Date = ""
            try:
                Instrument = (re.search('<STRONG>Instrument #:<\/STRONG><\/td><td valign=top>(\d*\n*\d*)<\/td>',
                                        test)).group(1)
            except:
                Instrument = ""
            try:
                Time = (re.search('<br>(\d{0,4}:\d{0,4}:\d{0,4}) PM', test)).group(1)
            except:
                Time = ""

            try:
                Instrument_Type = (re.search(
                    '<STRONG>Instrument Type:<\/STRONG><\/td><td(\n*)(\s*)valign=top>(.*)<\/td><\/tr><tr><td width=150 valign=top class=arial-black-14px-bold><STRONG>County',
                    test)).group(0)
                Instrument_Type = (re.search('valign=top>(.*)<\/td><\/tr><tr>', Instrument_Type)).group(1)
            except:
                Instrument_Type = ""
            try:
                Municipality = (re.search(
                    '<STRONG>Municipality:<\/STRONG><\/td><td\n*\s*valign=top>(.*)<\/td><\/tr><tr><td width=150\n*\s*valign=top class=arial-black-14px-bold><STRONG>Recording Status',
                    test)).group(1)
            except:
                Municipality = ""
            try:
                Recording_Status = (re.search(
                    '<STRONG>Recording Status:<\/STRONG><\/\n*\s*td><td valign=top>(\w*)<\/td><\/tr><\/table>',
                    test)).group(1)
            except:
                Recording_Status = ""
            try:
                DECEASED = (re.search(
                    '<STRONG>DECEASED<\/STRONG><\/td><\/tr><tr><td width=50% valign=top>(.*)<BR><\/td><td valign=top>',
                    test)).group(1)
            except:
                DECEASED = ""
            try:
                Book = (
                    re.search('<STRONG>Book:<\/STRONG><\/td><td valign=top>(.*)<\/td><\/tr><tr><td width=150',
                              test)).group(0)
                Book = (re.search(
                    '<STRONG>Book:<\/STRONG><\/td><td valign=top>(.*)<\/td><\/tr><tr><td width=150\n*\s*valign=top class=arial-black-14px-bold><STRONG>Page',
                    Book)).group(1)
            except:
                Book = ""
            try:
                Page = (re.search(
                    '<STRONG>Page:<\/STRONG><\/td><td valign=top>(.*)<\/td><\/tr><tr><td width=150 valign=top class=arial-black-14px-bold><STRONG>',
                    test)).group(1)
                Page.replace('<BR>', "")
            except:
                Page = ""
            try:
                Total_Pages = (re.search(
                    '<STRONG>Total Pages:<\/STRONG><\/td><td valign=top>(.*)<\/td><\/tr><tr><td width=150 valign=top \n*\s*class=arial-black-14px-bold rowspan=2><STRONG>Parcel',
                    test)).group(1)
            except:
                Total_Pages = ""
            try:
                Parcel_Number = (re.search(
                    '><STRONG>Parcel Numbers:<\/STRONG><\/td><td valign=top rowspan=2>(.*)<\/td><\/tr><\/table><\/td><\/tr><tr><td colspan=2>\n*\s*<table width=100% border=0><tr><td width=150 valign=top class=arial-black-14px-bold><STRONG>Notes',
                    test)).group(1)
            except:
                Parcel_Number = ""

            yield {
                "Instrument": Instrument,
                "Recoded Date": Recorded_Date + "" + Time,
                "County": "Blair",
                "Instrument Type": Instrument_Type,
                "Municipality": Municipality,
                "Recording_Status": Recording_Status,
                "DECEASED": DECEASED,
                "Book": Book,
                "Page": Page,
                "Total Pages": Total_Pages,
                'Parcel Numbers': Parcel_Number,
            }

        time.sleep(4)
        for i in range(2,6):
            try:
                time.sleep(4)
                nextpage = self.driver.find_element_by_xpath(f"(//a[@href='javascript:gotoPage({i})'])[1]")
                time.sleep(6)
                nextpage.click()
                #response conversion should be done after the selenium part  is completed
                response = response.replace(body=self.driver.page_source)
                total = response.xpath("(//a[@class='info']/@onclick)").getall()

                for i in range(1, (len(total) + 1)):

                    iter = str(response.xpath(f"(//a[@class='info']/@onclick)[{i}]").extract())

                    test = (re.search('[^\\n](.*)', iter)).group()
                    test = str(test)

                    try:
                        Recorded_Date = (
                            re.search('<STRONG>Recorded Date:<\/STRONG><\/td><td valign=top>(.*\n*, \d{4})',
                                      test)).group(1)

                    except:
                        Recorded_Date = ""
                    try:
                        Instrument = (re.search('<STRONG>Instrument #:<\/STRONG><\/td><td valign=top>(\d*\n*\d*)<\/td>',
                                                test)).group(1)
                    except:
                        Instrument = ""
                    try:
                        Time = (re.search('<br>(\d{0,4}:\d{0,4}:\d{0,4}) PM', test)).group(1)
                    except:
                        Time = ""

                    try:
                        Instrument_Type = (re.search(
                            '<STRONG>Instrument Type:<\/STRONG><\/td><td(\n*)(\s*)valign=top>(.*)<\/td><\/tr><tr><td width=150 valign=top class=arial-black-14px-bold><STRONG>County',
                            test)).group(0)
                        Instrument_Type = (re.search('valign=top>(.*)<\/td><\/tr><tr>', Instrument_Type)).group(1)
                    except:
                        Instrument_Type = ""
                    try:
                        Municipality = (re.search(
                            '<STRONG>Municipality:<\/STRONG><\/td><td\n*\s*valign=top>(.*)<\/td><\/tr><tr><td width=150\n*\s*valign=top class=arial-black-14px-bold><STRONG>Recording Status',
                            test)).group(1)
                    except:
                        Municipality = ""
                    try:
                        Recording_Status = (re.search(
                            '<STRONG>Recording Status:<\/STRONG><\/\n*\s*td><td valign=top>(\w*)<\/td><\/tr><\/table>',
                            test)).group(1)
                    except:
                        Recording_Status = ""
                    try:
                        DECEASED = (re.search(
                            '<STRONG>DECEASED<\/STRONG><\/td><\/tr><tr><td width=50% valign=top>(.*)<BR><\/td><td valign=top>',
                            test)).group(1)
                    except:
                        DECEASED = ""
                    try:
                        Book = (
                            re.search('<STRONG>Book:<\/STRONG><\/td><td valign=top>(.*)<\/td><\/tr><tr><td width=150',
                                      test)).group(0)
                        Book = (re.search(
                            '<STRONG>Book:<\/STRONG><\/td><td valign=top>(.*)<\/td><\/tr><tr><td width=150\n*\s*valign=top class=arial-black-14px-bold><STRONG>Page',
                            Book)).group(1)
                    except:
                        Book = ""
                    try:
                        Page = (re.search(
                            '<STRONG>Page:<\/STRONG><\/td><td valign=top>(.*)<\/td><\/tr><tr><td width=150 valign=top class=arial-black-14px-bold><STRONG>',
                            test)).group(1)
                    except:
                        Page = ""
                    try:
                        Total_Pages = (re.search(
                            '<STRONG>Total Pages:<\/STRONG><\/td><td valign=top>(.*)<\/td><\/tr><tr><td width=150 valign=top \n*\s*class=arial-black-14px-bold rowspan=2><STRONG>Parcel',
                            test)).group(1)
                    except:
                        Total_Pages = ""
                    try:
                        Parcel_Number = (re.search(
                            '><STRONG>Parcel Numbers:<\/STRONG><\/td><td valign=top rowspan=2>(.*)<\/td><\/tr><\/table><\/td><\/tr><tr><td colspan=2>\n*\s*<table width=100% border=0><tr><td width=150 valign=top class=arial-black-14px-bold><STRONG>Notes',
                            test)).group(1)
                        Parcel_Number=Parcel_Number.replace('<BR>', "")
                    except:
                        Parcel_Number = ""

                    yield {
                           "Instrument": Instrument,
                           "Recoded Date": Recorded_Date + "" + Time,
                           "County": "Blair",
                           "Instrument Type": Instrument_Type,
                           "Municipality": Municipality,
                           "Recording_Status": Recording_Status,
                           "DECEASED": DECEASED,
                           "Book": Book,
                           "Page": Page,
                           "Total Pages": Total_Pages,
                           'Parcel Numbers': Parcel_Number,
                           }





            except:
                pass
       # else:
            # response = response.replace(body=self.driver.page_source)
        # for else not working for this task


