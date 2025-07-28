import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys



driver= webdriver.Chrome(executable_path=r'C:\Users\91880\PycharmProjects\pythonProject\chromedriver.exe',)
driver.get("https://starr.tx.publicsearch.us/search/advanced/")
driver.implicitly_wait(8)

#
driver.find_element_by_id('recordedDateRange').click()
driver.find_element_by_id('recordedDateRange').send_keys(Keys.CONTROL,"a",Keys.BACK_SPACE)
# driver.find_element_by_id('recordedDateRange').clear()
driver.find_element_by_id('recordedDateRange').send_keys("1/5/2020")

driver.find_element(By.XPATH,"(//input[contains(@aria-label,'end date')])[1]").click()
driver.find_element(By.XPATH,"(//input[contains(@aria-label,'end date')])[1]").send_keys(Keys.CONTROL,"a",Keys.BACK_SPACE)
#driver.find_element(By.XPATH,"(//input[contains(@aria-label,'end date')])[1]").clear()  not working
driver.find_element(By.XPATH,"(//input[contains(@aria-label,'end date')])[1]").send_keys("1/7/2020")
time.sleep(8)
driver.find_element_by_tag_name('html').send_keys(Keys.PAGE_DOWN)
driver.find_element(By.XPATH,"//button[contains(@class,'advanced_search__search-button')]").click()

time.sleep(8)
count=1
total_rows=driver.find_elements(By.XPATH,"//tbody/tr")
driver.find_element(By.XPATH,"//td[contains(@class,'col-2 isDropdown hasIcon')]").click()

time.sleep(4)

driver.find_element(By.XPATH,"(//div[contains(@class,'linkText')])[2]").click()

list=[]
resume=True
for i in range(len(total_rows)):
    try:
        Document_Number=driver.find_element(By.XPATH,"//span[contains(text(),'Document Number:')]/following-sibling::span").text
    except:
        Document_Number=''

    try:
        Number_of_Pages=driver.find_element(By.XPATH,"//span[contains(text(),'Number of Pages:')]/following-sibling::span").text
    except:
        Number_of_Pages=''
    try:
        Recorded_Date=driver.find_element(By.XPATH,"//span[contains(text(),'Recorded Date:')]/following-sibling::span").text
    except:
        Recorded_Date=''
    try:
        Book_OR_Volume_OR_Page=driver.find_element(By.XPATH,"//span[contains(text(),'Book/Volume/Page:')]/following-sibling::span").text
    except:
        Book_OR_Volume_OR_Page=''
    try:
        Instrument_Date=driver.find_element(By.XPATH,"//span[contains(text(),'Instrument Date:')]/following-sibling::span").text
    except:
        Instrument_Date=''
    try:
        Consideration=driver.find_element(By.XPATH,"//span[contains(text(),'Consideration:')]/following-sibling::span").text
    except:
        Consideration=''
    # link=driver.find_elements_by_partial_link_text('results?department=RP&parties=%5B%7B%22term%')
    # for i in link:
    #        print(i.text)
    #        print(i)

    try:
        GRANTOR=driver.find_element(By.XPATH,"//span[contains(text(),'GRANTOR')]/preceding-sibling::a").text
    except:
        GRANTOR=''
    try:
        GRANTEE=driver.find_element(By.XPATH,"//span[contains(text(),'GRANTEE')]/preceding-sibling::a").text
    except:
        GRANTEE=''
    try:
        Legal_Description=driver.find_element(By.XPATH,"//h4[contains(text(),'Legal Description')]/following-sibling::p").text
    except:
        Legal_Description=''

    try:
        Marginal_References=driver.find_element(By.XPATH,"//h4[contains(text(),'Marginal References')]/following-sibling::p").text
    except:
        Marginal_References=''
    try:
        Document_Remarks=driver.find_element(By.XPATH,"//h4[contains(text(),'Document Remarks')]/following-sibling::p").text
    except:
        Document_Remarks=''
    try:
        Lot_OR_Block=driver.find_element(By.XPATH,"//h4[contains(text(),'Lot/Block')]/following-sibling::p").text
    except:
        Lot_OR_Block=''
    dict={'Document_Number':Document_Number,'Number_of_Pages':Number_of_Pages,'Recorded_Date':Recorded_Date,'Book_OR_Volume_OR_Page':Book_OR_Volume_OR_Page,
              'Instrument_Date':Instrument_Date ,'Consideration':Consideration,'GRANTOR':GRANTOR,'GRANTEE':GRANTEE,'Legal_Description':Legal_Description
          ,'Marginal_References':Marginal_References,'Document_Remarks':Document_Remarks,'Lot_OR_Block':Lot_OR_Block }
    list.append(dict)
    time.sleep(2)
    driver.find_element(By.XPATH,"//button[contains(text(),'Next Doc >')]").click()





print(len(list))

import pandas_practice as pd
df=pd.DataFrame(list).to_csv('starr.csv')

driver.close()

