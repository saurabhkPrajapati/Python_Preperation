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

class MadisonSpider(scrapy.Spider):
    name = 'madisonspider'
    start_date = '07/29/2021'
    headers = {'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
               'Accept-Encoding': 'gzip, deflate, br', 'Accept-Language': 'en-US,en;q=0.9', 'Cache-Control': 'max-age=0',
               'Connection': 'keep-alive', 'Host': 'searchiqs.com', 'Referer': 'https://searchiqs.com/NYMAD/Login.aspx',
               'sec-ch-ua': '"Chromium";v="92", " Not A;Brand";v="99", "Google Chrome";v="92"', 'sec-ch-ua-mobile': '?0', 'Sec-Fetch-Dest': 'document',
               'Sec-Fetch-Mode': 'navigate', 'Sec-Fetch-Site': 'same-origin', 'Sec-Fetch-User': '?1', 'Upgrade-Insecure-Requests': '1',
               'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/92.0.4515.107 Safari/537.36'
               }

    def start_requests(self):
        urls = "https://searchiqs.com/NYMAD/Login.aspx"

        yield scrapy.Request(
            url=urls,
            callback=self.parse1,
            headers=self.headers,
            dont_filter=True,
            method="GET"
        )
    #login as guest
    def parse1(self, response):
        # open_in_browser(response)
        viewstate = response.xpath("//input[@id='__VIEWSTATE']/@value").get()
        # eventarget = response.xpath("//input[@id='__EVENTTARGET']/@value").get()
        # viewstategenerator = response.xpath("//input[@id='__VIEWSTATEGENERATOR']/@value").get()
        eventvalidation = response.xpath("//input[@id='__EVENTVALIDATION']/@value").get()

        data = {
             '__EVENTTARGET': 'btnGuestLogin',
             '__VIEWSTATE': viewstate ,
             # '__VIEWSTATE': '/wEPaA8FDzhkOTU1NWVhMGE0ZWQ1M2Rg5WLF1kbeTFUP05cqJp2XQiZ9f/TOKTiadRJfWjjQMQ==',
             '__VIEWSTATEGENERATOR': '15160C5B',
             '__EVENTVALIDATION': eventvalidation ,
             # '__EVENTVALIDATION': '/wEdAAZjNBC+n3NtW7I5Teuf/C/5Zx2+BvjND/pmAi3FDx2Wlgkbq8Q+ob52t63N9IN3E1MqGgLJV0m0siKzkCBhn9Fh7ixyIk7cehzrzFMW1kZASIpVkFeAZD8ZRHRShIYYV00iCinb806FbhB8aQbJenVxFqvHUoB/AkjNfiMp/Lmp2Q==',
             'BrowserWidth': '1329', 'BrowserHeight': '925'
        }
        yield scrapy.FormRequest(
            url="https://searchiqs.com/NYMAD/Login.aspx",
            callback=self.parse2,
            dont_filter=True,
            formdata=data,
            method="POST",
            headers=self.headers,
            meta={'handle_httpstatus_list': [302]}
        )
    # opening searching page
    def parse2(self,response):
        # open_in_browser(response)
        # header = {'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9', 'Accept-Encoding': 'gzip, deflate, br', 'Accept-Language': 'en-US,en;q=0.9', 'Cache-Control': 'max-age=0', 'Connection': 'keep-alive', 'Host': 'searchiqs.com', 'sec-ch-ua': '"Chromium";v="92", " Not A;Brand";v="99", "Google Chrome";v="92"', 'sec-ch-ua-mobile': '?0', 'Sec-Fetch-Dest': 'document', 'Sec-Fetch-Mode': 'navigate', 'Sec-Fetch-Site': 'cross-site', 'Sec-Fetch-User': '?1', 'Upgrade-Insecure-Requests': '1', 'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/92.0.4515.107 Safari/537.36'}
        header = {'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9', 'Accept-Encoding': 'gzip, deflate, br', 'Accept-Language': 'en-US,en;q=0.9', 'Cache-Control': 'max-age=0', 'Connection': 'keep-alive', 'Host': 'searchiqs.com', 'sec-ch-ua': '"Chromium";v="92", " Not A;Brand";v="99", "Google Chrome";v="92"', 'sec-ch-ua-mobile': '?0', 'Sec-Fetch-Dest': 'document', 'Sec-Fetch-Mode': 'navigate', 'Sec-Fetch-Site': 'cross-site', 'Sec-Fetch-User': '?1', 'Upgrade-Insecure-Requests': '1', 'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/92.0.4515.107 Safari/537.36'}

        yield scrapy.Request(
            url="https://searchiqs.com/NYMAD/SearchResultsMP.aspx",
            callback=self.parse3,
            dont_filter=True,
            method="GET",
            # headers=self.headers,
            headers = header,
            meta={'handle_httpstatus_list': [200]}
        )
