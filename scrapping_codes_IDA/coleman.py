import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

options = webdriver.ChromeOptions()
# options.headless = True
# options.add_experimental_option()
options.add_argument("--window-size=1920,1080")
options.add_argument("--disable-gpu")
options.add_argument("--disable-extensions")
options.add_experimental_option("useAutomationExtension", False)
options.add_argument("--proxy-server='direct://'")
options.add_argument("--proxy-bypass-list=*")
options.add_argument("--start-maximized")
options.add_argument("--headless")
driver = webdriver.Chrome(options=options, executable_path=r'C:\Users\Saurabh prajapati\PycharmProjects\selenium\chromedriver.exe')
driver.get("https://countyfusion3.kofiletech.us/countyweb/loginDisplay.action?countyname=ColemanTX")
driver.implicitly_wait(8)

driver.find_element_by_xpath("//input[@value='Login as Guest']").click()
time.sleep(3)

driver.switch_to.frame("bodyframe")
driver.find_element_by_xpath("//input[@id='accept']").click()
driver.switch_to.frame("bodyframe")
driver.find_element_by_xpath("//tr[@id='datagrid-row-r1-2-0']").click()

driver.switch_to.parent_frame()
driver.switch_to.frame("bodyframe")
driver.switch_to.frame("dynSearchFrame")
driver.switch_to.frame("criteriaframe")
driver.find_element_by_xpath("(//input[contains(@class,'textbox-text validatebox-text')])[2]").click()
driver.find_element_by_xpath("(//input[contains(@class,'textbox-text validatebox-text')])[2]").send_keys("06/18/2021")

