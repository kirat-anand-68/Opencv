import cv2 as cv
import numpy as np
# Rotate the image

img=cv.imread('Cat2.jpg')

# used for shape recognitaion and
# cv.imshow('Cat',img)
blank=np.zeros(img.shape,dtype='uint8')
# cv.imshow('Blank',blank)


gray=cv.cvtColor(img,cv.COLOR_BGR2GRAY)
# cv.imshow('gray',gray)

# blur=cv.GaussianBlur(gray,(5,5),cv.BORDER_DEFAULT)
# cv.imshow('blur',blur)
# canny=cv.Canny(blur,125,175)
# cv.imshow('canny',canny)

rest,thresh=cv.threshold(gray,125,255,cv.THRESH_BINARY)
# threshold basically binarize the image
cv.imshow('thresh',thresh)

contours,hierarchise=cv.findContours(thresh,cv.RETR_LIST,cv.CHAIN_APPROX_NONE)
# cv.chain retr save the list of adl conyours change 
print(len(contours))

cv.drawContours(blank,contours,-1,(0,0,255),2)
cv.imshow('blank',blank)

cv.waitKey(0)