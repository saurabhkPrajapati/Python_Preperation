# import scrapy
# from scrapy import Request
# from scrapy.http import HtmlResponse
# from scrapy.utils.response import open_in_browser
# import time
# import re
# from selenium import webdriver
# from selenium.webdriver.common.keys import Keys
#
# class Macomb(scrapy.Spider):
#     name = 'macomb'
#
#     def start_requests(self):
#         urls = "https://macombcountymi-web.tylerhost.net/web/user/disclaimer"
#         yield scrapy.Request(
#             url=urls,
#             callback=self.parse,
#             dont_filter=True,
#             method="GET"
#         )
#
#     def parse(self, response):
#         driver = webdriver.Chrome(r'C:\Users\Saurabh prajapati\PycharmProjects\selenium\chromedriver.exe')
#         driver.get(response.url)
#         driver.implicitly_wait(6)
#         driver.find_element_by_xpath("//button[text()='I Accept']").click()
#         driver.find_element_by_xpath("//a[@href='/web/action/ACTIONGROUP95S1']").click()
#         time.sleep(4)
#         driver.find_element_by_xpath("//a[@href='/web/search/DOCSEARCH95S8']").click()
#         time.sleep(4)
#         driver.find_element_by_xpath("//input[@name='field_RecordingDateID_DOT_StartDate']").click()
#         driver.find_element_by_xpath("//input[@name='field_RecordingDateID_DOT_StartDate']").send_keys("01/01/2020")
#         driver.find_element_by_xpath("//input[@name='field_RecordingDateID_DOT_EndDate']").click()
#         driver.find_element_by_xpath("//input[@name='field_RecordingDateID_DOT_EndDate']").send_keys("01/02/2020")
#         time.sleep(4)
#         driver.find_element_by_tag_name('html').send_keys(Keys.PAGE_DOWN)
#         driver.find_element_by_xpath("//a[@href='/web/searchResults/DOCSEARCH., m95S8']").click()
#         # driver.find_element_by_xpath("//a[text()='Search']").click()
#         time.sleep(7)
#         driver.find_element_by_xpath("""(//li[contains(@data-href,"web/document")])[1]""").click()
#         time.sleep(4)
#         # driver.find_element_by_xpath("""(//p[@class='selfServiceSearchFullResult selfServiceSearchResultNavigation'])[1]""").click()
#         # driver.find_element_by_xpath("""(//p[@class='selfServiceSearchFullResult selfServiceSearchResultNavigation'])[71]""").click()
#         # driver.get("https://macombcountymi-web.tylerhost.net/web/document/DOCCLND-2020-2000357-MA?search=DOCSEARCH95S8")
#         driver.find_element_by_xpath("//a[text()='Next']").click()
#         time.sleep(7)
#         driver.find_element_by_xpath("//a[text()='Next']").click()
#         time.sleep(7)
#         while True:
#             response=HtmlResponse(url='https://www.example.com',body=driver.page_source.encode('utf-8'))
#             Document_Type = response.xpath("//li[contains(text(),'Document Type')]/following-sibling::li/text()").get(
#                 default='')
#             Document_Number = response.xpath(
#                 "//strong[contains(text(),'Document Number')]/../following-sibling::div/text()").get(default='')
#             Recording_Date = response.xpath(
#                 "//strong[contains(text(),'Recording Date:')]/../following-sibling::div/text()").get(default='')
#             Number_Pages = response.xpath("//strong[contains(text(),'Number Pages')]/../following-sibling::div/text()").get(
#                 default='')
#             Recording_Fee = response.xpath(
#                 "//strong[contains(text(),'Recording Fee')]/../following-sibling::div/text()").get(default='')
#             # Liber=response.xpath("(//tr/td/b[text()='Liber'])[1]/../text()").get()
#             Liber=''
#             for i in range(1,30):
#                 lb = response.xpath(f"(//b[contains(text(),'Liber')]){[i]}/following-sibling::text()").get(default='')
#
#                 # if lb != "":
#                 Liber = Liber + "|" + lb
#                 Liber = Liber.strip().strip("|")
#
#             Page = ''
#             for i in range(1, 30):
#                 lb = response.xpath(f"(//b[contains(text(),'Page')])[{i}]/following-sibling::text()").get(default='')
#
#                 if lb != "":
#                     Page = Page + "|" + lb
#                     Page = Page.strip().strip("|")
#
#             Grantor1 = response.xpath(
#                 "//strong[contains(text(),'Grantor')]/../following-sibling::div/text()").get(default='')
#
#             Grantor2 = ""
#             for i in range(1, 10):
#                 gn = response.xpath(
#                     f"//strong[contains(text(),'Grantor')]/../following-sibling::div/ul/li[{i}]/text()").get(
#                     default='')
#                 if gn != " ":
#                     Grantor2 = Grantor2 + "|" + gn
#                     Grantor2 = Grantor2.strip().strip("|")
#             Grantor = Grantor1 + Grantor2
#
#             Grantee_Notation1 = response.xpath(
#                 "//strong[contains(text(),'Grantee/Notation')]/../following-sibling::div/text()").get(default='')
#             Grantee_Notation2 = ""
#             for i in range(1, 10):
#                 gn = response.xpath(
#                     f"//strong[contains(text(),'Grantee/Notation')]/../following-sibling::div/ul/li[{i}]/text()").get(
#                     default='')
#                 Grantee_Notation2 = Grantee_Notation2 + "|" + gn
#                 Grantee_Notation2 = Grantee_Notation2.strip().strip("|")
#             Grantee_Notation = Grantee_Notation1 + Grantee_Notation2
#             Parcel = response.xpath("//div[contains(text(),'Parcel')]/text()").get(default='')
#             Property = response.xpath("//div[contains(text(),'property')]/text()").get(default='')
#             Legal = ''
#             for i in range(6):
#                 tt = response.xpath(f"((//ul[contains(@class,'ui-unbulleted-list')])[2]/li){[i]}/text()").get(
#                     default='')
#                 Legal = Legal + "|" + tt
#                 Legal = Legal.strip().strip("|")
#
#             Legal = Parcel + "|" + Property + "|" + Legal
#             Legal = Legal.strip("|")
#             Related1= response.xpath("//td[@class='related-doc-type truncate']/text()").get(default='')
#             Related2= response.xpath("//td[@class='related-doc-recording-date elipsis']/text()").get(default='')
#             Related3= response.xpath("//td[@class='related-doc-external-id truncate']/a/text()").get(default='')
#             Related41= response.xpath("//*[@id='relatedDataCollapsible']/div/div[2]/div[2]/div[1]/text()[1]").get(default='')
#             Related42= response.xpath("//*[@id='relatedDataCollapsible']/div/div[2]/div[2]/div[1]/text()[2]").get(default='')
#             Related43= response.xpath("//*[@id='relatedDataCollapsible']/div/div[2]/div[2]/div[1]/text()[3]").get(default='')
#             Related44= response.xpath("//*[@id='relatedDataCollapsible']/div/div[2]/div[2]/div[1]/text()[4]").get(default='')
#             Related45= response.xpath("//*[@id='relatedDataCollapsible']/div/div[2]/div[2]/div[1]/text()[5]").get(default='')
#             Related51= response.xpath("//*[@id='relatedDataCollapsible']/div/div[2]/div[2]/div[2]/text()[1]").get(default='')
#             Related52= response.xpath("//*[@id='relatedDataCollapsible']/div/div[2]/div[2]/div[2]/text()[2]").get(default='')
#             Related53= response.xpath("//*[@id='relatedDataCollapsible']/div/div[2]/div[2]/div[2]/text()[3]").get(default='')
#             Related54= response.xpath("//*[@id='relatedDataCollapsible']/div/div[2]/div[2]/div[2]/text()[4]").get(default='')
#             Related55= response.xpath("//*[@id='relatedDataCollapsible']/div/div[2]/div[2]/div[2]/text()[5]").get(default='')
#             # Related=Related1+"|"+Related2+"|"+Related3+"|"+Related41+"|"+Related42+"|"+Related43+"|"+
#             Related=''
#             for i in [Related1,Related2,Related3,Related41,Related42,Related43,Related44,Related45,Related51,Related52,Related53,Related54,Related55]:
#                 if i !='':
#                     Related=Related+"|"+i
#                     Related=Related.strip().strip("|")
#             Document_Date = response.xpath("//strong[text()='Document Date:']/../following-sibling::div/text()").get(default='')
#
#
#             yield {
#                 "Document Number": Document_Number,
#                 "Document Type": Document_Type.strip('\n\t'),
#                 "Recording Date": Recording_Date,
#                 "Number Pages": Number_Pages,
#                 "Recording Fees": Recording_Fee,
#                 "Liber": Liber,
#                 "Page": Page,
#                 "Grantor": Grantor.replace('\n', ''),
#                 "Grantee/Notation": Grantee_Notation.replace('\n', ''),
#                 "Legal":Legal,
#                 "Related Documents":Related.replace('\n', '').replace('\t', ''),
#                 "Document date":Document_Date.replace('\n', '').replace('\t', ''),
#
#             }
#             time.sleep(3)
#             try:
#                 driver.find_element_by_xpath("""//a[contains(text(),'Next Result') and contains(@data-inline,'true')]""").click()
#                 time.sleep(5)
#             except:
#                 break
#
#
#
#
#
#
# from scrapy.cmdline import execute
# execute('scrapy crawl macomb -o MI-01-02-2021.csv '.split())
# # -o MI-06-18-2021.csv