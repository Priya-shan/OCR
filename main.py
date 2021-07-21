import cv2
from pytesseract import pytesseract

pytesseract.tesseract_cmd=r'C:\Program Files\Tesseract-OCR\tesseract.exe'
img = cv2.imread("image1.png")
#img = cv2.resize(img, (500, 600))
image_data = pytesseract.image_to_data(img,output_type=pytesseract.Output.DICT)

for i, word in enumerate(image_data['text']):
    if word !="":
        x,y,w,h=image_data['left'][i],image_data['top'][i],image_data['width'][i],image_data['height'][i]
        cv2.rectangle(img,(x,y),(x+w,y+h),(0,255,0),3)
        cv2.putText(img,word,(x,y-16),cv2.FONT_HERSHEY_COMPLEX,1,(0,0,255))

cv2.imshow("OCR",img)
cv2.waitKey(0)
