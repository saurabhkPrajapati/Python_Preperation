import json
import sys
import time
import sqlite3
import re
import os
import csv
import pyodbc
from selenium.webdriver.support.select import Select
from datetime import datetime
from selenium.webdriver import ActionChains
from scrapy.http import HtmlResponse
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions as EC

conn = sqlite3.connect("flagler.db")
cursor = conn.cursor()

class FlaglerDetailSpider:

    allowed_domains = []
    start_urls = ['https://www.example.com']
    data = HtmlResponse("")
    job_id = ""
    outname = "Flagler_Detail.csv"

    def __init__(self, job_id):
        self.job_id = job_id
        self.outname = "D:/GENERAL_OUTPUT/FL/fl_flagler/%s/" % self.job_id + self.job_id + '_fl_flagler' + "_Full.csv"
        if os.path.exists("csvFiles/%s" % job_id):
            pass
        else:
            os.mkdir("csvFiles/%s" % job_id)

        if os.path.exists(self.outname) == False:
            with open(self.outname, "w", newline="") as wd:
                wr = csv.writer(wd)
                wr.writerow(["JOBID", "ST-COUNTY", "RECORDING DATE", "CONTRACT DATE", "DOCUMENT NUMBER", "BOOK NUMBER",
                             "PAGE NUMBER", "MAINDOCTYPE", "PARCEL ID", "1ST PARTY", "1ST PARY TYPE", "2ND PARTY",
                             "2ND PARTY TYPE", "1ST PARTY ADDRESS", "2ND PARTY ADDRESS", "AMOUNT", "UNIT", "LOT",
                             "BLOCK",
                             "SECTION", "TOWNSHIP", "RANGE", "SUBDEVISION", "PHASE", "TRACT", "ACREAGE",
                             "PROPERTY ADDRESS",
                             "PROPERTY STREET ADDRESS", "PROPERTY UNIT NO", "PROPERTY CITY", "PROPERTY STATE",
                             "PROPERTY ZIP",
                             "PROPERTY ZIP4", "MAP DETAILS", "CITY TRANSFER TAX", "COUNTY TRANSFER TAX",
                             "TOTAL TRANSFER TAX",
                             "ORIGINAL DOT RECORDING DATE", "ORIGINAL DOT DOCUMENT NUMBER", "ORIGINAL DOT BOOK NUMBER",
                             "ORIGINAL DOT PAGE NUMBER", "NEW COUNTY BLOCK", "REMARKS", "LEGAL DESCRIPTION",
                             "MARGINAL REFERENCES", "RETURNEE NAME", "RETURNEE ADDRESS", "RAW"])
            wd.close()

    def find_lot(self, stringdata):
        total = re.match("LT ([0-9]+)", stringdata, flags=re.I)
        if total:
            # print(total)
            num = total.group(1)
        else:
            total = re.match(".+LT ([0-9]+)", stringdata, flags=re.I)
            if total:

                num = total.group(1)
            else:
                num = ""
        num = str(num).replace(",", "")
        if num == "":
            total = re.match("LOT ([0-9]+)", stringdata, flags=re.I)
            if total:
                # print(total)
                num = total.group(1)
            else:
                total = re.match(".+LOT ([0-9]+)", stringdata, flags=re.I)
                if total:

                    num = total.group(1)
                else:
                    num = ""
            num = str(num).replace(",", "")
        return num

    def find_parc(self, stringdata):
        total = re.match(".+Parcel\: ([0-9 ]+)", stringdata, flags=re.I)
        if total:
            num = total.group(1)
        else:
            total = re.match("Parcel\: ([0-9 ]+)", stringdata, flags=re.I)
            if total:
                num = total.group(1)
            else:
                num = ""
        # num = str(num).replace(" ", "")
        return num

    def find_blk(self, stringdata):
        total = re.match(".+BLOCK ([0-9 ]+)", stringdata, flags=re.I)
        if total:
            num = total.group(1)
        else:
            total = re.match("BLOCK ([0-9 ]+)", stringdata, flags=re.I)
            if total:
                num = total.group(1)
            else:
                num = ""
        if num == "":
            total = re.match(".+BLOCK ([0-9 ]+)", stringdata, flags=re.I)
            if total:
                num = total.group(1)
            else:
                total = re.match("BLOCK ([0-9 ]+)", stringdata, flags=re.I)
                if total:
                    num = total.group(1)
                else:
                    num = ""
        return num


    def find_unit(self, stringdata):
        total = re.match(".+UNIT ([0-9A-Z]+)", stringdata, flags=re.I)
        if total:
            num = total.group(1)
        else:
            total = re.match("UNIT ([0-9A-Z]+)", stringdata, flags=re.I)
            if total:
                num = total.group(1)
            else:
                num = ""
        # num = str(num).replace(" ", "")
        return num

    def find_phase(self, stringdata):
        total = re.match(".+PHASE ([0-9A-Z]+)", stringdata, flags=re.I)
        if total:
            num = total.group(1)
        else:
            total = re.match("PHASE ([0-9A-Z]+)", stringdata, flags=re.I)
            if total:
                num = total.group(1)
            else:
                num = ""
        # num = str(num).replace(" ", "")
        return num

