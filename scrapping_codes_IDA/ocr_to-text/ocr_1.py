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
#image = cv2.imread(r'C:\Users\Saurabh prajapati\Downloads\PaperScan_20210519_20210202-000513_0884267_1.tif')

# gray_image = cv2.cvtColor(image,cv2.COLOR_BGR2GRAY)
# threshold_img = cv2.threshold(gray_image,0,255,cv2.THRESH_BINARY|cv2.THRESH_OTSU)[1]
# cv2.imshow('threshold image',threshold_img)
# cv2.waitKey(0)


    text_from_image = pytesseract.image_to_string(image)
    file=open('ocr-1', 'a')
    file.write(text_from_image+'\n')
    # file.close()

file.close()

#
# images=pdf2image.convert_from_path(r'C:\Users\Saurabh prajapati\Downloads\PaperScan_20210519_20210202-000513_0884267_1.tif')
# list=[]
# for i in images:
#     list.append(i)