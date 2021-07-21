import cv2
import pytesseract as tess

tess.pytesseract.tesseract_cmd=r'C:\Program Files\Tesseract-OCR\tesseract.exe'

img = cv2.imread("image1.png")
#img = cv2.resize(img, (500, 600))
text=tess.image_to_string(img)

cv2.imshow("OCR",img)
print('\n')
print(text)

cv2.waitKey(0)