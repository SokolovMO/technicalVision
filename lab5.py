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

def createTrackbar2():
    cv2.namedWindow("conversion parameter")
    cv2.createTrackbar("ksize", "conversion parameter", 0, 7, nothing)
    cv2.createTrackbar("scale", "conversion parameter", 1, 10, nothing)
    cv2.createTrackbar("delta", "conversion parameter", 1, 10, nothing)
    cv2.moveWindow("conversion parameter", 0, 800)
    cv2.resizeWindow("conversion parameter", 500, 50)

def createTrackbar3():
    cv2.namedWindow("conversion parameter")
    cv2.createTrackbar("threshold1", "conversion parameter", 0, 255, nothing)
    cv2.createTrackbar("threshold2", "conversion parameter", 0, 255, nothing)
    cv2.createTrackbar("apertureSize", "conversion parameter", 1, 10, nothing)
    cv2.moveWindow("conversion parameter", 0, 800)
    cv2.resizeWindow("conversion parameter", 500, 50)

pictureNonResize = cv2.imread('lr5/5-1.jpg')
picture = cv2.resize(pictureNonResize, (pictureNonResize.shape[1] // 5, pictureNonResize.shape[0] // 5))

while True:
    cv2.imshow('picture', picture)
    if cv2.waitKey(1) == ord('q'):
        break

cv2.destroyAllWindows()

createTrackbar1()

while True:
    xorder = int(cv2.getTrackbarPos("xorder", "conversion parameter"))
    yorder = int(cv2.getTrackbarPos("yorder", "conversion parameter"))
    ksize = int(cv2.getTrackbarPos("yorder", "conversion parameter"))
    pictureSobel = cv2.Sobel(picture, cv2.CV_8U, xorder, yorder, ksize)
    cv2.imshow('pictureSobel', pictureSobel)
    if cv2.waitKey(1) == ord('q'):
        break

cv2.destroyAllWindows()

createTrackbar2()

while True:
    ksize = int(cv2.getTrackbarPos("ksize", "conversion parameter"))
    scale = int(cv2.getTrackbarPos("scale", "conversion parameter"))
    delta = int(cv2.getTrackbarPos("delta", "conversion parameter"))
    pictureLaplacian = cv2.Laplacian(picture, cv2.CV_8U, ksize, scale, delta)
    cv2.imshow('pictureLaplacian', pictureLaplacian)
    if cv2.waitKey(1) == ord('q'):
        break

cv2.destroyAllWindows()

createTrackbar3()

while True:
    threshold1 = int(cv2.getTrackbarPos("threshold1", "conversion parameter"))
    threshold2 = int(cv2.getTrackbarPos("threshold2", "conversion parameter"))
    apertureSize = int(cv2.getTrackbarPos("apertureSize", "conversion parameter"))
    pictureCanny = cv2.Canny(picture, threshold1, threshold2, apertureSize)
    cv2.imshow('pictureCanny', pictureCanny)
    if cv2.waitKey(1) == ord('q'):
        break

cv2.destroyAllWindows()