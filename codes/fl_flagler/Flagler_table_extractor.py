import json
import sys
import time
import sqlite3
import re
import os
import csv
import pyodbc
# import math
from selenium.webdriver.support.select import Select

from datetime import datetime
from scrapy.http import HtmlResponse
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions as EC

conn = sqlite3.connect("flagler.db")
cursor = conn.cursor()
options = Options()
path2 = 'fl_flagler/spiders'

options.add_experimental_option('prefs', {
    "download.default_directory": path2,
    "download.prompt_for_download": False,
    "download.directory_upgrade": True,
    "plugins.always_open_pdf_externally": True
}
                                )

class FlaglerTableSpider:
    allowed_domains = []
    start_urls = ['https://www.example.com']
    data = HtmlResponse("")
    job_id = ""
    outname = "D:/OPERATOOL_TOOL_RPC/fl_orange/fl_orange/download/%s/" % job_id + job_id + "_Flagler_Table.csv"

    def __init__(self, job_id):
        self.job_id = job_id
        self.outname = "D:/GENERAL_OUTPUT/FL/fl_flagler/%s/" % self.job_id + self.job_id + '_fl_flagler' + "_Short.csv"
        # if os.path.exists("csvFiles/%s" % job_id):
        #     pass
        # else:
        #     os.mkdir("csvFiles/%s" % job_id)

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
        # self.extract_data()

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

    def extract_data(self, page_num, response,json_data):

        links = response.xpath("//*[@class='result odd'] | //*[@class='even result']  | //*[@class='even result odd'] | //*[@class='result even']")

        for link in links:
            raw_dict = {}
            remarks_dict = {}
            JOBID = self.job_id
            ST_COUNTY = "FL-FLAGLER"
            RECORDING_DATE = link.xpath('./td[8]/text()').get(default='').strip()
            CONTRACT_DATE = ""
            DOCUMENT_NUMBER = link.xpath('./td[13]/text()').get(default='').strip()
            BOOK_NUMBER = link.xpath('./td[11]/text()').get(default='').strip()
            PAGE_NUMBER = link.xpath('./td[12]/text()').get(default='').strip()
            MAINDOCTYPE = link.xpath('./td[9]/text()').get(default='').strip()
            PARTY_1ST = ' | '.join(i.strip() for i in link.xpath('./td[6]/text()').getall()).strip()
            PARY_TYPE_1ST = ""
            PARTY_2ND = ' | '.join(i.strip() for i in link.xpath('./td[7]/text()').getall()).strip()
            PARTY_TYPE_2ND = ""
            PARTY_ADDRESS_1ST = ""
            PARTY_ADDRESS_2ND = ""
            AMOUNT = ""
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
            LEGAL_DESCRIPTION = link.xpath('./td[14]/text()').get(default='').replace("\n"," ").strip()

            LOT = self.find_lot(LEGAL_DESCRIPTION)
            BLOCK = self.find_blk(LEGAL_DESCRIPTION)
            PARCEL_ID = self.find_parc(LEGAL_DESCRIPTION)
            PHASE = self.find_phase(LEGAL_DESCRIPTION)
            UNIT = self.find_unit(LEGAL_DESCRIPTION)
            MARGINAL_REFERENCES = ""
            RETURNEE_NAME = ""
            RETURNEE_ADDRESS = ""
            REMARKS = ""
            rec_date = ""
            doc_deed = ""
            grantor = ""
            grantee = ""
            legal = ""
            Book_Type = link.xpath('./td[10]/text()').get(default='').strip()
            DocLinks = ""
            Comments = ""
            # For Raw Data
            raw_dict["JOBID"] = JOBID
            raw_dict["Direct Name"] = PARTY_1ST
            raw_dict["Reverse Name"] = PARTY_2ND
            raw_dict["Record Date"] = RECORDING_DATE
            raw_dict["Doc Type"] = MAINDOCTYPE
            raw_dict["Book"] = BOOK_NUMBER
            raw_dict["Page"] = PAGE_NUMBER
            raw_dict["Legal Description"] = LEGAL_DESCRIPTION
            raw_dict["Instrument #"] = DOCUMENT_NUMBER
            if doc_deed:
                raw_dict[doc_deed] = TOTAL_TRANSFER_TAX
            else:
                raw_dict["Doc Deed Tax"] = TOTAL_TRANSFER_TAX
            RAW = json.dumps(raw_dict)
            # For Remark Data

            remarks_dict["Book Type"] = Book_Type

            REMARKS = json.dumps(remarks_dict)


            alldata = [JOBID, ST_COUNTY, RECORDING_DATE.split(" ")[0], CONTRACT_DATE, DOCUMENT_NUMBER, BOOK_NUMBER,
                       PAGE_NUMBER,
                       MAINDOCTYPE, PARCEL_ID.replace(" ", ""), PARTY_1ST, PARY_TYPE_1ST, PARTY_2ND, PARTY_TYPE_2ND,
                       PARTY_ADDRESS_1ST,
                       PARTY_ADDRESS_2ND, AMOUNT, UNIT, LOT, BLOCK, SECTION, TOWNSHIP, RANGE, SUBDEVISION, PHASE, TRACT,
                       ACREAGE,
                       PROPERTY_ADDRESS, PROPERTY_STREET_ADDRESS,
                       PROPERTY_UNIT_NO, PROPERTY_CITY, PROPERTY_STATE, PROPERTY_ZIP, PROPERTY_ZIP4, MAP_DETAILS,
                       CITY_TRANSFER_TAX,
                       COUNTY_TRANSFER_TAX, TOTAL_TRANSFER_TAX, ORIGINAL_DOT_RECORDING_DATE,
                       ORIGINAL_DOT_DOCUMENT_NUMBER,
                       ORIGINAL_DOT_BOOK_NUMBER, ORIGINAL_DOT_PAGE_NUMBER, NEW_COUNTY_BLOCK, REMARKS, LEGAL_DESCRIPTION,
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
            if json_data["INO"] != '' or json_data["BP"] != '':
                break

        try:
            cursor.execute(f"UPDATE pageUrlTable_{self.job_id} SET status = ? WHERE page_num = ?", [1, page_num])
            conn.commit()
            cursor.execute(f"SELECT page_num FROM pageUrlTable_{self.job_id} WHERE status = 1")
            rows = cursor.fetchall()
            if len(rows) != 0:
                conn.commit()
        except:
            file_object = open("error_log.txt", "a")
            exc_type, exc_obj, exc_tb = sys.exc_info()
            fname = os.path.split(exc_tb.tb_frame.f_code.co_filename)[1]
            print(exc_type, fname, exc_tb.tb_lineno)
            file_object.write(datetime.now().strftime("%d-%m-%y, %H:%M:%S") + ' | ' + "Error: " + str(
                exc_type) + ' | ' + 'Filename: ' + str(fname) + ' | ' + 'Line No: ' + str(
                exc_tb.tb_lineno) + "\n\n")
            file_object.write("----------------------------------------------------------\n\n")


            # final_data = pd.DataFrame.from_dict(data, orient='columns')
            # final_data.to_csv('Orange.csv', index=False)

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
    rec = wait.until(EC.element_to_be_clickable((By.XPATH, '//*[@id="resultsTable_info"]/b'))).text
    records = int(rec.split()[-1].strip())
    print('records', records)
    time.sleep(7)
    response = HtmlResponse(url='https://www.example.com', body=driver.page_source.encode('utf-8'))

    a = FlaglerTableSpider("123")
    a.extract_data(1, response)

# from scrapy.cmdline import execute
# execute('scrapy crawl hillsborough_table_data'.split())
