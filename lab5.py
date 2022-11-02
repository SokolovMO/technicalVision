import cv2
import numpy as np
import time

def nothing(x):
    pass

def createTrackbarSobel():
    cv2.namedWindow("conversion parameter")
    cv2.createTrackbar("xorder", "conversion parameter", 0, 2, nothing)
    cv2.createTrackbar("yorder", "conversion parameter", 0, 2, nothing)
    cv2.moveWindow("conversion parameter", 0, 800)
    cv2.resizeWindow("conversion parameter", 500, 50)

def createTrackbarCanny():
    cv2.namedWindow("conversion parameter")
    cv2.createTrackbar("threshold1", "conversion parameter", 0, 255, nothing)
    cv2.createTrackbar("threshold2", "conversion parameter", 0, 255, nothing)
    cv2.moveWindow("conversion parameter", 0, 800)
    cv2.resizeWindow("conversion parameter", 500, 50)

coordPictireX = 0
coordPictireY = 0

# задание 1

pictureNonResize = cv2.imread('lr5/5-2.jpg')
picture = cv2.resize(pictureNonResize, (pictureNonResize.shape[1] // 8, pictureNonResize.shape[0] // 8))

while True:
    cv2.imshow('picture', picture)
    cv2.moveWindow('picture', coordPictireX, coordPictireY)
    if cv2.waitKey(1) == ord('q'):
        break

cv2.destroyAllWindows()

createTrackbarSobel()

while True:
    xorder = int(cv2.getTrackbarPos("xorder", "conversion parameter"))
    yorder = int(cv2.getTrackbarPos("yorder", "conversion parameter"))
    try:
        pictureSobel = cv2.Sobel(picture, cv2.CV_8U, xorder, yorder, ksize=3, scale=1, delta=0)
        cv2.imshow('pictureSobel', pictureSobel)
        cv2.moveWindow('pictureSobel', coordPictireX, coordPictireY)
    except cv2.error:
        cv2.destroyWindow('pictureSobel')
        pass
    if cv2.waitKey(1) == ord('q'):
        break

cv2.destroyAllWindows()

while True:
    pictureLaplacian = cv2.Laplacian(picture, cv2.CV_8U, ksize=3, scale=1, delta=0)
    cv2.imshow('pictureLaplacian', pictureLaplacian)
    cv2.moveWindow('pictureLaplacian', coordPictireX, coordPictireY)
    if cv2.waitKey(1) == ord('q'):
        break

cv2.destroyAllWindows()

createTrackbarCanny()

while True:
    threshold1 = int(cv2.getTrackbarPos("threshold1", "conversion parameter"))
    threshold2 = int(cv2.getTrackbarPos("threshold2", "conversion parameter"))
    pictureCanny = cv2.Canny(picture, threshold1, threshold2, apertureSize=3, L2gradient=False)
    cv2.imshow('pictureCanny', pictureCanny)
    cv2.moveWindow('pictureCanny', coordPictireX, coordPictireY)
    if cv2.waitKey(1) == ord('q'):
        break

cv2.destroyAllWindows()

# задание 2

pictureNonResize = cv2.imread('lr5/5-5.jpg')
picture = cv2.resize(pictureNonResize, (pictureNonResize.shape[1] // 1, pictureNonResize.shape[0] // 1))

while True:
    cv2.imshow('picture', picture)
    cv2.moveWindow('picture', coordPictireX, coordPictireY)
    if cv2.waitKey(1) == ord('q'):
        break

cv2.destroyAllWindows()

createTrackbarCanny()

while True:
    threshold1 = int(cv2.getTrackbarPos("threshold1", "conversion parameter"))
    threshold2 = int(cv2.getTrackbarPos("threshold2", "conversion parameter"))
    pictureCanny = cv2.Canny(picture, threshold1, threshold2, apertureSize=3, L2gradient=False)
    cv2.imshow('pictureCanny', pictureCanny)
    cv2.moveWindow('pictureCanny', coordPictireX, coordPictireY)
    if cv2.waitKey(1) == ord('q'):
        break

cv2.destroyAllWindows()

# задание 3

video = cv2.VideoCapture('lr5/road.MOV')

createTrackbarCanny()

while True:

    try:
        _, pictureNonResize = video.read()
        picture = cv2.resize(pictureNonResize, (pictureNonResize.shape[1] // 2, pictureNonResize.shape[0] // 2))
        picture = cv2.cvtColor(picture, cv2.COLOR_BGR2GRAY)
        time.sleep(0.013)
        threshold1 = int(cv2.getTrackbarPos("threshold1", "conversion parameter"))
        threshold2 = int(cv2.getTrackbarPos("threshold2", "conversion parameter"))
        pictureCanny = cv2.Canny(picture, threshold1, threshold2, apertureSize=3, L2gradient=False)
        cv2.imshow('video', pictureCanny)
        cv2.moveWindow('pictureCanny', coordPictireX, coordPictireY)
        if cv2.waitKey(1) == ord('q'):
            break
    except AttributeError:
        break

cv2.destroyAllWindows()