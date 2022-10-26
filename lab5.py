import cv2
import numpy as np
import time

def nothing(x):
    pass

def createTrackbar1():
    cv2.namedWindow("conversion parameter")
    cv2.createTrackbar("xorder", "conversion parameter", 1, 10, nothing)
    cv2.createTrackbar("yorder", "conversion parameter", 1, 10, nothing)
    cv2.createTrackbar("ksize", "conversion parameter", 0, 7, nothing)
    cv2.moveWindow("conversion parameter", 0, 800)
    cv2.resizeWindow("conversion parameter", 500, 50)

picture = cv2.imread('lr5/5-1.jpg')

createTrackbar1()

while True:
    xorder = int(cv2.getTrackbarPos("xorder", "conversion parameter"))
    yorder = int(cv2.getTrackbarPos("yorder", "conversion parameter"))
    ksize = int(cv2.getTrackbarPos("yorder", "conversion parameter"))
    pictureSobel = cv2.Sobel(picture, cv2.CV_64F, xorder, yorder, ksize)
    cv2.imshow('pictureSobel', pictureSobel)
    if cv2.waitKey(1) == ord('q'):
        break