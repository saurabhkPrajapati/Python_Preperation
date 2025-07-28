import os
import glob
import configparser as cp
import csv
import sys, re, pprint
import time
import traceback
from collections import OrderedDict
from more_itertools import unique_everseen
import pandas_practice as pd
import shutil

filename = sys.argv[1]

dt1 = filename.split('-', 2)[2].replace('.csv', '').replace('-', '/')
df = pd.read_csv(filename)
df = df.drop_duplicates(keep='first')
df = df[df['Recording Date']!='Recording Date']
df = df.fillna('')
filename = filename.split('-', 2)[0] + '-' + filename.split('-', 2)[1][:6] + ' ' + filename.split('-', 2)[1][6:] + '-' + \
           filename.split('-', 2)[2].replace('-', '')
df.to_csv(filename, index=False)

# if not os.path.isdir(r"D:\\County-Extraction & Conversion\\Input\\CA-CONTRA COSTA"):
#     try:
#         os.mkdir(r"..//..//Input//CA-CONTRA COSTA")
#     except:
#         pass
#
# if not os.path.isdir(r"D:\\County-Extraction & Conversion\\Input\\CA-CONTRA COSTA\\%s" % dt1.replace('/', '')):
#     try:
#         os.mkdir(r"..//..//Input//CA-CONTRA COSTA//%s" % dt1.replace('/', ''))
#     except:
#         pass
#
# try:
#     shutil.move(r'CA-CONTRA COSTA-%s.csv' % dt1.replace('/', ''),
#                 "D:\\County-Extraction & Conversion\\Input\\CA-CONTRA COSTA\\%s\\" % dt1.replace('/', ''))
# except:
#     pass
