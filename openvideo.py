import cv2 as cv
# img=cv.imread('tigerimage.jpg')
# cv.imshow('water',img)
# capture=cv.VideoCapture('video1.mp4')
capture=cv.VideoCapture(0)

while True:
    isTrue, frame = capture.read()
    cv.imshow('Video',frame)
    if cv.waitKey(20) & 0xFF == ord('d'):
        break

capture.release()
cv.destroyAllWindows()