# searching with document date
    def parse3(self,response):
        # open_in_browser(response)
        header = {'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9', 'Accept-Encoding': 'gzip, deflate, br', 'Accept-Language': 'en-US,en;q=0.9', 'Cache-Control': 'max-age=0', 'Connection': 'keep-alive', 'Content-Type': 'application/x-www-form-urlencoded', 'Host': 'searchiqs.com', 'Origin': 'https://searchiqs.com', 'Referer': 'https://searchiqs.com/NYMAD/SearchAdvancedMP.aspx', 'sec-ch-ua': '"Chromium";v="92", " Not A;Brand";v="99", "Google Chrome";v="92"', 'sec-ch-ua-mobile': '?0', 'Sec-Fetch-Dest': 'document', 'Sec-Fetch-Mode': 'navigate', 'Sec-Fetch-Site': 'same-origin', 'Sec-Fetch-User': '?1', 'Upgrade-Insecure-Requests': '1', 'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/92.0.4515.107 Safari/537.36'}

        viewstate = response.xpath("//input[@id='__VIEWSTATE']/@value").get()
        # eventarget = response.xpath("//input[@id='__EVENTTARGET']/@value").get()
        # viewstategenerator = response.xpath("//input[@id='__VIEWSTATEGENERATOR']/@value").get()
        eventvalidation = response.xpath("//input[@id='__EVENTVALIDATION']/@value").get()
        data = {
            "__EVENTTARGET":"",
            "__EVENTARGUMENT":"",
            "__LASTFOCUS":"",
            '__VIEWSTATE': viewstate,
            # '__VIEWSTATE': '/wEPaA8FDzhkOTU1NWViMDc3ZmMzMxgBBR5fX0NvbnRyb2xzUmVxdWlyZVBvc3RCYWNrS2V5X18WAQUsY3RsMDAkQ29udGVudFBsYWNlSG9sZGVyMSRjaGtJZ25vcmVQYXJ0eVR5cGV1ihJ2v/A4wYwRy/x86mEm5nju7J4GjPGeNek2PK8KEw==',
            '__VIEWSTATEGENERATOR': 'B06333FE',
            '__EVENTVALIDATION': eventvalidation,
            # '__EVENTVALIDATION': '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',
            'ctl00$hidProveH': '0', 'ctl00$hidPageAccessExpire': '-1', 'ctl00$hidAllowCCSave': '0',
            'BrowserWidth': '1326', 'BrowserHeight': '745', 'ctl00$ContentPlaceHolder1$scrollPos': '0',
            'ctl00$ContentPlaceHolder1$chkIgnorePartyType': 'on',
            'ctl00$ContentPlaceHolder1$txtFromDate': '07/01/2021',
            'ctl00$ContentPlaceHolder1$txtThruDate': '07/01/2021',
            'ctl00$ContentPlaceHolder1$cboDocGroup': '(ALL)',
            'ctl00$ContentPlaceHolder1$cboDocType': '(ALL)', 'ctl00$ContentPlaceHolder1$cboTown': '(ALL)',
            'ctl00$ContentPlaceHolder1$cmdSearch': 'Search'
        }

        yield scrapy.FormRequest(
            url="https://searchiqs.com/NYMAD/SearchResultsMP.aspx",
            callback=self.parse4,
            dont_filter=False,
            formdata=data,
            method="POST",
            headers=header,
            meta={'handle_httpstatus_list': [302]}
        )
    def parse4(self,response):
        open_in_browser(response)
        header = {'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
                  'Accept-Encoding': 'gzip, deflate, br', 'Accept-Language': 'en-US,en;q=0.9', 'Cache-Control': 'max-age=0', 'Connection': 'keep-alive', 'Host': 'searchiqs.com', 'Referer': 'https://searchiqs.com/NYMAD/SearchAdvancedMP.aspx', 'sec-ch-ua': '"Chromium";v="92", " Not A;Brand";v="99", "Google Chrome";v="92"', 'sec-ch-ua-mobile': '?0', 'Sec-Fetch-Dest': 'document', 'Sec-Fetch-Mode': 'navigate', 'Sec-Fetch-Site': 'same-origin', 'Sec-Fetch-User': '?1', 'Upgrade-Insecure-Requests': '1', 'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/92.0.4515.107 Safari/537.36'}

        yield scrapy.Request(
            url="https://searchiqs.com/NYMAD/SearchResultsMP.aspx",
            callback=self.parse5,
            dont_filter=True,
            method="GET",
            headers=header,
            meta={'handle_httpstatus_list': [200]}
        )
    def parse5(self,response):
        open_in_browser(response)
    #     print(response.xpath('//*[@id="ContentPlaceHolder1_grdResults_lblParty1_0"]/text()'))
    #     header = {
    #         'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
    #         'Accept-Encoding': 'gzip, deflate, br', 'Accept-Language': 'en-US,en;q=0.9', 'Cache-Control': 'max-age=0',
    #         'Connection': 'keep-alive', 'Host': 'searchiqs.com',
    #         'Referer': 'https://searchiqs.com/NYMAD/SearchAdvancedMP.aspx',
    #         'sec-ch-ua': '"Chromium";v="92", " Not A;Brand";v="99", "Google Chrome";v="92"', 'sec-ch-ua-mobile': '?0',
    #         'Sec-Fetch-Dest': 'document', 'Sec-Fetch-Mode': 'navigate', 'Sec-Fetch-Site': 'same-origin',
    #         'Sec-Fetch-User': '?1', 'Upgrade-Insecure-Requests': '1',
    #         'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/92.0.4515.107 Safari/537.36'}
    #
    #     yield scrapy.Request(
    #         url="https://searchiqs.com/NYMAD/ImageViewerMP.aspx?CustomView=Search%20Results&SelectedDoc=L|1683718&SelectedRowIndex=0",
    #         callback=self.parse6,
    #         dont_filter=True,
    #         method="GET",
    #         headers=header,
    #         meta={'handle_httpstatus_list': [200]}
    #     )
    #
    # def parse6(self, response):
    #     open_in_browser(response)

from scrapy import cmdline
cmdline.execute("scrapy crawl madisonspider".split())