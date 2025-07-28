
import json


'''
Overview:

This program is helpful in making the dictionary from the raw_data string 

The process followed is 
1) the string is checked for non emptiness 
2) the string is split :
3) the dictonary is appended with all the key value pairs 





'''





raw_data = '''
accept: */*
accept-encoding: gzip, deflate, br
accept-language: en-US,en;q=0.9
cache-control: no-cache
content-length: 23
content-type: application/x-www-form-urlencoded; charset=UTF-8
cookie: ASP.NET_SessionId=ign0u3dv4m5hak23ztpce5mq; culture=en
origin: https://crsecurepayment.com
pragma: no-cache
referer: https://crsecurepayment.com/RW/?ln=en
sec-ch-ua: "Google Chrome";v="89", "Chromium";v="89", ";Not A Brand";v="99"
sec-ch-ua-mobile: ?0
sec-fetch-dest: empty
sec-fetch-mode: cors
sec-fetch-site: same-origin
user-agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/89.0.4389.114 Safari/537.36
x-requested-with: XMLHttpRequest
'''


data = {}



for ln in raw_data.split('\n'):
    if(len(ln) > 0):
        print(ln.split(': ', 1))
        key_str, val_str = ln.split(': ', 1)
        data[key_str] = val_str


# print(json.dumps(data, indent=4, sort_keys=True))

print(json.dumps(data, indent=4))