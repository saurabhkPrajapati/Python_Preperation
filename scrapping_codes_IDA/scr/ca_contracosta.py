#!/usr/bin/env python
# coding: utf-8

import pandas_practice as pd
import glob
import numpy as np
import csv
from datetime import datetime
import re
import os
import shutil

final_list = []

with open(r"D:\\County-Extraction & Conversion\\config\\company_keywords.csv", mode='r') as csv_file:
    csv_reader = csv.reader(csv_file, delimiter=',')
    org_name_list = [i[0] for i in csv_reader]


def check_if_org(name):
    org_name = [i for i in org_name_list if i.lower() in name.lower()]
    return 'ORG' if len(org_name) > 0 else "PERSON"


def create_name(name):
    name_list = name.split(' ')
    if len(name_list) > 0:
        if len(name_list) == 1:
            return name_list[0].strip(), ''
        else:
            return name_list[0].strip(), ' '.join(i for i in name_list[1:])

def split_values(gname, data, key_name, doc_no):
    k_fname, k_lname = key_name.split('/', 1)[0], key_name.split('/', 1)[1]
    data[k_fname] = ''
    data[k_lname] = ''
    #
    if "|" in gname:
        n_list = gname.split("|")
        f_list = []
        l_list = []
        for name in n_list:
            ntype = check_if_org(name)
            if ntype == 'ORG':
                l_list.append(name.replace(",", '').upper())
                f_list.append("")
                continue

            ln, fn = create_name(name)
            if 'the' in fn.lower().strip()[-4:]:
                n_name = "The " + fn.lower().replace('the', '').strip()
            else:
                n_name = fn.strip()

            if ' ee' in fn[-5:].lower():
                n_name = fn.lower().replace(' ee', '').strip()

            if ln:
                if 'the' in ln.lower().strip()[-4:]:
                    l_name = "The " + ln.lower().replace('the', '').strip()
                else:
                    l_name = ln.strip()

                if ' ee' in ln[-5:].lower():
                    l_name = ln.lower().replace(' ee', '').strip()
            else:
                l_name = ''

            l_list.append(l_name.upper())
            f_list.append(n_name.upper())

        data[k_fname] = '|'.join(n for n in f_list)
        data[k_lname] = '|'.join(n for n in l_list)
    else:
        ntype = check_if_org(gname)
        if ntype == 'ORG':
            print(gname)
            data[k_lname] = gname.replace(",", '').upper()
            data[k_fname] = ""
        else:
            ln, fn = create_name(gname)
            if 'the' in fn.lower().strip()[-4:]:
                n_name = "The " + fn.lower().replace('the', '').strip()
            else:
                n_name = fn.strip()

            if ' ee' in fn[-5:].lower():
                n_name = fn.lower().replace(' ee', '').strip()

            if ln:
                if 'the' in ln.lower().strip()[-4:]:
                    l_name = "The " + ln.lower().replace('the', '').strip()
                else:
                    l_name = ln.strip()

                if ' ee' in ln[-5:].lower():
                    l_name = ln.lower().replace(' ee', '').strip()
            else:
                l_name = ''
            data[k_lname] = l_name.upper()
            data[k_fname] = n_name


