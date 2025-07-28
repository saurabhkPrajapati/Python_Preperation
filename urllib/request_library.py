import requests
headers = {'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/106.0.0.0 Safari/537.36'}
url = 'https://www.programiz.com/python-programming/methods/built-in/classmethod'
response = requests.get(url, headers=headers)
csv_file = open('C:/Users/91880/PycharmProjects/pythonProject/oops/geeks.html', mode='w')
csv_file.write(response.text)
csv_file.close()
response.close()


