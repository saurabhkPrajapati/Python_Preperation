import scrapy
import configparser as cp
import os
import sys
import time
import traceback
import zipfile
from datetime import datetime

from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import  ActionChains

parser = cp.ConfigParser()
parser.read('config.ini')
opmode = int(parser.get("General", "opmode"))
options = Options()
if opmode == 2:
    options.add_argument("--headless")
PROXY_HOST = 'x.botproxy.net'  # rotating proxy
PROXY_PORT = 8080
PROXY_USER = 'pxu18829-0+us-ca'
PROXY_PASS = 'z5uglHJthAcKOAqd0MUM'
manifest_json = """
{
    "version": "1.0.0",
    "manifest_version": 2,
    "name": "Chrome Proxy",
    "permissions": [
        "proxy",
        "tabs",
        "unlimitedStorage",
        "storage",
        "<all_urls>",
        "webRequest",
        "webRequestBlocking"
    ],
    "background": {
        "scripts": ["background.js"]
    },
    "minimum_chrome_version":"22.0.0"
}
"""

background_js = """
var config = {
        mode: "fixed_servers",
        rules: {
          singleProxy: {
            scheme: "http",
            host: "%s",
            port: parseInt(%s)
          },
          bypassList: ["localhost"]
        }
      };

chrome.proxy.settings.set({value: config, scope: "regular"}, function() {});

function callbackFn(details) {
    return {
        authCredentials: {
            username: "%s",
            password: "%s"
        }
    };
SD}

chrome.webRequest.onAuthRequired.addListener(
            callbackFn,
            {urls: ["<all_urls>"]},
            ['blocking']
);
""" % (PROXY_HOST, PROXY_PORT, PROXY_USER, PROXY_PASS)
use_proxy = 1
user_agent = 1
if len(sys.argv) > 1:
    fname = sys.argv[1]
options.add_argument('--log-level=3')
if use_proxy:
    pluginfile = 'proxy_auth_plugin.zip'
    with zipfile.ZipFile(pluginfile, 'w') as zp:
        zp.writestr("manifest.json", manifest_json)
        zp.writestr("background.js", background_js)
    options.add_extension(pluginfile)
if user_agent:
    options.add_argument('--user-agent=%s' % user_agent)

dt1 = input("Enter the First Date(mm/dd/YYYY): ").replace("\n", "")
fir_date = datetime.strptime(dt1, '%m/%d/%Y').strftime("%A")
while fir_date in ['Saturday', 'Sunday']:
    print("No records found for this start date")
    dt1 = input("Enter the start date again(mm/dd/YYYY):").replace("\n", "")
    fir_date = datetime.strptime(dt1, '%m/%d/%Y').strftime("%A")
else:
    pass

dt2 = input("Enter the Next date(mm/dd/YYYY): ").replace("\n", "")
lst_date = datetime.strptime(dt2, '%m/%d/%Y').strftime("%A")
while lst_date in ['Saturday', 'Sunday']:
    print("No records found for this end date")
    dt2 = input("Enter the end date again(mm/dd/YYYY): ").replace("\n", "")
    lst_date = datetime.strptime(dt2, '%m/%d/%Y').strftime("%A")
else:
    pass
options = webdriver.ChromeOptions()
options.add_argument("--window-size=1920,1080")
options.add_argument("--disable-gpu")
options.add_argument("--disable-extensions")
options.add_experimental_option("useAutomationExtension", False)
options.add_argument("--proxy-server='direct://'")
options.add_argument("--proxy-bypass-list=*")
options.add_argument("--start-maximized")
driver = webdriver.Chrome(chrome_options=options, executable_path=r'C:\Users\Saurabh prajapati\PycharmProjects\selenium\chromedriver92\chromedriver.exe')
# driver.maximize_window()
driver.implicitly_wait(3)  # seconds

