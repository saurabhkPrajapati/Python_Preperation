from argparser import argparse1
import json
import time
import pyodbc
from selenium.webdriver.support.select import Select
import re
from ProxyBot import get_chromedriver
from scrapy.http import HtmlResponse
from DataExtractor import *

parser = argparse1.ArgumentParser()
parser.add_argument('--type', action="store", dest='type',
                    help='Download type ("--type S" for short or "--type F" for Full)', default="S")
parser.add_argument('--doc', action="store", dest='doc',
                    help='Download documents "--doc Y" or not "--doc N"', default="Y")
parser.add_argument('--config', action="store", dest='config',
                    help='Path of config or format file "--config file_path"', default="config.json")
parser.add_argument('--no', action="store", dest='no',
                    help='Document Number by "--no number"', default="polk")
results = parser.parse_args()
job_id = results.no
doc_type = results.doc
type = results.type
json_data = json.loads(open(results.config, "r").read())
error_json = json.loads(open("../error_json.json", "r").read())
configfile = str(results.config)
full_log = ""

def sqlcommad(command, values):
    # mycursor = mydb.cursor()
    sql = command
    val = values
    # mycursor.execute(sql, val)
    # mydb.commit()
    print(sql,val)
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


def file_rename(file_name):
    download_path = "D:/GENERAL_OUTPUT/FL/fl_polk_a/%s/" % job_id
    filename = max([download_path + "\\" + f for f in os.listdir(download_path)], key=os.path.getctime)
    os.rename(filename, os.path.join(download_path, f"{file_name}"))


def full_log_func(log):
    global full_log
    if full_log != "":
        full_log = full_log + "|" + log
    else:
        full_log = full_log + log + "|"
    return full_log


def update_log( f_log):
    f = full_log_func(f_log)
    try:
        sqlcommad("UPDATE statusTable SET Current_Log = ?, Full_Log = ? WHERE JOBID = ?", (f_log, f, job_id))
    except:
        pass

def takeScreenShot(driver, snap_name):
    try:
        screenshot_path = "D:/GENERAL_OUTPUT/FL/fl_polk_a/%s/" % job_id
        if snap_name == "":
            filename = datetime.now().strftime("%d%m%y%H%M%S") + ".png"
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
    except Exception as e:
        # update_log("Process Crashed")
        error_log(e)
        try:
            driver.close()
        except:
            pass


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
    if "FileNotFoundError" in exc_type:
        update_log(error_json["202"])
        error_code = "202"
    elif "NoSuchElementException" in exc_type:
        update_log(error_json["101"])
        error_code = "101"
    elif "EmptyDataError" in exc_type:
        update_log(error_json["201"])
        error_code = "201"
    elif "IntegrityError" in exc_type:
        update_log(error_json["501"])
        error_code = "501"
    elif "NoSuchWindowException" in exc_type:
        update_log(error_json["501"])
        error_code = "501"
    elif "WebDriverException" in exc_type:
        update_log(error_json["103"])
        error_code = "103"
    elif "Program Terminated" in exc_type:
        update_log(error_json["401"])
        error_code = "401"
    else:
        update_log("Unknown Error")
        error_code = "601"
    sqlcommad("INSERT INTO Table_Error VALUES(?,?,?,?)", (job_id, error_code, sc_path, msg))


def find_count(stringdata):
    total = re.match(".+([0-9 ]+) Matches found", stringdata, flags=re.I)
    if total:
        num = total.group(1)
    else:
        total = re.match("([0-9 ]+) Matches found", stringdata, flags=re.I)
        if total:
            num = total.group(1)
        else:
            num = ""
    # num = str(num).replace(" ", "")
    return int(num)

