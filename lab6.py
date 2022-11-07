import cv2
import numpy as np
import time

def nothing(x):
    pass

def createTrackbarForFindCountoursAndDrawContours():
    cv2.namedWindow("conversion parameter")
    cv2.createTrackbar("method", "conversion parameter", 1, 10, nothing)
    cv2.createTrackbar("contourIdx", "conversion parameter", 1, 10, nothing)
    cv2.createTrackbar("colorB", "conversion parameter", 0, 255, nothing)
    cv2.createTrackbar("colorG", "conversion parameter", 0, 255, nothing)
    cv2.createTrackbar("colorR", "conversion parameter", 0, 255, nothing)
    cv2.createTrackbar("thickness", "conversion parameter", 0, 50, nothing)
    cv2.moveWindow("conversion parameter", 960, 100)

picture = cv2.imread('lr6/picture.png')
picture = cv2.cvtColor(picture, cv2.COLOR_BGR2GRAY)
pictureCopy = picture

createTrackbarForFindCountoursAndDrawContours()

while True:

    contourIdx = int(cv2.getTrackbarPos("contourIdx", "conversion parameter"))
    colorB = int(cv2.getTrackbarPos("colorB", "conversion parameter"))
    colorG = int(cv2.getTrackbarPos("colorG", "conversion parameter"))
    colorR = int(cv2.getTrackbarPos("colorR", "conversion parameter"))
    thickness = int(cv2.getTrackbarPos("thickness", "conversion parameter"))

    contours, hierarchy = cv2.findContours(picture, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
    pictureCopy = cv2.drawContours(pictureCopy, contours, contourIdx, (colorB, colorG, colorR), thickness)
    time.sleep(0.05)
    cv2.imshow('picture', pictureCopy)
    pictureCopy = picture
    cv2.imshow('picture2', picture)
    if cv2.waitKey(1) == ord('q'):
        break