# options = Options()
# options.add_argument("--start-maximized")
# driver = webdriver.Chrome(options=options)
# driver.get('https://pubrec6.hillsclerk.com/ORIPublicAccess/')
# driver.find_element_by_id('ORI-Dat').click()
# WebDriverWait(driver, 30).until(EC.element_to_be_clickable((By.ID, 'ORI-Date'))).click()
# time.sleep(3)
# WebDriverWait(driver, 30).until(EC.element_to_be_clickable((By.ID, 'OBKey__1634_1'))).send_keys('07/06/2021')
# time.sleep(3)
# WebDriverWait(driver, 30).until(EC.element_to_be_clickable((By.XPATH, '//button[contains(text(),"Search")]'))).click()
# time.sleep(5)
# element = WebDriverWait(driver, 30).until(EC.element_to_be_clickable((By.XPATH, '//select[@id="pageSize"]')))
# element.location_once_scrolled_into_view
# WebDriverWait(driver, 30).until(EC.element_to_be_clickable((By.XPATH, '//select[@id="pageSize"]/option[last()]'))).click()
# time.sleep(3)
# response = HtmlResponse(url='https://www.example.com', body=driver.page_source.encode('utf-8'))
# total_data = re.findall(r'(\d+) results', response.xpath('/html/body/div/div[2]/div[2]/div/div[2]/table/div[3]/div/text()').getall()[-1])[0]
# total_pages = math.ceil(int(total_data)/500)
# for i in range(1, int(total_pages)+1):
#     links = response.xpath('/html/body/div/div[2]/div[2]/div/div[2]/table/div[2]/table/tbody/tr/td[6]/div/a')
#     for j in range(1, int(len(links))+1):
#         WebDriverWait(driver, 30).until(EC.element_to_be_clickable((By.XPATH, f'/html/body/div/div[2]/div[2]/div/div[2]/table/div[2]/table/tbody/tr[{j}]/td[6]/div/a'))).click()
#         response1 = HtmlResponse(url='https://www.example.com', body=driver.page_source.encode('utf-8'))
#         doc_type = response1.xpath('//div[contains(text(),"Document Type:")]/following-sibling::div/text()').get(default='').strip()
#         rec_date = response1.xpath('//div[contains(text(),"Recording Date:")]/following-sibling::div/text()').get(default='').strip()
#         grantor = '|'.join(i.strip() for i in response1.xpath('//div[contains(text(),"Grantor:")]/following-sibling::div/text()').getall()).replace('●','').replace(',|','|').strip()
#         grantee = '|'.join(i.strip() for i in response1.xpath('//div[contains(text(),"Grantee:")]/following-sibling::div/text()').getall()).replace('●','').replace(',|','|').strip()
#         book = response1.xpath('//div[contains(text(),"Book:")]/following-sibling::div/text()').get(default='').strip()
#         page = response1.xpath('//div[contains(text(),"Page:")]/following-sibling::div/text()').get(default='').strip()
#         legal = response1.xpath('//div[contains(text(),"Legal:")]/following-sibling::div/text()').get(default='').strip()
#         direct_link = response1.xpath('//div[contains(text(),"Direct link:")]/following-sibling::div/a/text()').get(default='').strip()
#         time.sleep(2)
#         WebDriverWait(driver, 30).until(EC.element_to_be_clickable((By.XPATH, '//div[@id="fancyContent"]//button[@title="Close"]'))).click()
#         time.sleep(2)
#     try:WebDriverWait(driver, 30).until(EC.element_to_be_clickable((By.XPATH, '//a[contains(text(),"Next")]'))).click()
#     except:pass

    def data_extractor(self, res_data, url):
        data = []
        response1 = res_data
        raw_dict = {}
        remarks_dict = {}
        JOBID = self.job_id
        ST_COUNTY = "FL-FLAGLER"  #//*[@id="documentInformationParent"]/table/tbody/tr[1]/td[2]
        RECORDING_DATE = response1.xpath(
                    '//label[contains(text(),"Record Date")]/../following-sibling::td/text()').get(default='').strip()
        CONTRACT_DATE = ""
        DOCUMENT_NUMBER = response1.xpath(
                    '//*[contains(text()," Instrument #")]/../following-sibling::td[1]/text()').get(default='').strip()
        BOOK_NUMBER = response1.xpath(
            '//label[contains(text(),"Book")]/../following-sibling::td/text()').get(default='').strip()
        if "/" in BOOK_NUMBER:
            BOOK_NUM = BOOK_NUMBER.split("/")[0]
            BOOK_NUMBER = BOOK_NUM.split(" ")[1]

        PAGE_NUMBER = response1.xpath(
                    '//label[contains(text(),"Page")]/../following-sibling::td/text()').get(default='').strip()
        if "/" in PAGE_NUMBER:
            PAGE_NUMBER = PAGE_NUMBER.split("/")[1]
        MAINDOCTYPE = response1.xpath(
                    '//label[contains(text(),"Doc Type")]/../following-sibling::td/text()').get(default='').strip()
        PARTY_ADDRESS_1ST = ""
        PARTY_ADDRESS_2ND = ""
        AMOUNT = response1.xpath(
                    '//label[contains(text(),"Consideration")]/../following-sibling::td/text()').get(default='').strip()
        SECTION = ""
        TOWNSHIP = ""
        RANGE = ""
        SUBDEVISION = ""
        TRACT = ""
        ACREAGE = ""
        PROPERTY_ADDRESS = ""
        PROPERTY_STREET_ADDRESS = ""
        PROPERTY_UNIT_NO = ""
        PROPERTY_CITY = ""
        PROPERTY_STATE = ""
        PROPERTY_ZIP = ""
        PROPERTY_ZIP4 = ""
        MAP_DETAILS = ""
        CITY_TRANSFER_TAX = ""
        COUNTY_TRANSFER_TAX = ""
        TOTAL_TRANSFER_TAX = ""
        ORIGINAL_DOT_RECORDING_DATE = ""
        ORIGINAL_DOT_DOCUMENT_NUMBER = ""
        ORIGINAL_DOT_BOOK_NUMBER = ""
        ORIGINAL_DOT_PAGE_NUMBER = ""
        NEW_COUNTY_BLOCK = ""
        LEGAL_DESCRIPTION = response1.xpath(
                    '//label[contains(text(),"Legal Description")]/../following-sibling::td/text()').get(default='').strip()

        LOT = ""
        BLOCK = ""
        PARCEL_ID = ""
        UNIT = ""
        PHASE = ""
        MARGINAL_REFERENCES = ""
        RETURNEE_NAME = ""
        RETURNEE_ADDRESS = ""
        PARTY_1ST = '|'.join(i.strip() for i in response1.xpath(
                    '//label[contains(text(),"1st Party")]/../following-sibling::td/text()').getall() if i != '').strip('|').strip()
        PARTY_2ND = '|'.join(i.strip() for i in response1.xpath(
                    '//label[contains(text(),"2nd Party")]/../following-sibling::td/text()').getall() if i != '').strip('|').strip()
        PARY_TYPE_1ST = ""
        PARTY_TYPE_2ND = ""

        # Not in Field List

        NUMBER_PAGES = response1.xpath(
                    '//label[contains(text(),"Number of Pages")]/../following-sibling::td/text()').get(default='').strip()

        NUMBER_NAMES = response1.xpath(
                    '//label[contains(text(),"Number of Names")]/../following-sibling::td/text()').get(default='').strip()

        Book_Type = response1.xpath(
            '//label[contains(text(),"Book Type")]/../following-sibling::td/text()').get(default='').strip()
        Case_Number = response1.xpath(
            '//label[contains(text(),"Case Number")]/../following-sibling::td/text()').get(default='').strip()
        Book_Page = response1.xpath(
            '//label[contains(text(),"Book and Page")]/../following-sibling::td/text()').get(default='').strip()
        Doc_Legals = response1.xpath(
            '//label[contains(text(),"Doc. Legals")]/../following-sibling::td/text()').get(default='').strip()

        # For Remark Data

        remarks_dict["Number of Pages"] = NUMBER_PAGES
        remarks_dict["Number of Names"] = NUMBER_NAMES
        remarks_dict["Book Type"] = Book_Type
        REMARKS = json.dumps(remarks_dict)

        # For Raw Data
        raw_dict["JOBID"] = JOBID
        raw_dict["Instrument #"] = DOCUMENT_NUMBER
        raw_dict["Book/Page"] = BOOK_NUMBER
        raw_dict["Record Date"] = RECORDING_DATE
        raw_dict["Book Type"] = Book_Type
        raw_dict["Doc Type"] = RECORDING_DATE
        raw_dict["Number of Pages"] = NUMBER_PAGES
        raw_dict["Number of Names"] = NUMBER_NAMES
        raw_dict["1st Party"] = PARTY_1ST
        raw_dict["2nd Party"] = PARTY_2ND
        raw_dict["Consideration"] = AMOUNT
        raw_dict["Case Number"] = Case_Number
        raw_dict["Book and Page"] = Book_Page
        raw_dict["Doc. Legals"] = Doc_Legals
        raw_dict["Legal Description"] = LEGAL_DESCRIPTION

        RAW = json.dumps(raw_dict)

        if self.job_id != "" and len(DOCUMENT_NUMBER.strip()) > 0:
            try:
                cursor.execute(f"UPDATE docUrlTable_{self.job_id} SET status = ? WHERE doc_num = ?", [1, url])
                conn.commit()
                cursor.execute(f"SELECT doc_num FROM docUrlTable_{self.job_id} WHERE status = 1")
                rows = cursor.fetchall()
                if len(rows) != 0:
                    conn.commit()
            except:
                pass
            

            alldata = [JOBID, ST_COUNTY, RECORDING_DATE.split(" ")[0], CONTRACT_DATE, DOCUMENT_NUMBER, BOOK_NUMBER,
                       PAGE_NUMBER,
                       MAINDOCTYPE, PARCEL_ID.replace(" ", ""), PARTY_1ST, PARY_TYPE_1ST, PARTY_2ND, PARTY_TYPE_2ND,
                       PARTY_ADDRESS_1ST,
                       PARTY_ADDRESS_2ND, AMOUNT, UNIT, LOT, BLOCK, SECTION, TOWNSHIP, RANGE, SUBDEVISION, PHASE,
                       TRACT,
                       ACREAGE,
                       PROPERTY_ADDRESS, PROPERTY_STREET_ADDRESS,
                       PROPERTY_UNIT_NO, PROPERTY_CITY, PROPERTY_STATE, PROPERTY_ZIP, PROPERTY_ZIP4, MAP_DETAILS,
                       CITY_TRANSFER_TAX,
                       COUNTY_TRANSFER_TAX, TOTAL_TRANSFER_TAX, ORIGINAL_DOT_RECORDING_DATE,
                       ORIGINAL_DOT_DOCUMENT_NUMBER,
                       ORIGINAL_DOT_BOOK_NUMBER, ORIGINAL_DOT_PAGE_NUMBER, NEW_COUNTY_BLOCK, REMARKS,
                       LEGAL_DESCRIPTION,
                       MARGINAL_REFERENCES, RETURNEE_NAME, RETURNEE_ADDRESS, RAW]

            with open(self.outname, "a", newline="") as wd:
                wr = csv.writer(wd)
                print(alldata)
                wr.writerow(alldata)
                wd.close()

            try:
                cnxn = pyodbc.connect(
                    "Driver={SQL Server};Server=51.81.242.172\DESQL;Database=county_search;UID=sa;PWD=ida@#2021;Trusted_Connection=no;")
                mscursor = cnxn.cursor()
                mscursor.execute(f"SELECT recs_processed FROM statusTable WHERE JOBID='{JOBID}'")
                for n in mscursor:
                    n = int(n[0]) + 1
                    mscursor.execute(f"UPDATE statusTable SET recs_processed={n} WHERE JOBID='{JOBID}'")
                    mscursor.commit()
                    mscursor.close()
            except:
                pass

