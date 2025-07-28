import scrapy
from scrapy.http import headers
from scrapy.utils.response import open_in_browser


class Nse(scrapy.Spider):
    #enter your symbol here
    symbol="ADANIPORTS"
    # enter your expirydate here like 26-Aug-2021, 29-Jul-2021, 30-Sep-2021
    expirydate = "30-Sep-2021"
    name = 'nse'
    headers = {
        'accept': '*/*', 'accept-encoding': 'gzip, deflate, br', 'accept-language': 'en-US,en;q=0.9',
         'referer': 'https://www.nseindia.com/option-chain',
         'sec-ch-ua': '" Not;A Brand";v="99", "Google Chrome";v="91", "Chromium";v="91"', 'sec-ch-ua-mobile': '?0',
         'sec-fetch-dest': 'empty', 'sec-fetch-mode': 'cors', 'sec-fetch-site': 'same-origin',
         'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36'
    }

    def start_requests(self):
        urls = "https://www.nseindia.com/option-chain"

        yield scrapy.Request(
            url=urls,
            callback=self.parse1,
            headers=self.headers,
            dont_filter=True,
            method="GET"
        )
    def parse1(self, response):
        # open_in_browser(response)
        yield scrapy.Request(
            url=f"https://www.nseindia.com/api/option-chain-equities?symbol={self.symbol}",
            callback=self.parse2,
            dont_filter=True,
            method="GET",
            headers=self.headers,
            # meta={'handle_httpstatus_list': [304]}
        )

    def parse2(self, response):
        # open_in_browser(response)
        res=response.json()

        # print(res)
        # yield{
        #     "a":res['records']['data'][0]['PE']
        # }
        for i in res['records']['data']:
            if self.expirydate == i['expiryDate']:
                STRIKE_PRICE=i['strikePrice']
                if 'CE' in i.keys():
                    C_IO=i['CE']['openInterest']
                    # C_IO=i.get('CE','0')['openInterest']
                    C_CHNG_IN_OI=i['CE']['changeinOpenInterest']
                    C_VOLUME=i['CE']['totalTradedVolume']
                    C_IV=i['CE']['impliedVolatility']
                    C_LTP=i['CE']['lastPrice']
                    C_CHNG=i['CE']['change']
                    C_BID_QTY=i['CE']['bidQty']
                    C_BID_PRICE=i['CE']['bidprice']
                    C_ASK_PRICE=i['CE']['askPrice']
                    C_ASK_QTY=i['CE']['askQty']
                    C_STRIKE_PRICE=i['CE']['strikePrice']
                else:
                    C_IO ='0'
                    # C_IO=i.get('CE','0')['openInterest']
                    C_CHNG_IN_OI = '0'
                    C_VOLUME = '0'
                    C_IV = '0'
                    C_LTP = '0'
                    C_CHNG = '0'
                    C_BID_QTY = '0'
                    C_BID_PRICE ='0'
                    C_ASK_PRICE = '0'
                    C_ASK_QTY = '0'
                    C_STRIKE_PRICE = '0'

                if 'PE' in i.keys():


                    P_STRIKE_PRICE = i['PE']['strikePrice']
                    P_BID_QTY=i['PE']['bidQty']
                    P_BID_PRICE=i['PE']['bidprice']
                    P_ASK_PRICE = i['PE']['askPrice']
                    P_ASK_QTY=i['PE']['askQty']
                    P_CHNG=i['PE']['change']
                    P_LTP = i['PE']['lastPrice']
                    P_IV=i['PE']['impliedVolatility']
                    P_VOLUME = i['PE']['totalTradedVolume']
                    P_CHNG_IN_OI = i['PE']['changeinOpenInterest']
                    P_IO = i['PE']['openInterest']
                else:

                    P_STRIKE_PRICE = '0'
                    P_BID_QTY = '0'
                    P_BID_PRICE = '0'
                    P_ASK_PRICE = '0'
                    P_ASK_QTY ='0'
                    P_CHNG = '0'
                    P_LTP = '0'
                    P_IV = '0'
                    P_VOLUME = '0'
                    P_CHNG_IN_OI = '0'
                    P_IO = '0'

                yield{

                       "IO":C_IO,
                       "CHNG IN OI":C_CHNG_IN_OI
                       ,'VOLUME':C_VOLUME,
                       'IV':C_IV,
                       "LTP":C_LTP,
                       "CHNG":C_CHNG,
                       'BID QTY':C_BID_QTY,
                       "BID_PRICE":C_BID_PRICE,
                       "ASK PRICE": C_ASK_PRICE,
                       "ASK_QTY":  C_ASK_QTY,
                       # "STRIKE PRICE":C_STRIKE_PRICE,


                        "STRIKE PRICE":STRIKE_PRICE,



                        # "STRIKE PRICE": P_STRIKE_PRICE,
                        ' BID QTY': P_BID_QTY,
                        " BID_PRICE": P_BID_PRICE,
                        " ASK_QTY": P_ASK_QTY,
                        " ASK PRICE": P_ASK_PRICE,
                        " CHNG": P_CHNG,
                        " LTP": P_LTP,
                        ' IV': P_IV,
                        ' VOLUME': P_VOLUME,
                        " CHNG IN OI": P_CHNG_IN_OI,
                        " IO": C_IO,
                }

                # yield{
                #    'CALLS':{
                #        "IO":C_IO,
                #        "CHNG IN OI":C_CHNG_IN_OI
                #        ,'VOLUME':C_VOLUME,
                #        'IV':C_IV,
                #        "LTP":C_LTP,
                #        "CHNG":C_CHNG,
                #        'BID QTY':C_BID_QTY,
                #        "BID_PRICE":C_BID_PRICE,
                #        "ASK PRICE": C_ASK_PRICE,
                #        "ASK_QTY":  C_ASK_QTY,
                #        # "STRIKE PRICE":C_STRIKE_PRICE,
                #    },
                #     ' ':{
                #         "STRIKE PRICE":STRIKE_PRICE
                #     },
                #
                #     "PUTS":{
                #         # "STRIKE PRICE": P_STRIKE_PRICE,
                #         'BID QTY': P_BID_QTY,
                #         "BID_PRICE": P_BID_PRICE,
                #         "ASK_QTY": P_ASK_QTY,
                #         "ASK PRICE": P_ASK_PRICE,
                #         "CHNG": P_CHNG,
                #         "LTP": P_LTP,
                #         'IV': P_IV,
                #         'VOLUME': P_VOLUME,
                #         "CHNG IN OI": P_CHNG_IN_OI,
                #         "IO": C_IO,
                #
                #     }
                #
                # }




from scrapy.cmdline import execute
execute('scrapy crawl nse -o sherin.csv'.split())