date = input("Enter the date(mm/dd/yyyy): ")
dates = os.listdir(r'D:\\County-Extraction & Conversion\\Input\\CA-CONTRA COSTA')
if date.replace('/','') in dates:
    filepath = "D:\\County-Extraction & Conversion\\Input\\CA-CONTRA COSTA\\%s\\CA-CONTRA COSTA-%s.csv" %(date.replace('/',''), date.replace('/',''))
    filename = filepath.rsplit("\\", 1)[-1].replace(".csv", '').rsplit('-', 1)[0]

    print(filename)
    df = pd.read_csv(filepath, dtype=str)
    df = df.replace(np.nan, '', regex=True)
    for df_i, df_row in df.iterrows():
        data_dict = {}
        data_dict['COUNTY'] = filename
        d_dict = df.iloc[df_i].to_dict()
        found = False
        with open(r"D:\\County-Extraction & Conversion\\config\\County_conversion.csv", newline='') as csvfile:
            spamreader = csv.reader(csvfile, delimiter=',')
            for i, row in enumerate(spamreader):
                if filename.lower() != row[1].lower():
                    continue
                else:
                    d_dict['FIPS'] = row[0]
                    if i==0:
                        continue
                    if (str(d_dict['FIPS']).strip().lower() == str(row[0]).strip().lower()) and (d_dict['Doc Type'].strip().lower() == row[2].strip().lower()):
                        for k, v in d_dict.items():
                            if k.strip().lower() == row[3].strip().lower():
                                if k == 'Doc Type':
                                    data_dict['MAINDOCTYPE'] = row[-2]
                                else:
                                    data_dict[row[4].strip()] = str(v).strip()

        if len(data_dict.keys()) == 1:
            data_dict['MAINDOCTYPE'] = 'Skip'

        data_dict['DOCUMENT NUMBER'] = d_dict.get('Document Number', '')
        data_dict['RECORDING DATE'] = d_dict.get('Recording Date', '')
        data_dict['FIPS'] = d_dict['FIPS']
        final_list.append(data_dict)

    results = []
    for data in final_list:
        if 'B FNAME MNAME/B LNAME/CORPNAME' in data and data['B FNAME MNAME/B LNAME/CORPNAME']:
            split_values(data['B FNAME MNAME/B LNAME/CORPNAME'], data, 'B FNAME MNAME/B LNAME/CORPNAME',data.get('DOCUMENT NUMBER', '').strip())
        if 'S FNAME MNAME/S LNAME/CORPNAME' in data and data['S FNAME MNAME/S LNAME/CORPNAME']:
            split_values(data['S FNAME MNAME/S LNAME/CORPNAME'], data, 'S FNAME MNAME/S LNAME/CORPNAME', data.get('DOCUMENT NUMBER', '').strip())

        if 'RECORDING DATE' in data and data['RECORDING DATE']:
            try:
                rec_date = re.findall('[0-9]{1,2}/[0-9]{1,2}/[0-9]{4}', data['RECORDING DATE'])
                if len(rec_date) > 0:
                    data['RECORDING DATE'] = rec_date[0]
                data['RECORDING DATE'] = datetime.strptime(data['RECORDING DATE'].strip(), '%m/%d/%Y').strftime("%m%d%Y")
            except:
                continue

        results.append(data)


    df1 = pd.read_excel(r"D:\\County-Extraction & Conversion\\config\\SQL_Headers.xlsx")
    d_dict = df1.to_dict()

    result_list = []
    d_dict = {k: [] for k in d_dict.keys()}
    for data in final_list:
        d = {}
        for key in d_dict.keys():
            if key in data:
                d[key] = data[key]
            else:
                d[key] = ''
        result_list.append(d)

    final_df = pd.DataFrame(result_list)

    # show(final_df, setting={'block': True})
    for cols in final_df.columns:
        try:
            final_df[cols] = final_df[cols].apply(lambda x: str(x).strip())
        except:
            print('float column found')
            pass


    if not os.path.isdir(r"D:\\County-Extraction & Conversion\\Output\\CA-CONTRA COSTA"):
        try:
            os.mkdir(r"..//..//Output//CA-CONTRA COSTA")
        except:
            pass

    if not os.path.isdir(r"D:\\County-Extraction & Conversion\\Output\\CA-CONTRA COSTA\\%s" %date.replace('/','')):
        try:
            os.mkdir(r"..//..//Output//CA-CONTRA COSTA//%s" %date.replace('/',''))
        except:
            pass
    final_df.to_csv(r'D:\\County-Extraction & Conversion\\Output\\CA-CONTRA COSTA\\%s\\output_%s.csv' %(date.replace('/',''), filepath.rsplit("\\", 1)[-1].replace(".csv", '')), index=False)
else:
    print("Input file is not present in the Input folder. Please run the extraction for the above provided date and then start conversion")
