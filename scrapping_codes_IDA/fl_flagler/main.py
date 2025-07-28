from argparser import argparse1
import json
from datetime import datetime
import sys, os, time
from subprocess import Popen, list2cmdline
from fake_useragent import UserAgent
from scrapy.http import HtmlResponse
from selenium.webdriver.chrome.options import Options
from concurrent.futures import ProcessPoolExecutor, wait
from ProxyBot import get_chromedriver
import signal, psutil, shutil
import sqlite3
from selenium.webdriver.common.keys import Keys
from flagler_detail_extractor import FlaglerDetailSpider
from selenium.webdriver.support.ui import Select
from Flagler_table_extractor import FlaglerTableSpider
import pyodbc
import pandas_practice as pd
import glob
import sqlalchemy
import urllib.parse
from selenium.webdriver.support.ui import WebDriverWait

# seconds


commands = []
conn = sqlite3.connect("flagler.db")
cursor = conn.cursor()
executor = ProcessPoolExecutor(max_workers=1)

now = datetime.now()
parser = argparse1.ArgumentParser()
parser.add_argument('--type', action="store", dest='type',
                    help='Download type ("--type S" for short or "--type F" for Full)', default="F")
parser.add_argument('--doc', action="store", dest='doc',
                    help='Download documents "--doc Y" or not "--doc N"', default="Y")
parser.add_argument('--config', action="store", dest='config',
                    help='Path of config or format file "--config file_path"', default="config.json")
parser.add_argument('--no', action="store", dest='no',
                    help='Document Number by "--no number"', default=datetime.now().strftime("%d%m%y%H%M%S"))
results = parser.parse_args()
job_id = results.no
doc_type = results.doc
json_data = json.loads(open(results.config, "r").read())
error_json = json.loads(open("../error_json.json", "r").read())
full_log = ""
screenshot_path = "screenshot/"


def cpu_count():
    ''' Returns the number of CPUs in the system
    '''
    num = 1
    if sys.platform == 'win32':
        try:
            num = int(os.environ['NUMBER_OF_PROCESSORS'])
        except Exception as e:
            error_log(e)
    elif sys.platform == 'darwin':
        try:
            num = int(os.popen('sysctl -n hw.ncpu').read())
        except Exception as e:
            error_log(e)
    else:
        try:
            num = os.sysconf('SC_NPROCESSORS_ONLN')
        except Exception as e:
            error_log(e)

    return num


def sqlcommad(command, values):
    # mycursor = mydb.cursor()
    sql = command
    val = values
    # mycursor.execute(sql, val)
    # mydb.commit()
    print(sql, val)
    if len(val) > 0:
        print("Hello test")
        try:
            cnxn = pyodbc.connect(
                "Driver={SQL Server};Server=51.81.242.172\DESQL;Database=county_search;UID=sa;PWD=ida@#2021;Trusted_Connection=no;")
            mscursor = cnxn.cursor()
            mscursor.execute(sql, val)
            mscursor.commit()
            mscursor.close()
        except Exception as e:
            error_log(e)
            pass
    else:
        print("Hello test")
        try:
            cnxn = pyodbc.connect(
                "Driver={SQL Server};Server=51.81.242.172\DESQL;Database=county_search;UID=sa;PWD=ida@#2021;Trusted_Connection=no;")
            mscursor = cnxn.cursor()
            mscursor.execute(sql)
            mscursor.commit()
            mscursor.close()
        except Exception as e:
            error_log(e)
            pass


def full_log_func(log):
    global full_log
    if full_log != "":
        full_log = full_log + "|" + log
    else:
        full_log = full_log + log + "|"
    return full_log


def update_log(f_log):
    f = full_log_func(f_log)
    try:
        sqlcommad("UPDATE statusTable SET Current_Log = ?, Full_Log = ? WHERE JOBID = ?", (f_log, f, job_id))
    except:
        pass


