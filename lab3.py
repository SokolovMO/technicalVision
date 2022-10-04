import cv2
import numpy as np

def nothing(x):
    pass

p3_1 = cv2.imread('lr3/3-1.PNG')

p3_1resize = cv2.resize(p3_1, (p3_1.shape[1] // 2, p3_1.shape[0] // 2))
p3_1resizeGray = cv2.cvtColor(p3_1resize, cv2.COLOR_BGR2GRAY)
p3_1gray = cv2.cvtColor(p3_1resize, cv2.COLOR_BGR2GRAY)
coordPictireX = 0
coordPictireY = 0

while True:
    cv2.imshow('p3_1', p3_1resize)
    cv2.moveWindow('p3_1', coordPictireX, coordPictireY)
    if cv2.waitKey(1) == ord('q'):
        break

cv2.destroyWindow('p3_1')

cv2.namedWindow("conversion parameter")
cv2.createTrackbar("ksizeX", "conversion parameter", 1, 100, nothing)
cv2.createTrackbar("ksizeY", "conversion parameter", 1, 100, nothing)
cv2.moveWindow("conversion parameter", 0, 800)
cv2.resizeWindow("conversion parameter", 500, 50)

while True:
    ksizeX = int(cv2.getTrackbarPos("ksizeX", "conversion parameter"))
    ksizeY = int(cv2.getTrackbarPos("ksizeY", "conversion parameter"))
    try:
        p3_1blur = cv2.blur(p3_1resize, (ksizeX, ksizeY), cv2.BORDER_DEFAULT)
        cv2.imshow('p3_1blur', p3_1blur)
        cv2.moveWindow('p3_1blur', coordPictireX, coordPictireY)
    except cv2.error:
        pass
    if cv2.waitKey(1) == ord('q'):
        break

cv2.destroyAllWindows()

cv2.namedWindow("conversion parameter")
cv2.createTrackbar("ksizeX", "conversion parameter", 1, 100, nothing)
cv2.createTrackbar("ksizeY", "conversion parameter", 1, 100, nothing)
cv2.moveWindow("conversion parameter", 0, 800)
cv2.resizeWindow("conversion parameter", 500, 50)

while True:
    ksizeX = int(cv2.getTrackbarPos("ksizeX", "conversion parameter"))
    ksizeY = int(cv2.getTrackbarPos("ksizeY", "conversion parameter"))
    try:
        p3_1box = cv2.boxFilter(p3_1resize, -1, (ksizeX, ksizeY), cv2.BORDER_DEFAULT)
        cv2.imshow('p3_1box', p3_1box)
        cv2.moveWindow('p3_1box', coordPictireX, coordPictireY)
    except cv2.error:
        pass
    if cv2.waitKey(1) == ord('q'):
        break

cv2.destroyAllWindows()

cv2.namedWindow("conversion parameter")
cv2.createTrackbar("ksize", "conversion parameter", 1, 100, nothing)
cv2.moveWindow("conversion parameter", 0, 800)
cv2.resizeWindow("conversion parameter", 500, 50)

while True:
    ksize = int(cv2.getTrackbarPos("ksize", "conversion parameter"))
    try:
        p3_1median = cv2.medianBlur(p3_1resize, ksize)
        cv2.imshow('p3_1median', p3_1median)
        cv2.moveWindow('p3_1median', coordPictireX, coordPictireY)
    except cv2.error:
        pass
    if cv2.waitKey(1) == ord('q'):
        break

cv2.destroyAllWindows()

cv2.namedWindow("conversion parameter")

cv2.createTrackbar("ksizeX", "conversion parameter", 1, 50, nothing)
cv2.createTrackbar("ksizeY", "conversion parameter", 1, 50, nothing)
cv2.createTrackbar("sigmaX", "conversion parameter", 1, 10, nothing)
cv2.createTrackbar("sigmaY", "conversion parameter", 1, 10, nothing)

cv2.moveWindow("conversion parameter", 0, 800)
cv2.resizeWindow("conversion parameter", 500, 50)

while True:
    ksizeX = int(cv2.getTrackbarPos("ksizeX", "conversion parameter"))
    ksizeY = int(cv2.getTrackbarPos("ksizeY", "conversion parameter"))
    sigmaX = int(cv2.getTrackbarPos("sigmaX", "conversion parameter"))
    sigmaY = int(cv2.getTrackbarPos("sigmaY", "conversion parameter"))
    try:
        p3_1gaussian = cv2.GaussianBlur(p3_1resize, (ksizeX, ksizeY), sigmaX, sigmaY, cv2.BORDER_DEFAULT)
        cv2.imshow('p3_1gaussian', p3_1gaussian)
        cv2.moveWindow('p3_1gaussian', coordPictireX, coordPictireY)
    except cv2.error:
        pass
    if cv2.waitKey(1) == ord('q'):
        break

cv2.destroyAllWindows()

cv2.namedWindow("conversion parameter")

cv2.createTrackbar("d", "conversion parameter", 1, 50, nothing)
cv2.createTrackbar("sigmaColor", "conversion parameter", 0, 10, nothing)
cv2.createTrackbar("sigmaSpace", "conversion parameter", 0, 10, nothing)

cv2.moveWindow("conversion parameter", 0, 800)
cv2.resizeWindow("conversion parameter", 500, 50)

while True:

    d = int(cv2.getTrackbarPos("d", "conversion parameter"))
    sigmaColor = int(cv2.getTrackbarPos("sigmaColor", "conversion parameter"))
    sigmaSpace = int(cv2.getTrackbarPos("sigmaSpace", "conversion parameter"))
    try:
        p3_1bilatera = cv2.bilateralFilter(p3_1resize, d, sigmaColor, sigmaSpace, cv2.BORDER_DEFAULT)
        cv2.imshow('p3_1bilatera', p3_1bilatera)
        cv2.moveWindow('p3_1bilatera', coordPictireX, coordPictireY)
    except cv2.error:
        pass
    if cv2.waitKey(1) == ord('q'):
        break

cv2.destroyAllWindows()

kernel = np.array([
        [0, -1, 0],
        [-1, 5, -1],
        [0, -1, 0]
])

while True:
    try:
        p3_1filter2D = cv2.filter2D(p3_1resize, -1, kernel)
        cv2.imshow('p3_1filter2D', p3_1filter2D)
        cv2.moveWindow('p3_1filter2D', coordPictireX, coordPictireY)
    except cv2.error:
        pass
    if cv2.waitKey(1) == ord('q'):
        break

cv2.destroyAllWindows()