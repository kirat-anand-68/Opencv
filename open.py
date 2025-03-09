import cv2 as cv
img=cv.imread('tigerimage.jpg')
cv.imshow('water',img)
def rescaleFrame(frame,scale=0.75):
    width=int(frame.shape[1]*scale)
    height=int(frame.shape[0]*scale)

    dimensions=(width,height)
    return cv.resize(frame,dimensions,interpolation=cv.INTER_AREA)

resize_image=rescaleFrame(img)
cv.imshow('resize cat',resize_image)
cv.waitKey(0)
"""
capture=cv.VideoCapture('video1.mp4')

while True:
    isTrue, frame = capture.read()
    frame_resized=rescaleFrame(frame)
    cv.imshow('Video',frame)
    cv.imshow('Video resized ',frame_resized)
    if cv.waitKey(20) & 0xFF == ord('d'):
        break

capture.release()
cv.destroyAllWindows()
"""
