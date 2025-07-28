import csv
import os
from scrapy.http import HtmlResponse
import pandas_practice as pd
import urllib
import sqlalchemy
import pyodbc
import sys
from datetime import datetime


class DataExtractor:
    JOBID = ""
    parcel_id = ""
    property_address = ""
    property_use_code = ""
    owner_name = ""
    legal_description = ""
    sales_filepath = ""

    def error_log(self):
        file_object = open("error_log.txt", "a")
        exc_type, exc_obj, exc_tb = sys.exc_info()
        fname = os.path.split(exc_tb.tb_frame.f_code.co_filename)[1]
        print(exc_type, fname, exc_tb.tb_lineno)
        file_object.write(datetime.now().strftime("%d-%m-%y, %H:%M:%S") + ' | ' + "Error: " + str(
            exc_type) + ' | ' + 'Filename: ' + str(fname) + ' | ' + 'Line No: ' + str(
            exc_tb.tb_lineno) + "\n\n")
        file_object.write("----------------------------------------------------------\n\n")


    def __init__(self, response, jobid):
        self.JOBID = jobid
        property = response.xpath('.//table[2]/tbody/tr[1]/td[1]')
        legal_desc = response.xpath('//h4[contains(text(),"Property Desc")]/following-sibling::div/following-sibling::text()[1]').get(default='').strip()
        legal_desc = legal_desc.replace("\n","")
        self.owner_name = '| '.join(i.strip() for i in response.xpath('//h4[text()="Owners"]/../table[1]/tbody/tr/td[1]/text()').getall())
        parcel_id = response.xpath('//h3[contains(text(),"Parcel Details")]/text()').get(default='').strip()
        parcel_id = parcel_id.replace("Parcel Details:"," ")
        self.property_data(property, parcel_id, legal_desc)
        print("data collected")
        sale = response.xpath('.//div/h3[contains(text(),"Sales History")]/../table')
        len(sale)
        if len(sale) != 0:
            self.sale_history(sale)
            df1 = pd.read_csv(self.sales_filepath, header='infer')
            all_data = []
            print(self.owner_name)
            try:
                for i, r in df1.iterrows():
                    jid = self.JOBID
                    stc = "fl_polk_a"
                    sales_date = r["Date"]
                    sales_price = r["Sales Price"]
                    doctype = r["Type Inst"]
                    # instnum = (r["Instrument Number"])
                    instnum = ""
                    # bkpg = str(r["Book"]) + "/" + str(r["Page"])
                    bkpg = str(r["OR Book/Page"])
                    # grantr = r["Grantor"]
                    grantr = ""
                    grantee = r["Grantee"]
                    all_data.append([jid, stc, sales_date, sales_price, doctype, instnum, bkpg, grantr, grantee,])
                df_res = pd.DataFrame(all_data)
                print("started pyodbc sales")
                params = urllib.parse.quote(
                    "Driver={SQL Server};Server=51.81.242.172\DESQL;Database=county_search;UID=sa;PWD=ida@#2021;Trusted_Connection=no;")
                cnxn = sqlalchemy.create_engine("mssql+pyodbc:///?odbc_connect=%s" % params)
                # df = df.fillna('')
                df_res.columns = ['Job ID', 'ST-COUNTY', 'Sales Date', 'Sales Price', 'Doctype', 'Instrument Number',
                                  'Book/Page', 'Grantor', 'Grantee']
                df_res.to_sql("SalesInformation", cnxn, if_exists='append', index=False)
            except Exception as e:
                print(e)
                self.error_log()
                print("started pyodbc error")
                pass

        try:
            print("started pyodbc prop")
            cnxn = pyodbc.connect(
                "Driver={SQL Server};Server=51.81.242.172\DESQL;Database=county_search;UID=sa;PWD=ida@#2021;Trusted_Connection=no;")
            mscursor = cnxn.cursor()
            mscursor.execute("INSERT INTO PropertyInformation VALUES(?,?,?,?,?,?,?)", (self.JOBID, "fl_polk_a", self.parcel_id, self.property_address, self.property_use_code, self.owner_name,self.legal_description))
            mscursor.commit()
        except:
            print("started pyodbc prop error")
            pass

    def property_data(self, data, parcel, description):
        self.outname = "D:/GENERAL_OUTPUT/FL/fl_polk_a/%s/" % self.JOBID + self.JOBID + '_fl_polk_a' +"_Property_Summary.csv"
        if not os.path.exists(self.outname):
            with open(self.outname, "w", newline="") as wd:
                wr = csv.writer(wd)
                wr.writerow(["Parcel ID", "Location", "Brief Tax Description","Property Use","Tax District","Neighbourhood","Subdivision","Community Redevelopment Area","Acreage",])
            wd.close()
        parcel_id = parcel.strip()

        # location = ",".join(i.strip() for i in data.xpath('//h4[text()="Site Address"]/following-sibling::table[1]/tbody/tr/td/span/text()').getall())
        desc = description
        add1 = data.xpath('(.//td[contains(text(),"Address 1")]/following-sibling::td/span)[2]/text()').get(default='').strip()
        add2 = data.xpath('(.//td[contains(text(),"Address 2")]/following-sibling::td/span)[2]/text()').get(default='').strip()
        city = data.xpath('(.//td[contains(text(),"City")]/following-sibling::td/span)/text()').get(default='').strip()
        state = data.xpath('(.//td[contains(text(),"State")]/following-sibling::td/span)/text()').get(default='').strip()
        zip = data.xpath('(.//td[contains(text(),"Zip")]/following-sibling::td/span)/text()').get(default='').strip()
        location = ""
        for i in [add1,add2,city,state,zip]:
            if i != "":
                location = location + ", " + i
                location = location.strip(",")


        prop_use = data.xpath('.//td[contains(text(),"Property (DOR) Use Code")]/following-sibling::td/span/text()').get(default='').strip() +" "+\
        data.xpath('.//td[contains(text(),"Property (DOR) Use Code")]/following-sibling::td/span/a/text()').get(default='').strip()

        sec_twp = ""
        tax_district = data.xpath('.//td[contains(text(),"Taxing District")]/following-sibling::td/span/text()').get(default='').strip()+" " +\
                       data.xpath('.//td[contains(text(),"Taxing District")]/following-sibling::td/span/a/text()').get(default='').strip()
        neighbourhood = data.xpath('.//td[contains(text(),"Neighborhood")]/following-sibling::td/span/text()').get(default='').strip()
        # millege_rate = ""
        acreage = data.xpath('.//td[contains(text(),"Acreage")]/following-sibling::td/span/text()').get(default='').strip()
        subdivision = data.xpath('.//td[contains(text(),"Subdivision")]/following-sibling::td/span/text()').get(default='').strip()
        cra = data.xpath('.//td/a[contains(text(),"Community Redevelopment Area")]/../following-sibling::td/span/text()').get(default='').strip()
        self.parcel_id = parcel_id
        self.property_address = location
        self.legal_description = desc
        self.property_use_code = prop_use

        alldata = [parcel_id, location,desc,prop_use,tax_district,neighbourhood, subdivision, cra, acreage,]
        with open(self.outname, "a", newline="") as wd:
            wr = csv.writer(wd)
            print(alldata)
            wr.writerow(alldata)
            wd.close()


    def sale_history(self, data):
        self.sales_filepath = "D:/GENERAL_OUTPUT/FL/fl_polk_a/%s/" % self.JOBID + self.JOBID + '_fl_polk_a' + f"_TaxInfo_{self.parcel_id}.csv"
        header_data_count = len(data.xpath('tbody/tr[1]/td'))

        thlist = []
        for i in range(1, header_data_count+1):
            trdata = ' '.join([i.strip() for i in data.xpath(f'tbody/tr[1]/td[{i}]/text()').getall()])
            # print(trdata)
            thlist.append(trdata)
        with open(self.sales_filepath, "a", newline="") as wd:
            wr = csv.writer(wd)
            wr.writerow(thlist)
            wd.close()
        tr_count = len(data.xpath('tbody/tr'))
        for j in range(2, tr_count + 1):
            td_count = len(data.xpath(f'tbody/tr[{j}]/td'))
            td_data = []
            for k in range(1, td_count+1):
                if k == 1:
                    tdata = '/'.join(i.strip() for i in data.xpath(f'tbody/tr[{j}]/td[{k}]/span/a/text()').getall())
                elif k == 4 or k == 3:
                    tdata = data.xpath(f'tbody/tr[{j}]/td[{k}]/a/text()').get(default='').strip()
                else:
                    tdata = data.xpath(f'tbody/tr[{j}]/td[{k}]/text()').get(default='').strip()
                td_data.append(tdata)
            with open(self.sales_filepath, "a", newline="") as wd:
                wr = csv.writer(wd)
                print(td_data)
                wr.writerow(td_data)
                wd.close()

