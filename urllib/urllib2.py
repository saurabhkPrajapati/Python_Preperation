import urllib.request as request

url = 'https://officialrecords.broward.org/AcclaimWeb/Image/DocumentPdfAllPages/LgDZxtd1VKYuPz08S3oBwCHUiCcMs1cF9FXO0jKjXQvutTcpLMuRTHVxDhVPtkl5'
pdf_path = 'C:/Users/91880/PycharmProjects/pythonProject/oops/broward.pdf'

response = request.urlopen(url)
data = response.read()
with open(pdf_path, mode='wb') as file_name:
    file_name.write(data)
request.urlcleanup()
