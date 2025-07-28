import csv
import time
from time import sleep
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import pandas_practice as pd

final_data = []

driver = webdriver.Chrome(executable_path="C:\\Users\\Shibu Naik\\Desktop\\chromedriver.exe")
driver.maximize_window()

driver.get("https://sanbenitocountyca-web.tylerhost.net/web/user/disclaimer")

html = driver.find_element_by_tag_name('html')
html.send_keys(Keys.END)
element = driver.find_element_by_xpath("//button[@id='submitDisclaimerAccept']").click()
time.sleep(5)

element1 = driver.find_element_by_xpath("(//a[@class='ss-action ss-action-form ss-utility-box ss-action-page-search ui-link'])[1]").click()
time.sleep(4)

element_next = driver.find_element_by_xpath("(//a[@class='ss-action ss-action-form ss-utility-box ss-action-page-search ui-link'])[1]").click()
time.sleep(4)

# inserting start and end date
time.sleep(3)

datefield = driver.find_element_by_xpath("(//input[@onblur='selfservice.dateBlurCallback(event)'])[1]")
datefield.click()
datefield.send_keys("06/17/2021")

datefield = driver.find_element_by_xpath("(//input[@onblur='selfservice.dateBlurCallback(event)'])[2]")
datefield.click()
datefield.send_keys("06/17/2021")
time.sleep(3)

html = driver.find_element_by_tag_name('html')
html.send_keys(Keys.END)
time.sleep(2)
element2 = driver.find_element_by_xpath('//a[contains(text(),"Search")]').click()
time.sleep(5)

element3 = driver.find_element_by_xpath('//li[contains(text(),"Recording Date")]')
element3.click()
time.sleep(2)

element4 = driver.find_element_by_xpath('//span[contains(text(),"View")]')
element4.click()
time.sleep(2)


for r in range(1,78):

    try:
        Document_Type = driver.find_element_by_xpath('//li[contains(text(),"Document Type")]/following-sibling::li').text
    except Exception as e:
        print(e)


    Document_Number = driver.find_element_by_xpath('//strong[contains(text(),"Document Number:") ]/../following-sibling::div').text

    Recording_Date = driver.find_element_by_xpath('//strong[contains(text(),"Recording Date:") ]/../following-sibling::div').text

    No_of_Pages = driver.find_element_by_xpath('//strong[contains(text(),"Number Pages:") ]/../following-sibling::div').text

    Book_Type = driver.find_element_by_xpath('(//th[@data-colstart="1"])[2]').text.replace("Book Type", "")

    Book = driver.find_element_by_xpath('(//th[contains(text(),"Book")])[2]').text.replace("Book", "")

    Page = driver.find_element_by_xpath('//th[contains(text(),"Page")]').text.replace("Page", "")

    Grantor_data = []

    Grantor = driver.find_elements_by_xpath('//strong[contains(text(),"Grantor")]/../following-sibling::div')

    for i in Grantor:
        grant = i.text.replace("\n", "|")

        Grantor_data.append(grant)

    Grantee_data = []

    Grantee = driver.find_elements_by_xpath(
        '//strong[contains(text(),"Grantee:")]/../following-sibling::div')

    for i in Grantee:
        grante = i.text.replace("\n", "|")

        Grantee_data.append(grante)

    Related_Document_data = []

    Related_Document = driver.find_elements_by_xpath(
        '//td[@class="related-doc-type truncate"]|//td[@class="related-doc-recording-date elipsis"]|//td[@class="related-doc-external-id truncate"]/a')

    for i in Related_Document:
        RD = i.text.replace("\n", "|")

        Related_Document_data.append(RD)
    try:
        Legal = driver.find_element_by_xpath(
            '//strong[contains(text(),"Assessor Parcel Number:")]/../following-sibling::div').text.replace("\n", "|")
    except: Legal = ""


    dic = {'document_type': '', 'document_no': '', 'recording_date': '', 'no_of_pages': '', 'book_type': '',
           'book': '', 'page': '', 'Grantor': '', 'Grantee': '', 'Related_docs': '', 'legal': ''}

    dic['document_type'] = Document_Type

    dic['document_no'] = Document_Number

    dic['recording_date'] = Recording_Date

    dic['no_of_pages'] = No_of_Pages

    dic['book_type'] = Book_Type

    dic['book'] = Book

    dic['page'] = Page

    str1 = '|'.join(Grantor_data)

    dic['Grantor'] = str1

    str2 = '|'.join(Grantee_data)

    dic['Grantee'] = str2

    str3 = '|'.join(Related_Document_data)

    dic['Related_docs'] = str3

    dic['legal'] = Legal

    final_data.append(dic)

    try:
        Next_doc = driver.find_element_by_xpath('//a[contains(text(),"Next Result")]')
        Next_doc.click()

    except:
        break

    time.sleep(10)



print(final_data)

keys = final_data[0].keys()

a_file = open("TX-Sanbanito-06172021.csv", "w")
dict_writer = csv.DictWriter(a_file, keys)
dict_writer.writeheader()
dict_writer.writerows(final_data)
a_file.close()
