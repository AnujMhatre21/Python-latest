import cv2
from PIL import Image
import pytesseract



im_image = "D:\Python Projects\OCR\data\page1.jpg"

image = cv2.imread(im_image)
cv2.imshow("original image", image) # "original image is like a title"
cv2.waitKey(0) # for much time the image should to be viewed if we put 0 then it will remain open 


# Inverted Image

inverted_image = cv2.bitwise_not(image)
cv2.imwrite ("temp/inverted.jpg",inverted_image)

cv2.imshow("temp/inverted_image.jpg",inverted_image)
cv2.waitKey(0)

# Binarization

def grayscale(image):
    return cv2.cvtColor(image,cv2.COLOR_BGR2GRAY)

gray_image = grayscale(image)
cv2.imwrite ("temp/gray.jpg",gray_image)

cv2.imshow("temp/gray_image.jpg",gray_image)
cv2.waitKey(0)

