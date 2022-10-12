import cv2
import numpy as np

def nothing(x):
    pass

p3_1 = cv2.imread('lr3/3-1.PNG')
p3_1resize = cv2.resize(p3_1, (p3_1.shape[1] // 3, p3_1.shape[0] // 3))
p3_1resizeGray = cv2.cvtColor(p3_1resize, cv2.COLOR_BGR2GRAY)

p3_2 = cv2.imread('lr3/3-2.PNG')
p3_2resize = cv2.resize(p3_2, (p3_2.shape[1] // 3, p3_2.shape[0] // 3))
p3_2resizeGray = cv2.cvtColor(p3_2resize, cv2.COLOR_BGR2GRAY)

p3_3 = cv2.imread('lr3/3-3.PNG')
p3_3resize = cv2.resize(p3_3, (p3_3.shape[1] // 3, p3_3.shape[0] // 3))
p3_3resizeGray = cv2.cvtColor(p3_3resize, cv2.COLOR_BGR2GRAY)

p3_4 = cv2.imread('lr3/3-4.PNG')
p3_4resize = cv2.resize(p3_4, (p3_4.shape[1] // 3, p3_4.shape[0] // 3))
p3_4resizeGray = cv2.cvtColor(p3_4resize, cv2.COLOR_BGR2GRAY)

coordPictireX = 0
coordPictireY = 0

##################################################################### 1

while True:

    cv2.imshow('p3_1', p3_1resize)
    cv2.imshow('p3_1gray', p3_1resizeGray)
    cv2.imshow('p3_2', p3_2resize)
    cv2.imshow('p3_2gray', p3_2resizeGray)

    cv2.moveWindow('p3_1', coordPictireX, coordPictireY)
    cv2.moveWindow('p3_1gray', p3_1resize.shape[1], coordPictireY)
    cv2.moveWindow('p3_2', 2*p3_1resize.shape[1], coordPictireY)
    cv2.moveWindow('p3_2gray', 2 * p3_1resize.shape[1] + p3_2resize.shape[1], coordPictireY)

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

        p3_1blur = cv2.blur(p3_1resize, (ksizeX, ksizeY), cv2.BORDER_DEFAULT)
        p3_2blur = cv2.blur(p3_2resize, (ksizeX, ksizeY), cv2.BORDER_DEFAULT)
        p3_1blurGray = cv2.blur(p3_1resizeGray, (ksizeX, ksizeY), cv2.BORDER_DEFAULT)
        p3_2blurGray = cv2.blur(p3_2resizeGray, (ksizeX, ksizeY), cv2.BORDER_DEFAULT)
        cv2.imshow('p3_1blur', p3_1blur)
        cv2.imshow('p3_2blur', p3_2blur)
        cv2.imshow('p3_1blurGray', p3_1blurGray)
        cv2.imshow('p3_2blurGray', p3_2blurGray)
        cv2.moveWindow('p3_1blur', coordPictireX, coordPictireY)
        cv2.moveWindow('p3_1blurGray', p3_1resize.shape[1], coordPictireY)
        cv2.moveWindow('p3_2blur', 2 * p3_1resize.shape[1], coordPictireY)
        cv2.moveWindow('p3_2blurGray', 2 * p3_1resize.shape[1] + p3_2resize.shape[1], coordPictireY)

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
        p3_2box = cv2.boxFilter(p3_2resize, -1, (ksizeX, ksizeY), cv2.BORDER_DEFAULT)
        p3_1boxGray = cv2.boxFilter(p3_1resizeGray, -1, (ksizeX, ksizeY), cv2.BORDER_DEFAULT)
        p3_2boxGray = cv2.boxFilter(p3_2resizeGray, -1, (ksizeX, ksizeY), cv2.BORDER_DEFAULT)
        cv2.imshow('p3_1box', p3_1box)
        cv2.imshow('p3_2box', p3_2box)
        cv2.imshow('p3_1boxGray', p3_1boxGray)
        cv2.imshow('p3_2boxGray', p3_2boxGray)
        cv2.moveWindow('p3_1box', coordPictireX, coordPictireY)
        cv2.moveWindow('p3_1boxGray', p3_1resize.shape[1], coordPictireY)
        cv2.moveWindow('p3_2box', 2 * p3_1resize.shape[1], coordPictireY)
        cv2.moveWindow('p3_2boxGray', 2 * p3_1resize.shape[1] + p3_2resize.shape[1], coordPictireY)

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
        p3_2median = cv2.medianBlur(p3_2resize, ksize)
        p3_1medianGray = cv2.medianBlur(p3_1resizeGray, ksize)
        p3_2medianGray = cv2.medianBlur(p3_2resizeGray, ksize)
        cv2.imshow('p3_1median', p3_1median)
        cv2.imshow('p3_2median', p3_2median)
        cv2.imshow('p3_1medianGray', p3_1medianGray)
        cv2.imshow('p3_2medianGray', p3_2medianGray)
        cv2.moveWindow('p3_1median', coordPictireX, coordPictireY)
        cv2.moveWindow('p3_1medianGray', p3_1resize.shape[1], coordPictireY)
        cv2.moveWindow('p3_2median', 2 * p3_1resize.shape[1], coordPictireY)
        cv2.moveWindow('p3_2medianGray', 2 * p3_1resize.shape[1] + p3_2resize.shape[1], coordPictireY)

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
        p3_2gaussian = cv2.GaussianBlur(p3_2resize, (ksizeX, ksizeY), sigmaX, sigmaY, cv2.BORDER_DEFAULT)
        p3_1gaussianGray = cv2.GaussianBlur(p3_1resizeGray, (ksizeX, ksizeY), sigmaX, sigmaY, cv2.BORDER_DEFAULT)
        p3_2gaussianGray = cv2.GaussianBlur(p3_2resizeGray, (ksizeX, ksizeY), sigmaX, sigmaY, cv2.BORDER_DEFAULT)
        cv2.imshow('p3_1gaussian', p3_1gaussian)
        cv2.imshow('p3_2gaussian', p3_2gaussian)
        cv2.imshow('p3_1gaussianGray', p3_1gaussianGray)
        cv2.imshow('p3_2gaussianGray', p3_2gaussianGray)
        cv2.moveWindow('p3_1gaussian', coordPictireX, coordPictireY)
        cv2.moveWindow('p3_1gaussianGray', p3_1resize.shape[1], coordPictireY)
        cv2.moveWindow('p3_2gaussian', 2 * p3_1resize.shape[1], coordPictireY)
        cv2.moveWindow('p3_2gaussianGray', 2 * p3_1resize.shape[1] + p3_2resize.shape[1], coordPictireY)

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
        p3_2bilatera = cv2.bilateralFilter(p3_2resize, d, sigmaColor, sigmaSpace, cv2.BORDER_DEFAULT)
        p3_1bilateraGray = cv2.bilateralFilter(p3_1resizeGray, d, sigmaColor, sigmaSpace, cv2.BORDER_DEFAULT)
        p3_2bilateraGray = cv2.bilateralFilter(p3_2resizeGray, d, sigmaColor, sigmaSpace, cv2.BORDER_DEFAULT)
        cv2.imshow('p3_1bilatera', p3_1bilatera)
        cv2.imshow('p3_2bilatera', p3_2bilatera)
        cv2.imshow('p3_1bilateraGray', p3_1bilateraGray)
        cv2.imshow('p3_2bilateraGray', p3_2bilateraGray)
        cv2.moveWindow('p3_1bilatera', coordPictireX, coordPictireY)
        cv2.moveWindow('p3_1bilateraGray', p3_1resize.shape[1], coordPictireY)
        cv2.moveWindow('p3_2bilatera', 2 * p3_1resize.shape[1], coordPictireY)
        cv2.moveWindow('p3_2bilateraGray', 2 * p3_1resize.shape[1] + p3_2resize.shape[1], coordPictireY)

    except cv2.error:
        pass
    if cv2.waitKey(1) == ord('q'):
        break

cv2.destroyAllWindows()

kernel = np.array([
        [-1, -1, -1],
        [-1, 9, -1],
        [-1, -1, -1]
])

kernelNorm = np.sum(kernel)

if kernelNorm == 0:
    kernelNorm += 1
else:
    pass

while True:
    try:

        p3_1filter2D = cv2.filter2D(p3_1resize, -1, 1 / kernelNorm * kernel)
        p3_2filter2D = cv2.filter2D(p3_2resize, -1, 1 / kernelNorm * kernel)
        p3_1filter2Dgray = cv2.filter2D(p3_1resizeGray, -1, 1 / kernelNorm * kernel)
        p3_2filter2Dgray = cv2.filter2D(p3_2resizeGray, -1, 1 / kernelNorm * kernel)
        cv2.imshow('p3_1filter2D', p3_1filter2D)
        cv2.imshow('p3_2filter2D', p3_2filter2D)
        cv2.imshow('p3_1filter2Dgray', p3_1filter2Dgray)
        cv2.imshow('p3_2filter2Dgray', p3_2filter2Dgray)
        cv2.moveWindow('p3_1filter2D', coordPictireX, coordPictireY)
        cv2.moveWindow('p3_1filter2Dgray', p3_1resize.shape[1], coordPictireY)
        cv2.moveWindow('p3_2filter2D', 2 * p3_1resize.shape[1], coordPictireY)
        cv2.moveWindow('p3_2filter2Dgray', 2 * p3_1resize.shape[1] + p3_2resize.shape[1], coordPictireY)

    except cv2.error:
        pass
    if cv2.waitKey(1) == ord('q'):
        break

cv2.destroyAllWindows()

##################################################################### 2

while True:

    cv2.imshow('p3_3', p3_3resize)
    cv2.imshow('p3_3gray', p3_3resizeGray)
    cv2.imshow('p3_4', p3_4resize)
    cv2.imshow('p3_4gray', p3_4resizeGray)

    cv2.moveWindow('p3_3', coordPictireX, coordPictireY)
    cv2.moveWindow('p3_3gray', p3_3resize.shape[1], coordPictireY)
    cv2.moveWindow('p3_4', 2*p3_3resize.shape[1], coordPictireY)
    cv2.moveWindow('p3_4gray', 2 * p3_3resize.shape[1] + p3_4resize.shape[1], coordPictireY)

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

        p3_3blur = cv2.blur(p3_3resize, (ksizeX, ksizeY), cv2.BORDER_DEFAULT)
        p3_4blur = cv2.blur(p3_4resize, (ksizeX, ksizeY), cv2.BORDER_DEFAULT)
        p3_3blurGray = cv2.blur(p3_3resizeGray, (ksizeX, ksizeY), cv2.BORDER_DEFAULT)
        p3_4blurGray = cv2.blur(p3_4resizeGray, (ksizeX, ksizeY), cv2.BORDER_DEFAULT)
        cv2.imshow('p3_3blur', p3_3blur)
        cv2.imshow('p3_4blur', p3_4blur)
        cv2.imshow('p3_3blurGray', p3_3blurGray)
        cv2.imshow('p3_4blurGray', p3_4blurGray)
        cv2.moveWindow('p3_3blur', coordPictireX, coordPictireY)
        cv2.moveWindow('p3_3blurGray', p3_3resize.shape[1], coordPictireY)
        cv2.moveWindow('p3_4blur', 2 * p3_3resize.shape[1], coordPictireY)
        cv2.moveWindow('p3_4blurGray', 2 * p3_3resize.shape[1] + p3_4resize.shape[1], coordPictireY)

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

        p3_3box = cv2.boxFilter(p3_3resize, -1, (ksizeX, ksizeY), cv2.BORDER_DEFAULT)
        p3_4box = cv2.boxFilter(p3_4resize, -1, (ksizeX, ksizeY), cv2.BORDER_DEFAULT)
        p3_3boxGray = cv2.boxFilter(p3_3resizeGray, -1, (ksizeX, ksizeY), cv2.BORDER_DEFAULT)
        p3_4boxGray = cv2.boxFilter(p3_4resizeGray, -1, (ksizeX, ksizeY), cv2.BORDER_DEFAULT)
        cv2.imshow('p3_3box', p3_3box)
        cv2.imshow('p3_4box', p3_4box)
        cv2.imshow('p3_3boxGray', p3_3boxGray)
        cv2.imshow('p3_4boxGray', p3_4boxGray)
        cv2.moveWindow('p3_3box', coordPictireX, coordPictireY)
        cv2.moveWindow('p3_3boxGray', p3_3resize.shape[1], coordPictireY)
        cv2.moveWindow('p3_4box', 2 * p3_3resize.shape[1], coordPictireY)
        cv2.moveWindow('p3_4boxGray', 2 * p3_3resize.shape[1] + p3_4resize.shape[1], coordPictireY)

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

        p3_3median = cv2.medianBlur(p3_3resize, ksize)
        p3_4median = cv2.medianBlur(p3_4resize, ksize)
        p3_3medianGray = cv2.medianBlur(p3_3resizeGray, ksize)
        p3_4medianGray = cv2.medianBlur(p3_4resizeGray, ksize)
        cv2.imshow('p3_3median', p3_3median)
        cv2.imshow('p3_4median', p3_4median)
        cv2.imshow('p3_3medianGray', p3_3medianGray)
        cv2.imshow('p3_4medianGray', p3_4medianGray)
        cv2.moveWindow('p3_3median', coordPictireX, coordPictireY)
        cv2.moveWindow('p3_3medianGray', p3_3resize.shape[1], coordPictireY)
        cv2.moveWindow('p3_4median', 2 * p3_3resize.shape[1], coordPictireY)
        cv2.moveWindow('p3_4medianGray', 2 * p3_3resize.shape[1] + p3_4resize.shape[1], coordPictireY)

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

        p3_3gaussian = cv2.GaussianBlur(p3_3resize, (ksizeX, ksizeY), sigmaX, sigmaY, cv2.BORDER_DEFAULT)
        p3_4gaussian = cv2.GaussianBlur(p3_4resize, (ksizeX, ksizeY), sigmaX, sigmaY, cv2.BORDER_DEFAULT)
        p3_3gaussianGray = cv2.GaussianBlur(p3_3resizeGray, (ksizeX, ksizeY), sigmaX, sigmaY, cv2.BORDER_DEFAULT)
        p3_4gaussianGray = cv2.GaussianBlur(p3_3resizeGray, (ksizeX, ksizeY), sigmaX, sigmaY, cv2.BORDER_DEFAULT)
        cv2.imshow('p3_3gaussian', p3_3gaussian)
        cv2.imshow('p3_4gaussian', p3_4gaussian)
        cv2.imshow('p3_3gaussianGray', p3_3gaussianGray)
        cv2.imshow('p3_4gaussianGray', p3_4gaussianGray)
        cv2.moveWindow('p3_3gaussian', coordPictireX, coordPictireY)
        cv2.moveWindow('p3_3gaussianGray', p3_3resize.shape[1], coordPictireY)
        cv2.moveWindow('p3_4gaussian', 2 * p3_3resize.shape[1], coordPictireY)
        cv2.moveWindow('p3_4gaussianGray', 2 * p3_3resize.shape[1] + p3_4resize.shape[1], coordPictireY)

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

        p3_3bilatera = cv2.bilateralFilter(p3_3resize, d, sigmaColor, sigmaSpace, cv2.BORDER_DEFAULT)
        p3_4bilatera = cv2.bilateralFilter(p3_4resize, d, sigmaColor, sigmaSpace, cv2.BORDER_DEFAULT)
        p3_3bilateraGray = cv2.bilateralFilter(p3_3resizeGray, d, sigmaColor, sigmaSpace, cv2.BORDER_DEFAULT)
        p3_4bilateraGray = cv2.bilateralFilter(p3_4resizeGray, d, sigmaColor, sigmaSpace, cv2.BORDER_DEFAULT)
        cv2.imshow('p3_3bilatera', p3_3bilatera)
        cv2.imshow('p3_4bilatera', p3_4bilatera)
        cv2.imshow('p3_3bilateraGray', p3_3bilateraGray)
        cv2.imshow('p3_4bilateraGray', p3_4bilateraGray)
        cv2.moveWindow('p3_3bilatera', coordPictireX, coordPictireY)
        cv2.moveWindow('p3_3bilateraGray', p3_3resize.shape[1], coordPictireY)
        cv2.moveWindow('p3_4bilatera', 2 * p3_3resize.shape[1], coordPictireY)
        cv2.moveWindow('p3_4bilateraGray', 2 * p3_3resize.shape[1] + p3_4resize.shape[1], coordPictireY)

    except cv2.error:
        pass
    if cv2.waitKey(1) == ord('q'):
        break

cv2.destroyAllWindows()

kernel = np.array([
        [-1, -1, -1],
        [-1, 9, -1],
        [-1, -1, -1]
])

kernelNorm = np.sum(kernel)

if kernelNorm == 0:
    kernelNorm += 1
else:
    pass

while True:
    try:

        p3_3filter2D = cv2.filter2D(p3_3resize, -1, 1 / kernelNorm * kernel)
        p3_4filter2D = cv2.filter2D(p3_4resize, -1, 1 / kernelNorm * kernel)
        p3_3filter2Dgray = cv2.filter2D(p3_3resizeGray, -1, 1 / kernelNorm * kernel)
        p3_4filter2Dgray = cv2.filter2D(p3_4resizeGray, -1, 1 / kernelNorm * kernel)
        cv2.imshow('p3_3filter2D', p3_3filter2D)
        cv2.imshow('p3_4filter2D', p3_4filter2D)
        cv2.imshow('p3_3filter2Dgray', p3_3filter2Dgray)
        cv2.imshow('p3_4filter2Dgray', p3_4filter2Dgray)
        cv2.moveWindow('p3_3filter2D', coordPictireX, coordPictireY)
        cv2.moveWindow('p3_3filter2Dgray', p3_3resize.shape[1], coordPictireY)
        cv2.moveWindow('p3_4filter2D', 2 * p3_3resize.shape[1], coordPictireY)
        cv2.moveWindow('p3_4filter2Dgray', 2 * p3_3resize.shape[1] + p3_4resize.shape[1], coordPictireY)

    except cv2.error:
        pass
    if cv2.waitKey(1) == ord('q'):
        break

cv2.destroyAllWindows()