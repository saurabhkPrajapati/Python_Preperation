# -*- coding: utf-8 -*-
import urllib
import scrapy
from scrapy import Spider
from scrapy.http import Request, FormRequest
from scrapy.utils.response import open_in_browser
import json
import configparser as cp
import re
import csv
import math
from random import randint



class CostaSpider(scrapy.Spider):
    name = 'costa'
    allowed_domains = []
    start_urls = ['https://crsecurepayment.com/RW/?ln=en']


    def random_with_N_digits(self, n):
        range_start = 10**(n-1)
        range_end = (10**n)-1
        return randint(range_start, range_end)

    toCSV = []

    parser = cp.ConfigParser()
    parser.read('config.ini')
    status = str(parser.get("General","status"))
    startdate = str(parser.get("General","startdate"))
    start_doc_num = str(parser.get("General","start_doc_num"))
    str_doc1, sttr_doc2 = start_doc_num.split('-')
    ending_doc_num = str(parser.get("General","ending_doc_num"))
    end_doc1, end_doc2 = ending_doc_num.split('-')

    def parse(self, response):
        if(self.status == "True"):
            for doc in range( int(self.sttr_doc2), int(self.end_doc2)):
                doc = str(self.str_doc1) + "-" + str(doc).zfill(7)  # "-{:02}".format(str(doc))
                # doc = "2021-0068714"
                # print(doc)
                head = {
                    "accept": "*/*",
                    "accept-encoding": "gzip, deflate, br",
                    "accept-language": "en-US,en;q=0.9",
                    "cache-control": "no-cache",
                    "content-type": "application/x-www-form-urlencoded; charset=UTF-8",
                    "origin": "https://crsecurepayment.com",
                    "pragma": "no-cache",
                    "referer": "https://crsecurepayment.com/RW/?ln=en",
                    "sec-fetch-dest": "empty",
                    "sec-fetch-mode": "cors",
                    "sec-fetch-site": "same-origin",
                    "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/89.0.4389.114 Safari/537.36",
                    "x-requested-with": "XMLHttpRequest"
                }
                frmdata = {
                    "FromDocNum": f"{doc}",
                    "ToDocNum": f"{doc}",
                    "ERetrievalGroup": "1",
                    "SearchMode": "2",
                    "IsNewSearch": "true"
                }
                # print(json.dumps(frmdata, indent=4, sort_keys=True))
                yield FormRequest(
                                url="https://crsecurepayment.com/RW/Presentors/AjaxPresentor.aspx",
                                headers = head,
                                method="POST",
                                formdata=frmdata,
                                dont_filter=True,
                                callback=self.send_date)
        else:
            print("\n\n\n\n\t\t\t The status of the script is Failed\n\n\n")


    def send_date(self, response):
        # open_in_browser(response)
        docNum  =  response.xpath('//*[@id="SortedItems"]//tr/td/label/input/@value').extract_first()
        frm_data = {
            "ImgIsPCOR": "False",
            "ImgIsDTT": "False",
            "ImgIsOBIndex": "False",
            "OBBookTab": "",
            "OBBookSeq": "",
            "OBIndexPage": "",
            "OBDocImageBook": "",
            "OBDocImagePage": "",
            "OBDocImageRecYear": "",
            "OBDocImageFormType": "",
            "ImgIsRef": "False",
            "FromBasket": "False",
            "FitToSize": "False",
            "ERetrievalGroup": "1",
            "IsNewSearch": "True",
            "resultsCount": "1",
            "BookFirstPage": "0",
            "docIdIndex": "0",
            "imgIndex": "1",
            "docid": f"{str(docNum)}",
            "ImgIsOBDocImage": "False"
        }
        head = {
            "accept": "*/*",
            "accept-encoding": "gzip, deflate, br",
            "accept-language": "en-US,en;q=0.9",
            "cache-control": "no-cache",
            "content-type": "application/x-www-form-urlencoded; charset=UTF-8",
            "origin": "https://crsecurepayment.com",
            "pragma": "no-cache",
            "referer": "https://crsecurepayment.com/RW/?ln=en",
            "sec-fetch-dest": "empty",
            "sec-fetch-mode": "cors",
            "sec-fetch-site": "same-origin",
            "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/89.0.4389.114 Safari/537.36",
            "x-requested-with": "XMLHttpRequest"
        }
        yield FormRequest(
                        url="https://crsecurepayment.com/RW/Presentors/DetailsPresentor.aspx",
                        headers = head,
                        method="POST",
                        formdata=frm_data,
                        dont_filter=True,
                        callback=self.extract_data)

    def extract_data(self, response):
        # open_in_browser(response)
        doc_num = str(response.xpath('//td[@id="DocumentSpinner1_docNumber"]/text()').extract_first())

        num_pg = ''.join(response.xpath("//td[contains(text(),\"Number of Pages: \")]/following-sibling::td[1]/text()").extract()).replace('\t','').replace('\r','').replace('   ', '')

        recdt = ''.join(response.xpath('//td[contains(text(),"Recording Date: ")]/following-sibling::td[1]/text()').extract_first()).replace('\t','').replace('\r','').replace('   ', '')

        doc_type =  ''.join(response.xpath('//td[@class=" enableHighlight docTypeSelected"]/..//text()').extract()).replace('\t','').replace('\r','').replace('   ', '').replace('\n', ' ')

        # detail = ''.join(response.xpath('//*[@id="subDetailsPanel"]/table//text()').extract()).replace('\t','').replace('\r','').replace('   ', '').replace('\n', '').replace('   ', '')
        detail = ''.join(response.xpath('//*[@id="subDetailsPanel"]/table//text()').extract()).replace('\t','').replace('\r','').replace('   ', '').replace('\n', ' ').replace('   ', ' ')
        # 1 of 0
        detail = detail[23:]
        detail = detail.strip().replace('  ','|')

        grr = '|'.join(response.xpath('//div[@id="Grantors"]//td/text()').extract()).replace('\t','').replace('\r','').replace('   ', '').replace('\n', '').replace('   ', '').replace('||', '').replace('\r\n\t\t\t\t|','')

        gee = '|'.join(response.xpath('//div[@id="Grantees"]//td/text()').extract()).replace('\t','').replace('\r','').replace('   ', '').replace('\n', '').replace('   ', '').replace('||', '').replace('\r\n\t\t\t\t|','')

        # grgtee = '|'.join(response.xpath('//*[@id="GrGrantee"]//text()').extract()).replace('\t','').replace('\r','').replace('   ', '').replace('\n', '').replace('   ', '').replace('||', '').replace('\r\n\t\t\t\t|','')
        #
        # # s[1:] if s.startswith('0') else s
        # if(grgtee.startswith('|')):
        #     grgtee = grgtee[1:]
        # if(grgtee.endswith('|')):
        #     grgtee = grgtee[:-1]

        # shoInfo = ' '.join(response.xpath('//*[@id="Instructions"]//text()').extract())
        # shopInfo_final  = ( shoInfo.replace('Shopping Instructions','').replace('\t','').replace('\r','').replace('   ', '').replace('\n', '').replace('   ', '').replace('Click “Add Document” to purchase this record.Click “Add Current Page” to purchase the current image only.  Frequently Asked Questions', '') if shoInfo else "" )
        out_dict = {
            "Document Number" : doc_num,
            "Num Pages" : num_pg.strip(),
            "Recording Date" : recdt.strip(),
            "Doc Type" : doc_type.strip(),
            "details" : detail.strip(),
            "Grantors" : grr.strip(),
            "Grantees" : gee.strip(),
            # "Grantor/Grantee": grgtee.strip(),
            # "Shopping Instructions": shopInfo_final.strip(),
        }
        # if(":" in detail):
        #     for val in detail.split('|'):
        #         if( "Instrument Number" in val.split(':')[0] or  "Date" in val.split(':')[0] ):
        #             out_dict["ORIGINAL "+val.split(':')[0]] = val.split(':')[1].strip()
        #         else:
        #             out_dict[val.split(':')[0]] = val.split(':')[1].strip()

        # if( ( "Assessors Parcel No" in out_dict ) and ( len(out_dict["Assessors Parcel No"]) == 8 )  ):
        #     out_dict["Assessors Parcel No(8 Digit)"] = out_dict["Assessors Parcel No"][0:3]+ '-' + out_dict["Assessors Parcel No"][3:6] + '-' + out_dict["Assessors Parcel No"][6:8]
        # if( "Tract #" in out_dict ):
        #     out_dict["TRACT NO"] = "TRACT NO "+ str(int(out_dict["Tract #"]))
        # if( "Transfer Tax Amount" in out_dict ):
        #     out_dict["Transfer Tax Amount"] = int( float(out_dict["Transfer Tax Amount"]) * 100 )
        yield out_dict

    def close(self, reason):
        start_time = self.crawler.stats.get_value('start_time')
        finish_time = self.crawler.stats.get_value('finish_time')
        print("Total run time: ", finish_time - start_time)