driver.find_element_by_xpath("(//input[contains(@class,'textbox-text validatebox-text')])[3]").click()
driver.find_element_by_xpath("(//input[contains(@class,'textbox-text validatebox-text')])[3]").send_keys("06/21/2021")
driver.find_element_by_xpath("(//input[contains(@class,'textbox-text validatebox-text')])[3]").send_keys(Keys.RETURN)
# time.sleep(4)
# driver.switch_to.parent_frame()
driver.switch_to.default_content()
driver.switch_to.frame("bodyframe")
driver.switch_to.frame("resultFrame")
driver.switch_to.frame("resultListFrame")
# driver.find_element_by_xpath("(//a[text()='202101163'])[1]").click()
driver.find_element_by_xpath("//tr[@class='datagrid-row datagrid-row-selected']/descendant::a").click()
# element = driver.find_element_by_xpath("//tr[@class='datagrid-row datagrid-row-selected']/descendant::a")
# driver.execute_script("arguments[0].click();" , element)
# 202101166
list=[]
count=0
while True:
    driver.switch_to.default_content()
    driver.switch_to.frame("bodyframe")
    driver.switch_to.frame("documentFrame")
    driver.switch_to.frame("docInfoFrame")
    # try:
    #     print(driver.find_element_by_xpath("//*[@id='data']/table[5]/tbody/tr/td[2]/table/tbody/tr/td").text)
    # except:
    #     pass
    try:
        Book_Type=driver.find_element_by_xpath("(//span[text()='Book Type:']/../following-sibling::td)[1]").text
    except:
        Book_Type =""
    try:
        Document_No=driver.find_element_by_xpath("(//span[text()='Document No:']/../following-sibling::td)[1]").text
    except:
        Document_No =""
    try:
        Book_No=driver.find_element_by_xpath("(//span[text()='Book No:']/../following-sibling::td)[1]").text
    except:
        Book_No=""
    try:
        Page_No=driver.find_element_by_xpath("(//span[text()='Page No:']/../following-sibling::td)[1]").text
    except:
        Page_No=""
    try:
        Document_Type=driver.find_element_by_xpath("(//span[text()='Document Type:']/../following-sibling::td)[1]").text
    except:
        Document_Type=""
    try:
        License_Number=driver.find_element_by_xpath("(//span[text()='License Number:']/../following-sibling::td)[1]").text

    except:
        License_Number=""
    try:
        Book=driver.find_element_by_xpath("(//span[text()='Book:']/../following-sibling::td)[1]").text
    except:
        Book=""
    try:
        Page=driver.find_element_by_xpath("(//span[text()='Page:']/../following-sibling::td)[1]").text
    except:
        Page=""
    try:
        Filed_Date=driver.find_element_by_xpath("(//span[text()='Filed Date:']/../following-sibling::td)[1]").text
    except:
        Filed_Date=""
    try:
        Filed_Date_Time=driver.find_element_by_xpath("(//span[text()='Filed Date/Time:']/../following-sibling::td)[1]").text
    except:
        Filed_Date_Time=""
    try:
        Marriage_Date=driver.find_element_by_xpath("(//span[text()='Marriage Date:']/../following-sibling::td)[1]").text
    except:
        Marriage_Date=""
    try:
        Instrument_Type=driver.find_element_by_xpath("(//span[text()='Instrument Type:']/../following-sibling::td)[1]").text
    except:
        Instrument_Type=""
    try:
        Instrument_Date=driver.find_element_by_xpath("(//span[text()='Instrument Date:']/../following-sibling::td)[1]").text
    except:
        Instrument_Date=""
    # try:
    #     Grantors=driver.find_element_by_xpath("//span[text()='Grantor(s):']/ancestor::table/following-sibling::table[1]/descendant::td[3]").text
    # except:
    #     Grantors=""

    Grantors = ''
    try:
        # Grantees=driver.find_element_by_xpath("//span[text()='Grantee(s):']/ancestor::table/following-sibling::table[1]/descendant::td[2]")
        Grantorslist = driver.find_elements_by_xpath(
            "//span[text()='Grantor(s):']/ancestor::table/following-sibling::table[1]/descendant::td")
        iter = 0
        for i in Grantorslist:
            iter += 1
            if iter > 2:
                # print(i)
                Grantors = Grantors + "|" + i.text
            #print(Grantors)
        Grantors=Grantors.strip('|').strip('|').lstrip('|')
    except:
        Grantors = ""
    Grantees =""
    try:
        # Grantees=driver.find_element_by_xpath("//span[text()='Grantee(s):']/ancestor::table/following-sibling::table[1]/descendant::td[2]")
        Granteeslist=driver.find_elements_by_xpath("//span[text()='Grantee(s):']/ancestor::table/following-sibling::table[1]/descendant::td")
        iter=0
        for i in Granteeslist:
            iter+=1
            if iter>2:
                #print(i)
                Grantees = Grantees+ "|"+ i.text
            #print(Grantees)
        Grantees=Grantees.strip('|').strip('|').lstrip('|')
    except:
        Grantees=""
    try:
        Applicant_1=driver.find_element_by_xpath("//span[text()='Applicant 1:']/ancestor::table/following-sibling::table[1]/descendant::td[3]").text
    except:
        Applicant_1=""
    try:
        Applicant_2=driver.find_element_by_xpath("//span[text()='Applicant 2:']/ancestor::table/following-sibling::table[1]/descendant::td[3]").text
    except:
        Applicant_2=""
    try:
        Legal_Description=driver.find_element_by_xpath("//span[text()='Legal Description:']/ancestor::table/following-sibling::table[1]/descendant::td[3]").text
    except:
        Legal_Description=""

    dict = {'Book_Type': Book_Type.replace('\n', ''), 'Document_No': Document_No.replace('\n', ''),'Book_No': Book_No.replace('\n', ''),'Page_No': Page_No.replace('\n', ''),
            "Document_Type": Document_Type.replace('\n', ''), 'License_Number':License_Number.replace('\n', ''),
            'Book':Book.replace('\n', ''),'Page':Page.replace('\n', ''), 'Filed_Date':Filed_Date.replace('\n', ''),'Filed_Date_Time':Filed_Date_Time.replace('\n', ''),
            'Marriage_Date':Marriage_Date.replace('\n', '') ,'Instrument_Type': Instrument_Type.replace('\n', ''),'Instrument_Date': Instrument_Date.replace('\n', ''),
            'Grantors': Grantors.replace('\n', ''), 'Grantees': Grantees.replace('\n', ''),'Applicant_1':Applicant_1,'Applicant_2':Applicant_2.replace('\n', ''),
            'Legal_Description': Legal_Description.replace('\n', ''),
            }
    print(dict)
    list.append(dict)
    # time.sleep(3)
    #
    # driver.find_element_by_xpath('''///a[@onclick="navToDocument('next'); return false;"]''')
    # driver.find_element_by_xpath('''///a[@onclick="navToDocument('next'); return false;"]''').click()
    count += 1
    if count >= 24:
        break

    # time.sleep(3)

    driver.switch_to.default_content()
    driver.switch_to.frame("bodyframe")
    driver.switch_to.frame("documentFrame")
    try:
        driver.find_element_by_xpath("//img[@alt='Load Next Document']").click()

        time.sleep(3)
    except:
        break


import pandas_practice as pd
df=pd.DataFrame(list).to_csv('../coleman.csv')

driver.close()
