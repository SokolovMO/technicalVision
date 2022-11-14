import cv2
import numpy as np
import time

def nothing(x):
    pass

def createTrackbarForFindCountoursAndDrawContours():
    cv2.namedWindow("conversion parameter")
    cv2.createTrackbar("method", "conversion parameter", 1, 10, nothing)
    cv2.createTrackbar("contourIdx", "conversion parameter", 1, 100, nothing)
    cv2.createTrackbar("colorB", "conversion parameter", 0, 255, nothing)
    cv2.createTrackbar("colorG", "conversion parameter", 0, 255, nothing)
    cv2.createTrackbar("colorR", "conversion parameter", 0, 255, nothing)
    cv2.createTrackbar("thickness", "conversion parameter", 0, 50, nothing)
    cv2.moveWindow("conversion parameter", 960, 100)

picture = cv2.imread('lr6/picture.png', cv2.IMREAD_GRAYSCALE)
_, picture = cv2.threshold(picture, 100, 255, cv2.THRESH_BINARY)
pictureCopy = picture
createTrackbarForFindCountoursAndDrawContours()

if __name__ == "__main__":

    while True:

        contourIdx = int(cv2.getTrackbarPos("contourIdx", "conversion parameter"))
        colorB = int(cv2.getTrackbarPos("colorB", "conversion parameter"))
        colorG = int(cv2.getTrackbarPos("colorG", "conversion parameter"))
        colorR = int(cv2.getTrackbarPos("colorR", "conversion parameter"))
        thickness = int(cv2.getTrackbarPos("thickness", "conversion parameter"))

        contours, hierarchy = cv2.findContours(picture, cv2.RETR_LIST, cv2.CHAIN_APPROX_SIMPLE)
        pictureCopy = cv2.drawContours(pictureCopy, contours, contourIdx, (colorB, colorG, colorR), thickness)

        x, y, w, h = cv2.boundingRect(contours)
        cv2.rectangle(pictureCopy, (x, y), (x + w, y + h), (255 - colorB, 255 - colorG, 255 - colorR), thickness)

        cv2.imshow('picture', pictureCopy)
        pictureCopy = cv2.imread('lr6/picture.png')

        if cv2.waitKey(1) == ord('q'):
            break