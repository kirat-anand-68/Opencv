# countour are boundary of the objects outline or shape of the something
import cv2 as cv
import numpy as np
# Rotate the image

img=cv.imread('Cat2.jpg')

# used for shape recognitaion and
# cv.imshow('Cat',img)

gray=cv.cvtColor(img,cv.COLOR_BGR2GRAY)
cv.imshow('gray',gray)

blur=cv.GaussianBlur(gray,(5,5),cv.BORDER_DEFAULT)
cv.imshow('blur',blur)
canny=cv.Canny(blur,125,175)
cv.imshow('canny',canny)

contours,hierarchise=cv.findContours(canny,cv.RETR_LIST,cv.CHAIN_APPROX_NONE)
# cv.chain retr save the list of all conyours change 
print(len(contours))
cv.waitKey(0)