def exec_commands(cmds):
    ''' Exec commands in parallel in multiple process
    (as much as we have CPU)
    '''
    if not cmds: return  # empty list

    def done(p):
        return p.poll() is not None

    def success(p):
        return p.returncode == 0

    def fail():
        sys.exit(1)

    max_task = cpu_count()
    # max_task = 2
    processes = []
    while True:
        while cmds and len(processes) < max_task:
            task = cmds.pop()
            print(list2cmdline(task))

            processes.append(Popen(task))

        for p in processes:
            if done(p):
                if success(p):
                    processes.remove(p)
                else:
                    fail()

        if not processes and not cmds:
            break
        else:
            time.sleep(0.05)


def kill_child_processes(parent_pid, sig=signal.SIGTERM):
    try:
        parent = psutil.Process(parent_pid)
    except psutil.NoSuchProcess:
        return
    children = parent.children(recursive=True)
    for process in children:
        process.send_signal(sig)


def takeScreenShot(driver,snap_name=""):
    screenshot_path = "D:/GENERAL_OUTPUT/FL/fl_flagler/%s/" % job_id
    if snap_name == "":
        filename = "error_" + datetime.now().strftime("%d%m%y%H%M%S") + ".png"
    else:
        filename = snap_name
    path = screenshot_path + filename
    original_size = driver.get_window_size()
    required_width = driver.execute_script('return document.body.parentNode.scrollWidth')
    required_height = driver.execute_script('return document.body.parentNode.scrollHeight')
    driver.set_window_size(required_width, required_height)
    # driver.save_screenshot(path)  # has scrollbar
    driver.find_element_by_tag_name('body').screenshot(path)  # avoids scrollbar
    driver.set_window_size(original_size['width'], original_size['height'])
    driver.maximize_window()
    return path


def log_terminate():
    # a.cursor.execute(
    #     "UPDATE statusTable SET Current_Log = ?,Status = ? WHERE JOBID = ?",
    #     [len(rows), 3, job_id])
    # conn.commit()
    update_log("Critical Failure")
    sqlcommad("UPDATE statusTable SET Status = ? WHERE JOBID = ?", (3, job_id))
    file_object = open("error_log.txt", "a")
    msg = datetime.now().strftime("%d-%m-%y, %H:%M:%S") + ' | ' + "Error: " + "Program Terminated" + "\n\n"
    file_object.write(msg)
    file_object.write("----------------------------------------------------------\n\n")
    sqlcommad("INSERT INTO Table_Error VALUES(?,?,?,?)", (job_id, "401", "", msg))


def error_log(e, driver=None):
    file_object = open("error_log.txt", "a")
    exc_type, exc_obj, exc_tb = sys.exc_info()
    fname = os.path.split(exc_tb.tb_frame.f_code.co_filename)[1]
    print(exc_type, fname, exc_tb.tb_lineno)
    msg = datetime.now().strftime("%d-%m-%y, %H:%M:%S") + ' | ' + "Error: " + str(
        exc_type) + ' | ' + 'Filename: ' + str(fname) + ' | ' + 'Line No: ' + str(
        exc_tb.tb_lineno) + ' | ' + str(e) + "\n\n"
    file_object.write(msg)
    file_object.write("----------------------------------------------------------\n\n")
    sc_path = ""
    error_code = ""
    if driver != None:
        sc_path = takeScreenShot(driver)
    if "FileNotFoundError" in str(exc_type):
        update_log(error_json["202"])
        error_code = "202"
    elif "NoSuchElementException" in str(exc_type):
        update_log(error_json["101"])
        error_code = "101"
    elif "EmptyDataError" in str(exc_type):
        update_log(error_json["201"])
        error_code = "201"
    elif "IntegrityError" in str(exc_type):
        update_log(error_json["501"])
        error_code = "501"
    elif "NoSuchWindowException" in str(exc_type):
        update_log(error_json["501"])
        error_code = "501"
    elif "WebDriverException" in str(exc_type):
        update_log(error_json["103"])
        error_code = "103"
    elif "Program Terminated" in str(exc_type):
        update_log(error_json["401"])
        error_code = "401"
    else:
        update_log("Unknown Error")
        error_code = "601"
    sqlcommad("INSERT INTO Table_Error_Log VALUES(?,?,?,?)", (job_id, error_code, sc_path, msg))