def download_data(json_data):
    update_log("Search Initializing")
    driver = get_chromedriver(use_proxy=True, ji=job_id)
    driver.maximize_window()
    driver.implicitly_wait(5)
    try:
        # driver.get("https://www.polkpa.org/CamaDisplay.aspx?cookie_test=true")
        driver.get("https://www.polkpa.org/CamaDisplay.aspx?OutputMode=Input&searchType=RealEstate&page=FindByOwnerName")
        update_log("Login Successful")
        if json_data["ON"] != "":
            try:
                driver.find_element_by_id("OwnerName").send_keys(json_data["ON"])
                time.sleep(1)
                select = Select(driver.find_element_by_xpath('//select[@title="Records per Page"]'))
                select.select_by_value("250")
                time.sleep(1)
                driver.find_element_by_id('searchRE_name').click()
            except Exception as e:
                error_log(e, driver)
        elif json_data["APN"] != "":
            try:
                driver.find_element_by_xpath('//a[text()="Find Parcel By ID"]').click()
                time.sleep(4)
                driver.find_element_by_id("parcelID").send_keys(json_data["APN"])
                time.sleep(1)
                select = Select(driver.find_element_by_xpath('//select[@title="Records per Page"]'))
                select.select_by_value("250")
                time.sleep(1)
                driver.find_element_by_id('searchRE_id').click()
            except Exception as e:
                error_log(e, driver)

        elif json_data["PADD"] != "":
            try:
                driver.find_element_by_xpath('//a[text()="Find Parcel By Site Address"]').click()
                time.sleep(4)
                driver.find_element_by_id("address").send_keys(json_data["PADD"])
                time.sleep(1)
                select = Select(driver.find_element_by_xpath('//select[@title="Records per Page"]'))
                select.select_by_value("250")
                time.sleep(1)
                driver.find_element_by_id('searchRE_address').click()
            except Exception as e:
                error_log(e, driver)

        time.sleep(5)
        try:
            check_multi = find_count(driver.find_element_by_xpath('//div[@id="CamaDisplayArea"]/span').text)
        except:
            check_multi = 1
        if check_multi > 1:
            update_log("Start Collecting Multiple Data")
            # tabledata = len(driver.find_elements_by_xpath('//div[@id="CamaDisplayArea"]/span'))
            update_log(f"Total {check_multi} Data Found")
            for i in range(2, check_multi + 1):
                time.sleep(1)
                url = driver.find_element_by_xpath(
                    f'(//*[@class="parcelid"])[{i}]/a').get_attribute('href')
                update_log(f"Data Processing = {i-1}")
                driver.execute_script("window.open('%s','newwindow%s')" % (url, i))
                # driver.switch_to.window('newwindow%s' %i)
                driver.switch_to.window(driver.window_handles[1])
                driver.execute_script('window.print()')
                time.sleep(1)
                file_rename(f'{job_id}_fl_polk_a_PropertyDoc{i}.pdf')
                response1 = HtmlResponse(url='https://www.example.com', body=driver.page_source.encode('utf-8'))
                DataExtractor(response1, job_id)
                try:
                    driver.find_element_by_xpath('//img[@alt="Parcel Tax Bill"]').click()
                    time.sleep(5)
                    driver.close()
                    driver.switch_to.window(driver.window_handles[1])
                    driver.maximize_window()
                    driver.find_element_by_xpath('//input[@value="Click Here to Continue"]').click()
                    time.sleep(5)
                    driver.switch_to.window(driver.window_handles[1])
                    try:
                        driver.find_element_by_xpath('//span[contains(text(),"Print Bill")]').click()
                    except:
                        driver.execute_script('window.print()')
                    file_rename(f'{job_id}_fl_polk_a_Tax_Screenshot{i}.pdf')
                except:
                    driver.find_element_by_xpath('//img[@alt="Trim Notice"]').click()
                    time.sleep(10)
                    driver.switch_to.window(driver.window_handles[2])
                    driver.close()
                    driver.switch_to.window(driver.window_handles[1])
                driver.close()
                driver.switch_to.window(driver.window_handles[0])
            update_log("Completed Collecting Data")
            driver.quit()
        else:
            update_log("Start Collecting Single Data")
            update_log(f"Total {check_multi} Data Found")
            time.sleep(3)
            url = driver.find_element_by_xpath(
                f'(//*[contains(@class,"parcelid")])[2]/a').get_attribute('href')
            driver.execute_script("window.open('%s','newwindow%s')" % (url, 1))
            driver.switch_to.window(driver.window_handles[1])
            driver.execute_script('window.print()')
            time.sleep(1)
            file_rename(f'{job_id}_fl_polk_a_PropertyDoc.pdf')
            response1 = HtmlResponse(url='https://www.example.com', body=driver.page_source.encode('utf-8'))
            # DataExtractor(response1, job_id)
            try:
                driver.find_element_by_xpath('//img[@alt="Parcel Tax Bill"]').click()
                time.sleep(5)
                # driver.close()
                driver.switch_to.window(driver.window_handles[1])
                driver.maximize_window()
                driver.find_element_by_xpath('//input[@value="Click Here to Continue"]').click()
                time.sleep(5)
                driver.switch_to.window(driver.window_handles[1])
                try:
                    driver.find_element_by_xpath('//span[contains(text(),"Print Bill")]').click()
                    time.sleep(7)
                except:
                    driver.execute_script('window.print()')
                file_rename(f'{job_id}_fl_polk_a_Tax_Screenshot.pdf')

            except:
                driver.find_element_by_xpath('//img[@alt="Trim Notice"]').click()

                time.sleep(10)
                driver.switch_to.window(driver.window_handles[2])
                driver.close()
            update_log("Completed Collecting Data")
            driver.quit()


    except Exception as e:
        error_log(e, driver)
        driver.quit()


if __name__ == '__main__':
    try:

        # try:
        #     cur = mscursor.execute(f"Select Full_Log from statusTable WHERE JOBID={job_id}")
        #     vals = [i for i in cur]
        #     full_log = vals[0][0]
        #     print(full_log)
        #
        # except:
        #     full_log = ""
        try:
            sqlcommad("INSERT INTO statusTable VALUES(?,?,?,?,?)", (job_id, "JOB ID INSERTED", "JOB ID INSERTED", 0, 0))
        except:
            pass
        update_log("Search Algorithm Started")
        screenshot_path = "screenshot/"
        json_data = json.loads(open(configfile, "r").read())
        sqlcommad("UPDATE statusTable SET Status = ? WHERE JOBID = ?", (1, job_id))
        download_data(json_data)
        sqlcommad("UPDATE statusTable SET Status = ? WHERE JOBID = ?", (2, job_id))
        #configpath = f'D:/GENERAL_OUTPUT/FL/fl_polk_a/{job_id}/{job_id}_config.json'
        #if os.path.exists(configpath):
            #    os.remove(configpath)
    except Exception as e:
        update_log("Could Not Initialize Process")
        log_terminate()
        error_log(e)



