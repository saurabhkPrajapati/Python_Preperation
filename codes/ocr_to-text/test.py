import os
import re
import pandas_practice as pd

# file="Number Pages: dfadgfgfagsagsag,"
path = ("C:/Users/Saurabh prajapati/Downloads/New folder")
totalfiles = os.listdir(path)  # gives reslut like.....['filedir1','filedir2']
result = []

dict = {}
for i in totalfiles:

    file = open("C:/Users/Saurabh prajapati/Downloads/New folder/" + i, 'r', encoding="cp1252")
    # utf-8' codec can't decode byte 0x92 in position 109: invalid start byte...use this encoding="cp1252"
    lines = file.readlines()  # encoding is important
    for line in lines:
        match1 = re.search(r"Office File Number\s*:\s*(\d*-\d*)\s", line)
        if match1:
            # print(line)....testing purpose
            Office_File_Number = (match1.group(1)).replace(',', '')

        # match2 = re.search(r"Recorded (.*) PM", line)
        match2 = re.search(r"Policy Number\s*:\s*(.*)\s", line)
        if match2:
            # print(line)....testing purpose
            Policy_Number = match2.group(1)

        match3 = re.search(r"^(Policy Date)\s*:\s*(.*)(P.M.)$", line)
        if match3:
            Policy_Date = (match3.group(2))

        match4 = re.search(r"olicy Amount\s*:\s*\$(\d*,\d*,\d*.\d*)", line)
        if match4:
            Policy_Amount = (match4.group(1)).replace(',', '')

        #
    dict = {'Office File Number': Office_File_Number, 'Policy Number': Policy_Number, 'Policy Date': Policy_Date,
            'Policy Amount': Policy_Amount,
            }
    result.append(dict)
print(result)

#converting to csv
df=pd.DataFrame(result).to_csv('filename.csv')