def file_rename(file_name):
    download_path = "D:/GENERAL_OUTPUT/FL/fl_flagler/%s/" % job_id
    filename = max([download_path + "\\" + f for f in os.listdir(download_path)], key=os.path.getctime)
    # os.rename(filename, os.path.join(download_path, f"{file_name}"))
    shutil.move(filename, os.path.join(download_path, f"{file_name}"))


def details_data_extractor(json_data, url, doc):
    newdriver = get_chromedriver(use_proxy=True, ji=job_id)
    newdriver.maximize_window()
    newdriver.implicitly_wait(50)
    newdriver.get("https://apps.flaglerclerk.com/Landmark/")
    newdriver.find_element_by_xpath('//*[@id="bodySection"]/div/div/div[3]/div/div[1]/a/img').click()
    newdriver.find_element_by_id('idAcceptYes').click()
    update_log("Logged In")
    if json_data["NAME"] != "":
        parcelclick = newdriver.find_element_by_xpath('//*[@id="searchCriteriaName-tab"]')
        if parcelclick != "":
            parcelclick.click()
        try:
            newdriver.find_element_by_xpath('//*[@id="matchType-Name"]/option[2]').click()
            time.sleep(1)
            newdriver.find_element_by_id("name-Name").send_keys(json_data["NAME"])
            time.sleep(2)
            newdriver.find_element_by_id("submit-Name").click()
        except Exception as e:
            error_log(e,newdriver)

    elif json_data["APN"] != "":
        parcelclick = newdriver.find_element_by_xpath('//*[@id="searchCriteriaParcelId-tab"]')
        if parcelclick != "":
            parcelclick.click()

        try:
            time.sleep(1)
            newdriver.find_element_by_xpath('//*[@id="matchType-ParcelId"]/option[2]').click()
            newdriver.find_element_by_id("parcelId").send_keys(json_data["APN"])
            time.sleep(2)
            newdriver.find_element_by_id("submit-ParcelId").click()
        except Exception as e:
            error_log(e,newdriver)

    elif json_data["DOCTYPE"] != "":
        parcelclick = newdriver.find_element_by_xpath('//*[@id="searchCriteriaDocuments-tab"]')
        if parcelclick != "":
            parcelclick.click()
        try:
            newdriver.find_element_by_id("documentType-DocumentType").send_keys(json_data["DOCTYPE"])
            time.sleep(2)
            newdriver.find_element_by_id("submit-DocumentType").click()
        except Exception as e:
            error_log(e,newdriver)

    elif json_data["BP"] != "":
        parcelclick = newdriver.find_element_by_xpath('//*[@id="searchCriteriaBookPage-tab"]')
        if parcelclick != "":
            parcelclick.click()
        bp = json_data["BP"].split("/")
        try:
            newdriver.find_element_by_id("book").send_keys(bp[0])
            newdriver.find_element_by_id("page").send_keys(bp[1])
            time.sleep(2)
            newdriver.find_element_by_id("submit-BookPage").click()
        except Exception as e:
            error_log(e,newdriver)

    elif json_data["CASE"] != "":
        parcelclick = newdriver.find_element_by_xpath('//*[@id="searchCriteriaCaseNumber-tab"]')
        if parcelclick != "":
            parcelclick.click()
        try:
            newdriver.find_element_by_id("caseNumber").send_keys(json_data["CASE"])
            time.sleep(2)
            newdriver.find_element_by_id("submit-CaseNumber").click()
        except Exception as e:
            error_log(e,newdriver)

    elif json_data["RSDATE"] != "":
        parcelclick = newdriver.find_element_by_xpath('//*[@id="searchCriteriaRecordDate-tab"]')
        if parcelclick != "":
            parcelclick.click()
        try:
            newdriver.find_element_by_id("beginDate-RecordDate").send_keys(Keys.CONTROL + 'a')
            newdriver.find_element_by_id("beginDate-RecordDate").send_keys(Keys.BACKSPACE)
            newdriver.find_element_by_id("endDate-RecordDate").send_keys(Keys.CONTROL + 'a')
            newdriver.find_element_by_id("endDate-RecordDate").send_keys(Keys.BACKSPACE)
            newdriver.find_element_by_id("beginDate-RecordDate").send_keys(json_data["RSDATE"])
            if json_data["REDATE"] != "":
                newdriver.find_element_by_id("endDate-RecordDate").send_keys(json_data["REDATE"])
            else:
                newdriver.find_element_by_id("endDate-RecordDate").send_keys(json_data["RSDATE"])
            time.sleep(2)
            newdriver.find_element_by_id("submit-RecordDate").click()
        except Exception as e:
            error_log(e,newdriver)

    elif json_data["INO"] != "":
        parcelclick = newdriver.find_element_by_xpath('//*[@id="searchCriteriaInstrumentNumber-tab"]')
        if parcelclick != "":
            parcelclick.click()
        try:
            newdriver.find_element_by_id("instrumentNumber").send_keys(json_data["INO"])
            time.sleep(2)
            newdriver.find_element_by_id("submit-InstrumentNumber").click()
        except Exception as e:
            error_log(e,newdriver)

    elif json_data["LEGAL"] != "":
        parcelclick = newdriver.find_element_by_xpath('//*[@id="searchCriteriaLegal-tab"]')
        if parcelclick != "":
            parcelclick.click()
        try:
            newdriver.find_element_by_id("legal").send_keys(json_data["LEGAL"])
            time.sleep(2)
            newdriver.find_element_by_id("submit-Legal").click()
        except Exception as e:
            error_log(e,newdriver)

    select = Select(newdriver.find_element_by_name("resultsTable_length"))
    try:
        select.select_by_value('-1')
    except Exception as e:
        error_log(e,newdriver)

    time.sleep(6)

    # row = newdriver.find_element_by_xpath(f"//*[@id='resultsTable']/tbody/tr[{url}]")
    # try:
    #     row.click()
    # except Exception as e:
    #     error_log(e)
    #     newdriver.execute_script("arguments[0].click();", row)
    # except Exception as e:
    #     error_log(e)
    #     WebDriverWait(driver, 20).until(EC.invisibility_of_element((By.XPATH, f"//*[@id='resultsTable']/tbody/tr[{url}]")))
    #     WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.XPATH, f"//*[@id='resultsTable']/tbody/tr[{url}]"))).click()
    # time.sleep(4)

    element = newdriver.find_element_by_xpath(f"//*[@id='resultsTable']/tbody/tr[{url}]")
    desired_y = (element.size['height'] / 2) + element.location['y']
    window_h = newdriver.execute_script('return window.innerHeight')
    window_y = newdriver.execute_script('return window.pageYOffset')
    current_y = (window_h / 2) + window_y
    scroll_y_by = desired_y - current_y
    newdriver.execute_script("window.scrollBy(0, arguments[0]);", scroll_y_by)
    time.sleep(1)
    newdriver.find_element_by_xpath(f'//table[@id="resultsTable"]/tbody/tr[{url}]').click()
    # WebDriverWait(newdriver, 200).until(EC.element_to_be_clickable(
    #     (By.XPATH, f'//table[@id="resultsTable"]//tbody/tr[{url}]'))).click()
    time.sleep(10)
    response1 = HtmlResponse(url='https://www.example.com', body=newdriver.page_source.encode('utf-8'))
    a = FlaglerDetailSpider(job_id)
    a.data_extractor(response1, url)
    update_log("Detailed Data Extraction Completed")
    DOCUMENT_NUMBER = response1.xpath(
        '//*[contains(text()," Instrument #")]/../following-sibling::td[1]/text()').get(default='').strip()

    time.sleep(5)
    if doc == "Y":
        update_log("Downloading Documents")
        newdriver.find_element_by_tag_name("body").send_keys(Keys.PAGE_UP)
        time.sleep(1)
        newdriver.find_element_by_xpath(
            '//*[@id="idViewGroup"]').click()
        newdriver.find_element_by_xpath("//*[@id='DocumentViewButtonAll']/a").click()
        time.sleep(10)
        file_rename(f'{job_id}_fl_flagler_Document_{DOCUMENT_NUMBER}.pdf')

    newdriver.quit()

    # driver.close()


