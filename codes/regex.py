import re
import os

#file="Number Pages: dfadgfgfagsagsag,"
path=("C:/Users/Saurabh prajapati/Downloads/12031-2021012801")
totalfiles=os.listdir(path) # gives reslut like.....['filedir1','filedir2']
result=[]
count=0
count2=0
count3=0
new=[]
new2=[]
new3=[]
l=[]
m=[]
n4=[]
dict = {}
for i in totalfiles:

    file=open("C:/Users/Saurabh prajapati/Downloads/12031-2021012801/" +i, 'r',encoding="utf8")
    lines=file.readlines()                                                                      #encoding is important
    # dict = {}
    for line in lines:

        match1 = re.search(r"Number Pages:\s(.*)\s",line)
        if match1:
            #print(line)....testing purpose
            Number_Pages=(match1.group(1)).replace(',','')

            n4.append(Number_Pages)
            count+=1

        # match2 = re.search(r"Recorded (.*) PM", line)
        match2 = re.search(r"Recorded(\s*)(.*)(\s*)\s*PM", line)
        if match2:
            # print(line)....testing purpose
            new_value=match2.group(2)+'PM'
            new.append(new_value)
            Recorded =new_value

            count2 += 1

        # else:
        #     Recorded=''

        match3 = re.search(r"BK (\d*)\s", line)
        if match3:
            BK=(match3.group(1))

        match4 = re.search(r"Doc # (\d*)", line)
        if match4:
            Doc = (match4.group(1)).replace(',','')


        match5 = re.search(r"Page (\d*)", line)
        if match5:
            Page = (match5.group(1)).replace(',', '')

        # match6 = re.search(r"RECORDING \$([+-]?([0-9]+([.][0-9]*)?|[.][0-9]+)) ", line)
        match6 = re.search(r"RECORDING \$([+-]?([0-9]+([.][0-9]*)?|[.][0-9]+)) ", line)
        if match6:
            Recording = (match6.group(1)).replace(',', '')
            count3 +=1
        else:
            Recording=''

        # match7 = re.search(r"Parcel ID Number: ([0-9-]+)", line.strip())
        match7 = re.search(r"Parcel ID Number:\s*((\d*)(\s*)(-*)(\s*)(\d*)) ", line)
        if match7:
            Parcel_Id = match7.group(1)
            l.append(file)
            new2.append(Parcel_Id)
        else:
            Parcel_Id= ''

        match8 = re.search(r"LOT\s(\d+)\s", line)
        if match8:
            LOT= match8.group(1)
            m.append(file)
            new3.append(LOT)
        else:
            LOT = ''
        #
    dict = {'Doc':Doc,'BK':BK,'Page':Page,'Number Page':Number_Pages ,'Recorded':Recorded,'Recording':Recording,
            'Parcel_Id ':Parcel_Id,'LOT':LOT }
    result.append(dict)
print(result)
# print(count)
# print(count2)
# print(new)
# print(new2)
print(new3)
print(len(n4),n4)
# import pandas_practice as pd
# #df=pd.DataFrame(result).to_csv('regex_file_1.csv')
# print(m)


