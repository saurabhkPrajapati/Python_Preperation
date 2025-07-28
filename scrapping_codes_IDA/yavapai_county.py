import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
# from selenium.webdriver.remote.webelement import WebElement
# from selenium.webdriver.support.wait import WebDriverWait
# from selenium.webdriver.support import expected_conditions as EC
# import xml.etree.ElementTree as ET
# from itertools import countfrom selenium.webdriver import ActionChains


driver= webdriver.Chrome()
driver.get("https://yavapaicountyaz-web.tylerhost.net/web/")
driver.implicitly_wait(8)
driver.find_element_by_tag_name('html').send_keys(Keys.PAGE_DOWN)
driver.find_element(By.XPATH,"//button[contains(@id,'submitDisclaimerAccept')]").click()
driver.find_element(By.XPATH,"//a[contains(@class,'ss-action ss-action-form ss-utility-box ss-action-page-search ui-link')][1]").click()

driver.find_element_by_id('field_RecordingDateID_DOT_StartDate').click()
driver.find_element_by_id('field_RecordingDateID_DOT_StartDate').send_keys("01012020")

driver.find_element_by_id('field_RecordingDateID_DOT_EndDate').click()
driver.find_element_by_id('field_RecordingDateID_DOT_EndDate').send_keys("01052020")

driver.find_element_by_tag_name('html').send_keys(Keys.PAGE_DOWN)
driver.find_element(By.XPATH,"//a[contains(@id,'searchButton')]").click()

time.sleep(8)
links=[]
lists=driver.find_elements_by_xpath('/html/body/div[1]/div[2]/div/div[2]/div/div[2]/ul/li[3]/ul/li')
for i in lists:
    links.append(str(i.get_attribute('data-href')))

print(links)
print(len(links))
result=[]
count=1
for i in links:
   if count>25:
       break
   driver.get('https://yavapaicountyaz-web.tylerhost.net'+i)
   time.sleep(2)
   try:
       a = driver.find_element(By.XPATH,
                           "//*[contains(@id,'documentIndexingInformation')]/div[1]/div/div/div[1]/ul/li[2]/table/tbody/"
                           "tr/td[1]/ul/li[2]/table/tbody/tr[1]/td/div[2]").text
   except:
       a=None
   try:
       b = driver.find_element(By.XPATH, "//*[contains(@id,'documentIndexingInformation')]/div[1]/div/div/div[1]/ul/li[2]/"
                                     "table/tbody/tr/td[1]/ul/li[2]/table/tbody/tr[2]/td/div[2]").text
   except:
       b=None

   try:
       c = driver.find_element(By.XPATH, "//*[contains(@id,'documentIndexingInformation')]/div[1]/div/div/div[1]/ul/li[2]/"
                                  "table/tbody/tr/td[1]/ul/li[2]/table/tbody/tr[3]/td/div[2]").text
   except:
       c = None

   try:
       d = driver.find_element(By.XPATH,
                           "//*[contains(@id,'documentIndexingInformation')]/div[1]/div/div/div[1]/ul/li[2]/table/"
                           "tbody/tr/td[1]/ul/li[2]/table/tbody/tr[5]/td/div[2]").text
   except:
       d = None
   try:
       e = driver.find_element(By.XPATH,
                           "//*[contains(@id,'documentIndexingInformation')]/div[1]/div/div/div[1]/ul/li[2]/table/tbody/"
                           "tr/td[1]/ul/li[2]/table/tbody/tr[6]/td/div[2]").text
   except:
       e = None

   try:
       f = (driver.find_element(By.XPATH, "//strong[contains(text(),'City:')]/..").text).replace('City:\n','')


   except:
       f = 'None'


   try:
       g =( driver.find_element(By.XPATH,"//strong[contains(text(),'Return To:')]/../"
                                         "following-sibling::div" ).text).replace('Return To:\n','')


   except:
       g='None'

   try:
       h = (driver.find_element(By.XPATH, "//strong[contains(text(),'Address1:')]/..").text).replace('Address1:\n','')

   except:
       h = 'None'
   try:
       i = (driver.find_element(By.XPATH, "//strong[contains(text(),'State:')]/..").text).replace('State:\n','')

   except:
       i = 'None'
   try:
       j = (driver.find_element(By.XPATH, "//strong[contains(text(),'Zip:')]/..").text).replace('Zip:\n','')

   except:
       j ='None'
   try:
       k = ( driver.find_element(By.XPATH, "((//*[contains(@class,'ui-responsive doc-viewer "
                                          "ui-table ui-table-reflow')])[4]//ul)[1]").text).replace('\n','')

   except:
       k = 'None'
   try:
       l =  (driver.find_element(By.XPATH,
                                "((//*[contains(@class,'ui-responsive doc-viewer"
                                " ui-table ui-table-reflow')])[4]//ul)[2]").text).replace('\n','')

   except:
       l = 'None'




   temp={'Number Pages': a, 'Recording Fee': b, 'Reception Number': c, 'Recording Date': d, 'Document Date': e,'Return To':g,
         'Address':h,'City':f,'State':i,'Zip':j ,'Grantor':k ,'Grantee':l }
   result.append(temp)
   count+=1
print(len(result))

import pandas_practice as pd
df=pd.DataFrame(result).to_csv('file.csv')

driver.close()