def details_extractor(doc, json_data, doc_type):
    try:
        print("Detail Extractor")
        update_log("Detail Extractor")
        select = Select(driver.find_element_by_name("resultsTable_length"))
        pages_count = 100
        total_pages = 0
        if json_data["INO"] != '' or json_data["BP"] != '':
            total_pages = 1
        else:
            try:
                select.select_by_value('-1')
            except Exception as e:
                error_log(e,driver)

            time.sleep(2)
            total_data = driver.find_elements_by_xpath('//*[@id="resultsTable"]/tbody/tr')

            try:
                total_pages = len(total_data)
            except Exception as e:
                error_log(e,driver)

        update_log(f"Total No. of Record Found={total_pages}")

        update_log("Navigating Urls")
        for j in range(1, total_pages + 1):
            try:
                cursor.execute(f"INSERT or IGNORE INTO docUrlTable_{job_id} VALUES(?,?,?)",
                               [j, j, 0])
                conn.commit()
            except Exception as e:
                error_log(e,driver)

        print(total_pages)
        update_log("Multiple Extraction")
        futures = [executor.submit(details_data_extractor, json_data, url, doc_type) for url in range(1, total_pages + 1)]
        wait(futures)
        driver.close()
    except Exception as e:
        update_log("Unable to Process Search")

        error_log(e,driver)
        log_terminate()
        try:
            driver.close()
        except:
            pass

