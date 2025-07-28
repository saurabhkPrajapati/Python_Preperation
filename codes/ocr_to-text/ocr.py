from PIL import Image
import cv2
import pytesseract

# download and instal tesseract and give the tesseract.exe path
pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'

# for unicode error use r'......'
image=Image.open(r'C:\Users\Saurabh prajapati\Downloads\PaperScan_20210519_20210202-000513_0884267_1.tif')
file=open('ocr-1', 'w+')
for i in range(5):
    image.seek(i)


    text_from_image = pytesseract.image_to_string(image)
    file=open('ocr-1', 'a')
    file.write(text_from_image+'\n')


file.close()