# from scrapy.cmdline import execute
# execute('scrapy crawl hillsborough_detail_data'.split())

if __name__ == "__main__":
    driver = webdriver.Chrome()
    url = "https://apps.flaglerclerk.com/Landmark/"
    driver.get(url)
    wait = WebDriverWait(driver, 10)
    wait.until(
        EC.element_to_be_clickable((By.XPATH, '//*[@id="bodySection"]/div/div/div[3]/div/div[7]/a/img'))).click()
    wait.until(EC.element_to_be_clickable((By.ID, 'idAcceptYes'))).click()

    wait.until(EC.element_to_be_clickable((By.ID, 'beginDate-RecordDate'))).clear()
    time.sleep(1)
    wait.until(EC.element_to_be_clickable((By.ID, 'beginDate-RecordDate'))).send_keys('03/01/2021')
    wait.until(EC.element_to_be_clickable((By.ID, 'endDate-RecordDate'))).clear()
    time.sleep(1)
    wait.until(EC.element_to_be_clickable((By.ID, 'endDate-RecordDate'))).send_keys('03/01/2021')
    select = Select(driver.find_element_by_id('numberOfRecords-RecordDate'))
    select.select_by_value('2000')
    wait.until(EC.element_to_be_clickable((By.ID, 'submit-RecordDate'))).click()
    time.sleep(4)
    # rec = wait.until(EC.element_to_be_clickable((By.XPATH, '//*[@id="resultsTable_info"]/b'))).text
    # records = int(rec.split()[-1].strip())
    # print('records', records)
    #
    first_row = wait.until(EC.element_to_be_clickable((By.XPATH,
                                                       '/html/body/div[6]/div/div/div/div[2]/div/div[3]/div[1]/div/div[3]/table/tbody/tr/td/div/div[8]/table/tbody/tr[1]')))
    actions = ActionChains(driver)
    actions.move_to_element(first_row).click().perform()
    time.sleep(4)
    response1 = HtmlResponse(url='https://www.example.com', body=driver.page_source.encode('utf-8'))

    a = FlaglerDetailSpider("123")
    a.data_extractor(response1, 'https://apps.flaglerclerk.com/Landmark/')