def download_data(config, type, doc):
    if configfile != "":
        print(type)
        json_data = json.loads(open(config, "r").read())
        wait = WebDriverWait(driver, 90)
        driver.get("https://apps.flaglerclerk.com/Landmark/")
        driver.find_element_by_xpath('//*[@id="bodySection"]/div/div/div[3]/div/div[1]/a/img').click()
        driver.find_element_by_id('idAcceptYes').click()
        update_log("Login Successful")
        if json_data["NAME"] != "":
            parcelclick = driver.find_element_by_xpath('//*[@id="searchCriteriaName-tab"]')
            if parcelclick != "":
                parcelclick.click()
            time.sleep(1)

            try:
                driver.find_element_by_xpath('//*[@id="matchType-Name"]/option[2]').click()
                time.sleep(1)
                driver.find_element_by_id("name-Name").send_keys(json_data["NAME"])
                takeScreenShot(driver, "County_date_valid_Thru_" + datetime.now().strftime("%d%m%y%H%M%S") + ".png")
                time.sleep(2)
                driver.find_element_by_id("submit-Name").click()
            except Exception as e:
                error_log(e,driver)

        elif json_data["APN"] != "":
            parcelclick = driver.find_element_by_xpath('//*[@id="searchCriteriaParcelId-tab"]')
            if parcelclick != "":
                parcelclick.click()

            try:
                time.sleep(1)
                driver.find_element_by_xpath('//*[@id="matchType-ParcelId"]/option[2]').click()
                driver.find_element_by_id("parcelId").send_keys(json_data["APN"])
                takeScreenShot(driver, "County_date_valid_Thru_" + datetime.now().strftime("%d%m%y%H%M%S") + ".png")
                time.sleep(2)
                driver.find_element_by_id("submit-ParcelId").click()
            except Exception as e:
                error_log(e,driver)

        elif json_data["DOCTYPE"] != "":
            parcelclick = driver.find_element_by_xpath('//*[@id="searchCriteriaDocuments-tab"]')
            if parcelclick != "":
                parcelclick.click()
            try:
                driver.find_element_by_id("documentType-DocumentType").send_keys(json_data["DOCTYPE"])
                takeScreenShot(driver, "County_date_valid_Thru_" + datetime.now().strftime("%d%m%y%H%M%S") + ".png")
                time.sleep(2)
                driver.find_element_by_id("submit-DocumentType").click()
            except Exception as e:
                error_log(e,driver)

        elif json_data["BP"] != "":
            parcelclick = driver.find_element_by_xpath('//*[@id="searchCriteriaBookPage-tab"]')
            if parcelclick != "":
                parcelclick.click()
            bp = json_data["BP"].split("/")
            try:
                driver.find_element_by_id("book").send_keys(bp[0])
                driver.find_element_by_id("page").send_keys(bp[1])
                takeScreenShot(driver, "County_date_valid_Thru_" + datetime.now().strftime("%d%m%y%H%M%S") + ".png")
                time.sleep(2)
                driver.find_element_by_id("submit-BookPage").click()
            except Exception as e:
                error_log(e,driver)

        elif json_data["CASE"] != "":
            parcelclick = driver.find_element_by_xpath('//*[@id="searchCriteriaCaseNumber-tab"]')
            if parcelclick != "":
                parcelclick.click()
            try:
                driver.find_element_by_id("caseNumber").send_keys(json_data["CASE"])
                takeScreenShot(driver, "County_date_valid_Thru_" + datetime.now().strftime("%d%m%y%H%M%S") + ".png")
                time.sleep(2)
                driver.find_element_by_id("submit-CaseNumber").click()
            except Exception as e:
                error_log(e,driver)

        elif json_data["RSDATE"] != "":
            parcelclick = driver.find_element_by_xpath('//*[@id="searchCriteriaRecordDate-tab"]')
            if parcelclick != "":
                parcelclick.click()
            try:
                driver.find_element_by_id("beginDate-RecordDate").send_keys(Keys.CONTROL + 'a')
                driver.find_element_by_id("beginDate-RecordDate").send_keys(Keys.BACKSPACE)
                driver.find_element_by_id("endDate-RecordDate").send_keys(Keys.CONTROL + 'a')
                driver.find_element_by_id("endDate-RecordDate").send_keys(Keys.BACKSPACE)
                driver.find_element_by_id("beginDate-RecordDate").send_keys(json_data["RSDATE"])
                if json_data["REDATE"] != "":
                    driver.find_element_by_id("endDate-RecordDate").send_keys(json_data["REDATE"])
                else:
                    driver.find_element_by_id("endDate-RecordDate").send_keys(json_data["RSDATE"])
                takeScreenShot(driver, "County_date_valid_Thru_" + datetime.now().strftime("%d%m%y%H%M%S") + ".png")
                time.sleep(2)
                driver.find_element_by_id("submit-RecordDate").click()
            except Exception as e:
                error_log(e,driver)

        elif json_data["INO"] != "":
            parcelclick = driver.find_element_by_xpath('//*[@id="searchCriteriaInstrumentNumber-tab"]')
            if parcelclick != "":
                parcelclick.click()
            try:
                driver.find_element_by_id("instrumentNumber").send_keys(json_data["INO"])
                takeScreenShot(driver, "County_date_valid_Thru_" + datetime.now().strftime("%d%m%y%H%M%S") + ".png")
                time.sleep(2)
                driver.find_element_by_id("submit-InstrumentNumber").click()
            except Exception as e:
                error_log(e,driver)

        elif json_data["LEGAL"] != "":
            parcelclick = driver.find_element_by_xpath('//*[@id="searchCriteriaLegal-tab"]')
            if parcelclick != "":
                parcelclick.click()
            try:
                driver.find_element_by_id("legal").send_keys(json_data["LEGAL"])
                takeScreenShot(driver, "County_date_valid_Thru_" + datetime.now().strftime("%d%m%y%H%M%S") + ".png")
                time.sleep(2)
                driver.find_element_by_id("submit-Legal").click()
            except Exception as e:
                error_log(e,driver)

        if type == "S":
            update_log("Starting Short Data Extractor")
            select = Select(driver.find_element_by_name("resultsTable_length"))
            try:
                select.select_by_value('-1')
            except Exception as e:
                error_log(e,driver)

            time.sleep(10)
            if json_data["INO"] != '' or json_data["BP"] != '':
                total_data = 1
            else:
                total_data = driver.find_elements_by_xpath('//*[@id="resultsTable"]/tbody/tr')

            total_data_count = 0
            try:
                total_data_count = len(total_data) + 1
            except Exception as e:
                error_log(e,driver)

            for j in range(1, total_data_count + 1):
                try:
                    cursor.execute(f"INSERT or IGNORE INTO pageUrlTable_{job_id} VALUES(?,?,?)",
                                   [j, j, 0])
                    conn.commit()
                except Exception as e:
                    error_log(e, driver)
            time.sleep(2)
            driver.find_element_by_id('results-Print').click()
            time.sleep(5)
            driver.switch_to.window(driver.window_handles[1])
            time.sleep(5)
            driver.execute_script("window.print()")
            time.sleep(2)
            driver.close()
            driver.switch_to.window(driver.window_handles[0])
            time.sleep(2)
            response1 = HtmlResponse(url='https://www.example.com', body=driver.page_source.encode('utf-8'))
            a = FlaglerTableSpider(job_id)
            a.extract_data(total_data_count, response1, json_data)
            driver.close()
        elif type == "F":
            update_log("Starting Full Data Extractor")
            details_extractor(doc, json_data, doc)


