import scrapy
from scrapy.utils.response import open_in_browser


class AdairSpider(scrapy.Spider):
    name = 'adair'
    allowed_domains = []
    headers= {'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.101 Safari/537.36'}

    def start_requests(self):
        yield scrapy.Request(
            url="https://okcountyrecords.com/",
            callback=self.parse,
            headers=self.headers,
            dont_filter=True
        )
    def parse(self, response):
        open_in_browser(response)


        yield scrapy.Request(
            url="https://okcountyrecords.com/search/adair",
            callback=self.parse1,
            headers=self.headers,
            method='GET',
            dont_filter=True,
        )

    def parse1(self, response):
        header = {
            ":authority": "okcountyrecords.com",
            ":method": "GET",
            ":path": "/results/recorded-start=2021-06-05:recorded-end=2021-06-11:site=adair/page-1",
            ":scheme": "https",
            "accept - encoding": "gzip,deflate,br",
            "accept - language": "en - US,en;",

            "User-Agent": "Mozilla/5.0 (Windows NT 6.3; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.77 Safari/537.36",
        }
        for i in range(7):
            yield scrapy.Request(
            url=f"https://okcountyrecords.com/results/recorded-start=2021-06-01:recorded-end=2021-06-02:site=adair/page-{i}",
                                            # "/results/recorded-start=2021-06-03:recorded-end=2021-06-10:site=adair/page-2"
            callback=self.parse2,
            headers=header,
            method='GET',
            dont_filter=True,

        )

    def parse2(self, response):
        # total = response.xpath("//td[@class='optional nowrap']/a[starts-with(@href, '/detail/adair/')]").getall()
        total=response.xpath("//td[@class='optional nowrap']//a[starts-with(@href, '/detail/adair/')]/text()").getall()
        header = {
            "Accept":"text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9",
            "Accept-Encoding": "gzip,deflate,br",
            "Accept-Language": "en - US,en;",
            "Connection": "keep-alive",
            "Host": "okcountyrecords.com",
            "User-Agent": "Mozilla/5.0 (Windows NT 6.3; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.77 Safari/537.36",
        }
        for i in total:
            yield scrapy.FormRequest(
            # url="https://okcountyrecords.com/detail/adair/2021-001954/",
            url=f"https://okcountyrecords.com/detail/adair/{i}/",
            callback=self.parse3,
            headers=header,
            method='GET',
            dont_filter=True,
        )
    def parse3(self,response):
        Intrument_No= response.xpath("(//th[contains(text(),'Instrument')])[1]/following-sibling::td/text()").get().strip()
        Book = response.xpath('//th[contains(text(),"Book")]/following-sibling::td/text()').get(default='').strip()

        Page = response.xpath('//th[contains(text(),"Page")]/following-sibling::td/text()').get(default='').strip()

        Recorded_date = response.xpath('//th[contains(text(),"Recorded")]/following-sibling::td/text()').get(default='').strip()

        Recorded_on = response.xpath('//th[contains(text(),"Recorded on")]/following-sibling::td/text()').get( default='').strip()

        Instrument_date = response.xpath('//th[contains(text(),"Instrument date")]/following-sibling::td/text()').get( default='').strip()

        Grantors = '|'.join(i.strip() for i in response.xpath(
            "(//span[contains(text(),'Grantor')]/following-sibling::ul/li/text())[position() =2 or position()=4 or position() = 6 or  position() =8 or position() =10 or position() =12]").getall()
                            if i != '')

        Grantees = '|'.join(i.strip() for i in response.xpath(
            "(//span[contains(text(),'Grantor')]/following-sibling::ul/li/text())[position() =2 or position()=4 or position() = 6 or  position() =8 or position() =10 or position() =12]").getall()
                            if i != '')

        Legal_desc = '|'.join(i.strip() for i in response.xpath(
            "(//h2[contains(text(),'Legal Description')]/following-sibling::ul/li/text())[position() =2 or position()=4 or position() = 6 or  position() =8 or position() =10 or position() =12]").getall()
                              if i != '')

        yield {"Inst_no": Intrument_No,
               "Book": Book,
               "Page": Page,
               "Recorded_date": Recorded_date,
               "Recorded_on": Recorded_on,
               "Instrument_date": Instrument_date,
               "Grantors": Grantors,
               "Grantees": Grantees,
               "Legal_desc": Legal_desc,
               }
