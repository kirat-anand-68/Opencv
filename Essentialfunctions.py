import cv2 as cv
img=cv.imread('Cat2.jpg')

# cv.imshow('Cat',img)


#converting image to grayscale
gray= cv.cvtcolor(img,cv.COLOR_BGR2GRAY)
# # cv.imshow('Gray',gray)
# # BLUR
blur=cv.GaussianBlur(img,(7,7),cv.BORDER_DEFAULT)
# cv.imshow('blur',blur)
# #EDGE CAscade
canny =cv.Canny(img,125,175)
# cv.imshow('canny',canny)

#Dilating the image
dilated=cv.dilate(canny,(3,3),iterations=1)
# cv.imshow('Dilated',dilated)

#REsize 
resize=cv.resize(img,(500,500))
cv.imshow('RESIZE',resize)
#CRAOPPING

cropped=img[50:200,200:400]
cv.imshow('Cropped',cropped)

cv.waitKey(0)