if __name__ == "__main__":
    try:

        # try:
        #     cnxn = pyodbc.connect(
        #         "Driver={SQL Server};Server=51.81.242.172\DESQL;Database=county_search;UID=sa;PWD=ida@#2021;Trusted_Connection=no;")
        #     mscursor = cnxn.cursor()
        #     cur = mscursor.execute(f"Select Full_Log from statusTable WHERE JOBID={job_id}")
        #     vals = [i for i in cur]
        #     full_log = vals[0][0]
        #     print(full_log)
        #     mscursor.close()
        #
        # except:
        #     full_log = ""

        print(full_log)
        getall = False
        ua = UserAgent()
        userAgent = ua.random
        print("userAgent", userAgent)

        driver = get_chromedriver(use_proxy=True, ji=job_id)
        WebDriverWait(driver, 50)
        driver.maximize_window()
        driver.implicitly_wait(5)
        configfile = ""
        options = Options()

        try:
            cursor.execute(f"""CREATE TABLE IF NOT EXISTS docUrlTable_{job_id} (
                            doc_num NOT NULL PRIMARY KEY,
                            doc_url,
                            status
                             )""")

            cursor.execute(f"""CREATE TABLE IF NOT EXISTS pageUrlTable_{job_id} (
                                               page_num NOT NULL PRIMARY KEY,
                                               page_url,
                                               status
                                                )""")

            cursor.execute("""CREATE TABLE IF NOT EXISTS jobData (
                                                                      job_num NOT NULL PRIMARY KEY,
                                                                      json_data,
                                                                      status
                                                                       )""")
        except Exception as e:
            error_log(e)
        conn.commit()
        try:
            sqlcommad("INSERT INTO statusTable VALUES(?,?,?,?,?)", (job_id, "JOB ID INSERTED", "JOB ID INSERTED", 0, 0))

        except:
            pass
        update_log("Search Algorithm Started")
        if results.config == "":
            print("Please provide the config file by (--config file_name)")
        else:
            sqlcommad("UPDATE statusTable SET Status = ? WHERE JOBID = ?", (1, job_id))
            update_log("Search Initializing")
            j = json.dumps(json_data)
            cursor.execute("INSERT or IGNORE INTO jobData VALUES(?,?,?)", [job_id, j, 0])
            conn.commit()
            configfile = str(results.config)
            print(configfile)
            download_data(configfile, results.type, results.doc)
            cursor.execute("UPDATE jobData SET status = ? WHERE job_num = ?", [1, job_id])
            conn.commit()
            update_log("Completed Collecting Data")
            sqlcommad("UPDATE statusTable SET Status = ? WHERE JOBID = ?", (2, job_id))
            conn.close()
            #configpath = f'D:/GENERAL_OUTPUT/FL/fl_flagler/{job_id}/config_{job_id}.json'
            #if os.path.exists(configpath):
                #    os.remove(configpath)
    except:
        log_terminate()

    try:
        params = urllib.parse.quote(
            "Driver={SQL Server};Server=51.81.242.172\DESQL;Database=county_search;UID=sa;PWD=ida@#2021;Trusted_Connection=no;")
        cnxn = sqlalchemy.create_engine("mssql+pyodbc:///?odbc_connect=%s" % params)

        csv_new = glob.glob("D:/GENERAL_OUTPUT/FL/fl_flagler/%s/*.csv" % job_id)[0]
        df = pd.read_csv(csv_new, header="infer", sep=",", dtype=str, na_filter=False)  # keep_default_na=False)
        # df = df.fillna('')
        df.to_sql("TestOUT", cnxn, if_exists='append')
    except Exception as e:
        print(e)

        pass