def init_entry(driver, dt):
    driver.get("https://www.recorder.pima.gov/PublicServices/PublicSearch")
    time.sleep(8)
    driver.find_element_by_xpath("//div/input[@name='ContentPlaceHolder1_txtStartDate']").click()
    driver.find_element_by_xpath("//div/input[@name='ContentPlaceHolder1_txtStartDate']").send_keys(dt)
    time.sleep(4)
    driver.find_element_by_xpath("//div/input[@name='ContentPlaceHolder1_txtEndDate']").click()
    driver.find_element_by_xpath("//div/input[@name='ContentPlaceHolder1_txtEndDate']").send_keys(dt)

    time.sleep(4)
    driver.find_element_by_tag_name('html').send_keys(Keys.PAGE_DOWN)
    driver.find_element_by_xpath("//input[@name='ctl00$ContentPlaceHolder1$btnDocumentSearch']").click()
    time.sleep(7)
    try:
        driver.find_element_by_xpath("//button[text()='Ok']").click()
    except:
        pass
    time.sleep(10)
    # WebDriverWait(driver,25).until(EC.element_to_be_clickable((By.XPATH,"//a[text()='Sequence #']"))).send_keys(Keys.ENTER)
    # element = driver.find_element_by_xpath("//a[text()='Sequence #']")
    # driver.execute_script("arguments[0].click();" , element)
    # action = ActionChains(driver)
    # element = driver.find_element_by_xpath("""//a[@href ="javascript:__doPostBack('ctl00$ContentPlaceHolder1$gvDocuments','Sort$SEQUENCE_NO')"]""")
    # element = driver.find_element_by_xpath("//a[text()='Sequence #']")
    # action.move_to_element(element).perform()
    # element.click()
    # if dt = dt1:
    s1 = str(driver.find_element_by_xpath("(//tr/td/following-sibling::td)[2]").text)
    driver.find_element_by_xpath("//a[text()='Sequence #']").click()
    time.sleep(3)
    try:
        driver.find_element_by_xpath("//button[text()='Ok']").click()
    except:
        pass
    s2 = str(driver.find_element_by_xpath("(//tr/td/following-sibling::td)[2]").text)
    driver.find_element_by_xpath("//a[text()='Sequence #']").click()
    time.sleep(3)
    try:
        driver.find_element_by_xpath("//button[text()='Ok']").click()
    except:
        pass
    s3 = str(driver.find_element_by_xpath("(//tr/td/following-sibling::td)[2]").text)
    sequence = min(s1,s2,s3)
    try:
        return sequence
    except:
        print("No records for Start Date")
    time.sleep(2)


try:
    strt_doc_num = init_entry(driver, dt1)
    end_doc_num = init_entry(driver, dt2)
    parser.set("General", "startdate", str(dt1))
    parser.set("General", "nextdate", str(dt2))
    parser.set("General", "start_doc_num", str(strt_doc_num))
    parser.set("General", "ending_doc_num", str(end_doc_num))
    parser.set("General", "total_doc_num", str(end_doc_num + "to" + strt_doc_num))
    parser.set("General", "status", "True")
    parser.write(open('config.ini', "w"))
    print("Config Created successfully")
    driver.close()
    # os.system(f"scrapy crawl pima_countyy -o AZ-PIMA-{dt1.replace('/', '')}.csv")
    # os.system('python remove_head.py AZ-PIMA-%s.csv' %dt1.replace('/', ''))
    os.system(f"scrapy crawl costa -o CA-CONTRACOSTA-6182020.csv")
    # os.system(f"scrapy crawl costa -o CA-CONTRACOSTA-{dt1.replace('/', '')}.csv")
    # os.system('python remove_head.py CA-CONTRACOSTA-%s.csv' %dt1.replace('/', ''))

except Exception as e:
    driver.close()
    parser.set("General", "startdate", str(dt1))
    parser.set("General", "nextdate", str(dt2))
    parser.set("General", "status", "False")
    parser.write(open('config.ini', "w"))
    print("Config Created successfully")
    print(traceback.print_exc())
    print("Exception 2")
    pass

# from scrapy.cmdline import execute
# execute('scrapy crawl prima'.split())
# execute('scrapy crawl prima -o AZ-PIMA-06212021.csv'.split())


# time.sleep(3)
# print('success')
# print(first_sequence)
# print(end_sequence)
# start = int(first_sequence) - int(end_sequence)
# begin = int(first_sequence)
# print(begin)
# time.sleep(4)
