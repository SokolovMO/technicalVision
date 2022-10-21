import cv2
import numpy as np
import math
import time

# задание 1

def nothing(x):
    pass

shkalaNeTolkoSerogo = cv2.imread('lr2/shkalaNeTolkoSerogo.jpg')
shkalaSerogo = cv2.cvtColor(shkalaNeTolkoSerogo, cv2.COLOR_BGR2GRAY)
coordPictireX = 0
coordPictireY = 0


while True:
    cv2.imshow('shkalaSerogo', shkalaSerogo)
    cv2.moveWindow('shkalaSerogo', coordPictireX, coordPictireY)
    if cv2.waitKey(1) == ord('q'):
        break

cv2.destroyWindow('shkalaSerogo')

cv2.namedWindow("conversion parameter")
cv2.createTrackbar("T1", "conversion parameter", 0, 255, nothing)
cv2.createTrackbar("T2", "conversion parameter", 0, 255, nothing)
cv2.moveWindow("conversion parameter", 0, 350)
cv2.resizeWindow("conversion parameter", 500, 50)

while True:
    T1 = int(cv2.getTrackbarPos("T1", "conversion parameter"))
    T2 = int(cv2.getTrackbarPos("T2", "conversion parameter"))
    _, threshPicture1 = cv2.threshold(shkalaSerogo, T1, T2, cv2.THRESH_TRUNC)
    cv2.imshow('THRESH_TRUNC', threshPicture1)
    cv2.moveWindow('THRESH_TRUNC', coordPictireX, coordPictireY)
    if cv2.waitKey(1) == ord('q'):
        break

cv2.destroyWindow('THRESH_TRUNC')

while True:
    T1 = int(cv2.getTrackbarPos("T1", "conversion parameter"))
    T2 = int(cv2.getTrackbarPos("T2", "conversion parameter"))
    _, threshPicture2 = cv2.threshold(shkalaSerogo, T1, T2, cv2.THRESH_OTSU)
    cv2.imshow('THRESH_OTSU', threshPicture2)
    cv2.moveWindow('THRESH_OTSU', coordPictireX, coordPictireY)
    if cv2.waitKey(1) == ord('q'):
        break

cv2.destroyWindow('THRESH_OTSU')

while True:
    T1 = int(cv2.getTrackbarPos("T1", "conversion parameter"))
    T2 = int(cv2.getTrackbarPos("T2", "conversion parameter"))
    _, threshPicture3 = cv2.threshold(shkalaSerogo, T1, T2, cv2.THRESH_BINARY)
    cv2.imshow('THRESH_BINARY', threshPicture3)
    cv2.moveWindow('THRESH_BINARY', coordPictireX, coordPictireY)
    if cv2.waitKey(1) == ord('q'):
        break

cv2.destroyWindow('THRESH_BINARY')

while True:
    T1 = int(cv2.getTrackbarPos("T1", "conversion parameter"))
    T2 = int(cv2.getTrackbarPos("T2", "conversion parameter"))
    _, threshPicture4 = cv2.threshold(shkalaSerogo, T1, T2, cv2.THRESH_BINARY_INV)
    cv2.imshow('THRESH_BINARY_INV', threshPicture4)
    cv2.moveWindow('THRESH_BINARY_INV', coordPictireX, coordPictireY)
    if cv2.waitKey(1) == ord('q'):
        break

cv2.destroyWindow('THRESH_BINARY_INV')

while True:
    T1 = int(cv2.getTrackbarPos("T1", "conversion parameter"))
    T2 = int(cv2.getTrackbarPos("T2", "conversion parameter"))
    _, threshPicture5 = cv2.threshold(shkalaSerogo, T1, T2, cv2.THRESH_TRIANGLE)
    cv2.imshow('THRESH_TRIANGLE', threshPicture5)
    cv2.moveWindow('THRESH_TRIANGLE', coordPictireX, coordPictireY)
    if cv2.waitKey(1) == ord('q'):
        break

cv2.destroyWindow('THRESH_TRIANGLE')
cv2.destroyWindow('conversion parameter')

cv2.namedWindow("conversion parameter")
cv2.createTrackbar("T1", "conversion parameter", 0, 255, nothing)
cv2.createTrackbar("T2", "conversion parameter", 0, 50, nothing)
cv2.createTrackbar("T3", "conversion parameter", 0, 50, nothing)
cv2.moveWindow("conversion parameter", 0, 350)
cv2.resizeWindow("conversion parameter", 500, 50)

while True:
    T1 = int(cv2.getTrackbarPos("T1", "conversion parameter"))
    T2 = int(cv2.getTrackbarPos("T2", "conversion parameter"))
    T3 = int(cv2.getTrackbarPos("T3", "conversion parameter"))
    try:
        adaptiveTHRESH_BINARY = cv2.adaptiveThreshold(shkalaSerogo, T1, cv2.ADAPTIVE_THRESH_MEAN_C, cv2.THRESH_BINARY, T2, T3)
        cv2.imshow('adaptiveTHRESH_TRUNC', adaptiveTHRESH_BINARY)
        cv2.moveWindow('adaptiveTHRESH_TRUNC', coordPictireX, coordPictireY)
    except cv2.error:
        pass
    if cv2.waitKey(1) == ord('q'):
        break

cv2.destroyWindow('adaptiveTHRESH_TRUNC')

while True:
    T1 = int(cv2.getTrackbarPos("T1", "conversion parameter"))
    T2 = int(cv2.getTrackbarPos("T2", "conversion parameter"))
    T3 = int(cv2.getTrackbarPos("T3", "conversion parameter"))
    try:
        adaptiveTHRESH_BINARY_INV = cv2.adaptiveThreshold(shkalaSerogo, T1, cv2.ADAPTIVE_THRESH_GAUSSIAN_C, cv2.THRESH_BINARY_INV, T2, T3)
        cv2.imshow('adaptiveTHRESH_BINARY_INV', adaptiveTHRESH_BINARY_INV)
        cv2.moveWindow('adaptiveTHRESH_BINARY_INV', coordPictireX, coordPictireY)
    except cv2.error:
        pass
    if cv2.waitKey(1) == ord('q'):
        break

cv2.destroyWindow('adaptiveTHRESH_BINARY_INV')
cv2.destroyWindow('conversion parameter')

# задание 2

# картинка 221

def nothing(x):
    pass

picture221 = cv2.imread('lr2/221.jpg')
picture221resize = cv2.resize(picture221, (picture221.shape[1] // 6, picture221.shape[0] // 6))
picture221resizeGray = cv2.cvtColor(picture221resize, cv2.COLOR_BGR2GRAY)
coordPictireX = 0
coordPictireY = 0

while True:
    cv2.imshow('picture221', picture221resize)
    cv2.moveWindow('picture221', coordPictireX, coordPictireY)
    if cv2.waitKey(1) == ord('q'):
        break

cv2.destroyWindow('picture221')

cv2.namedWindow("conversion parameter")
cv2.createTrackbar("T1", "conversion parameter", 0, 255, nothing)
cv2.createTrackbar("T2", "conversion parameter", 0, 255, nothing)
cv2.moveWindow("conversion parameter", 0, 800)
cv2.resizeWindow("conversion parameter", 500, 50)

while True:
    T1 = int(cv2.getTrackbarPos("T1", "conversion parameter"))
    T2 = int(cv2.getTrackbarPos("T2", "conversion parameter"))
    _, threshTruncPicture221resizeGray = cv2.threshold(picture221resizeGray, T1, T2, cv2.THRESH_TRUNC)
    cv2.imshow('THRESH_TRUNC', threshTruncPicture221resizeGray)
    cv2.moveWindow('THRESH_TRUNC', coordPictireX, coordPictireY)
    if cv2.waitKey(1) == ord('q'):
        break

cv2.destroyWindow('THRESH_TRUNC')

while True:
    T1 = int(cv2.getTrackbarPos("T1", "conversion parameter"))
    T2 = int(cv2.getTrackbarPos("T2", "conversion parameter"))
    _, threshOtsuPicture221resizeGray = cv2.threshold(picture221resizeGray, T1, T2, cv2.THRESH_OTSU)
    cv2.imshow('THRESH_OTSU', threshOtsuPicture221resizeGray)
    cv2.moveWindow('THRESH_OTSU', coordPictireX, coordPictireY)
    if cv2.waitKey(1) == ord('q'):
        break

cv2.destroyWindow('THRESH_OTSU')

while True:
    T1 = int(cv2.getTrackbarPos("T1", "conversion parameter"))
    T2 = int(cv2.getTrackbarPos("T2", "conversion parameter"))
    _, threshBinaryPicture221resizeGray = cv2.threshold(picture221resizeGray, T1, T2, cv2.THRESH_BINARY)
    cv2.imshow('THRESH_BINARY', threshBinaryPicture221resizeGray)
    cv2.moveWindow('THRESH_BINARY', coordPictireX, coordPictireY)
    if cv2.waitKey(1) == ord('q'):
        break

cv2.destroyWindow('THRESH_BINARY')

while True:
    T1 = int(cv2.getTrackbarPos("T1", "conversion parameter"))
    T2 = int(cv2.getTrackbarPos("T2", "conversion parameter"))
    _, threshBinaryInvPicture221resizeGray = cv2.threshold(picture221resizeGray, T1, T2, cv2.THRESH_BINARY_INV)
    cv2.imshow('THRESH_BINARY_INV', threshBinaryInvPicture221resizeGray)
    cv2.moveWindow('THRESH_BINARY_INV', coordPictireX, coordPictireY)
    if cv2.waitKey(1) == ord('q'):
        break

cv2.destroyWindow('THRESH_BINARY_INV')

while True:
    T1 = int(cv2.getTrackbarPos("T1", "conversion parameter"))
    T2 = int(cv2.getTrackbarPos("T2", "conversion parameter"))
    _, threshTrianglePicture221resizeGray = cv2.threshold(picture221resizeGray, T1, T2, cv2.THRESH_TRIANGLE)
    cv2.imshow('THRESH_TRIANGLE', threshTrianglePicture221resizeGray)
    cv2.moveWindow('THRESH_TRIANGLE', coordPictireX, coordPictireY)
    if cv2.waitKey(1) == ord('q'):
        break

cv2.destroyWindow('THRESH_TRIANGLE')
cv2.destroyWindow('conversion parameter')

cv2.namedWindow("conversion parameter")
cv2.createTrackbar("T1", "conversion parameter", 0, 255, nothing)
cv2.createTrackbar("T2", "conversion parameter", 0, 50, nothing)
cv2.createTrackbar("T3", "conversion parameter", 0, 50, nothing)
cv2.moveWindow("conversion parameter", 0, 800)
cv2.resizeWindow("conversion parameter", 500, 50)

while True:
    T1 = int(cv2.getTrackbarPos("T1", "conversion parameter"))
    T2 = int(cv2.getTrackbarPos("T2", "conversion parameter"))
    T3 = int(cv2.getTrackbarPos("T3", "conversion parameter"))
    try:
        adaptiveThreshBinaryPicture221resizeGray = cv2.adaptiveThreshold(picture221resizeGray, T1, cv2.ADAPTIVE_THRESH_MEAN_C, cv2.THRESH_BINARY, T2, T3)
        cv2.imshow('adaptiveTHRESH_TRUNC', adaptiveThreshBinaryPicture221resizeGray)
        cv2.moveWindow('adaptiveTHRESH_TRUNC', coordPictireX, coordPictireY)
    except cv2.error:
        pass
    if cv2.waitKey(1) == ord('q'):
        break

cv2.destroyWindow('adaptiveTHRESH_TRUNC')

while True:
    T1 = cv2.getTrackbarPos("T1", "conversion parameter")
    T2 = cv2.getTrackbarPos("T2", "conversion parameter")
    T3 = cv2.getTrackbarPos("T3", "conversion parameter")
    try:
        adaptiveThreshBinaryInvPicture221resizeGray = cv2.adaptiveThreshold(picture221resizeGray, T1, cv2.ADAPTIVE_THRESH_GAUSSIAN_C, cv2.THRESH_BINARY_INV, T2, T3)
        cv2.imshow('adaptiveTHRESH_BINARY_INV', adaptiveThreshBinaryInvPicture221resizeGray)
        cv2.moveWindow('adaptiveTHRESH_BINARY_INV', coordPictireX, coordPictireY)
    except cv2.error:
        pass
    if cv2.waitKey(1) == ord('q'):
        break

cv2.destroyWindow('adaptiveTHRESH_BINARY_INV')
cv2.destroyWindow('conversion parameter')

# картинка 222

#####################################################################################################################################################################

def nothing(x):
    pass

picture222 = cv2.imread('lr2/222.jpg')
picture222resize = cv2.resize(picture222, (picture222.shape[1] // 4, picture222.shape[0] // 4))
picture222resizeGray = cv2.cvtColor(picture222resize, cv2.COLOR_BGR2GRAY)
coordPictireX = 0
coordPictireY = 0

while True:
    cv2.imshow('picture222', picture222resize)
    cv2.moveWindow('picture222', coordPictireX, coordPictireY)
    if cv2.waitKey(1) == ord('q'):
        break

cv2.destroyWindow('picture222')

cv2.namedWindow("conversion parameter")
cv2.createTrackbar("T1", "conversion parameter", 0, 255, nothing)
cv2.createTrackbar("T2", "conversion parameter", 0, 255, nothing)
cv2.moveWindow("conversion parameter", 0, 800)
cv2.resizeWindow("conversion parameter", 500, 50)

while True:
    T1 = int(cv2.getTrackbarPos("T1", "conversion parameter"))
    T2 = int(cv2.getTrackbarPos("T2", "conversion parameter"))
    _, threshTruncPicture222resizeGray = cv2.threshold(picture222resizeGray, T1, T2, cv2.THRESH_TRUNC)
    cv2.imshow('THRESH_TRUNC', threshTruncPicture222resizeGray)
    cv2.moveWindow('THRESH_TRUNC', coordPictireX, coordPictireY)
    if cv2.waitKey(1) == ord('q'):
        break

cv2.destroyWindow('THRESH_TRUNC')

while True:
    T1 = int(cv2.getTrackbarPos("T1", "conversion parameter"))
    T2 = int(cv2.getTrackbarPos("T2", "conversion parameter"))
    _, threshOtsuPicture222resizeGray = cv2.threshold(picture222resizeGray, T1, T2, cv2.THRESH_OTSU)
    cv2.imshow('THRESH_OTSU', threshOtsuPicture222resizeGray)
    cv2.moveWindow('THRESH_OTSU', coordPictireX, coordPictireY)
    if cv2.waitKey(1) == ord('q'):
        break

cv2.destroyWindow('THRESH_OTSU')

while True:
    T1 = int(cv2.getTrackbarPos("T1", "conversion parameter"))
    T2 = int(cv2.getTrackbarPos("T2", "conversion parameter"))
    _, threshBinaryPicture222resizeGray = cv2.threshold(picture222resizeGray, T1, T2, cv2.THRESH_BINARY)
    cv2.imshow('THRESH_BINARY', threshBinaryPicture222resizeGray)
    cv2.moveWindow('THRESH_BINARY', coordPictireX, coordPictireY)
    if cv2.waitKey(1) == ord('q'):
        break

cv2.destroyWindow('THRESH_BINARY')

while True:
    T1 = int(cv2.getTrackbarPos("T1", "conversion parameter"))
    T2 = int(cv2.getTrackbarPos("T2", "conversion parameter"))
    _, threshBinaryInvPicture222resizeGray = cv2.threshold(picture222resizeGray, T1, T2, cv2.THRESH_BINARY_INV)
    cv2.imshow('THRESH_BINARY_INV', threshBinaryInvPicture222resizeGray)
    cv2.moveWindow('THRESH_BINARY_INV', coordPictireX, coordPictireY)
    if cv2.waitKey(1) == ord('q'):
        break

cv2.destroyWindow('THRESH_BINARY_INV')

while True:
    T1 = int(cv2.getTrackbarPos("T1", "conversion parameter"))
    T2 = int(cv2.getTrackbarPos("T2", "conversion parameter"))
    _, threshTrianglePicture222resizeGray = cv2.threshold(picture222resizeGray, T1, T2, cv2.THRESH_TRIANGLE)
    cv2.imshow('THRESH_TRIANGLE', threshTrianglePicture222resizeGray)
    cv2.moveWindow('THRESH_TRIANGLE', coordPictireX, coordPictireY)
    if cv2.waitKey(1) == ord('q'):
        break

cv2.destroyWindow('THRESH_TRIANGLE')
cv2.destroyWindow('conversion parameter')

cv2.namedWindow("conversion parameter")
cv2.createTrackbar("T1", "conversion parameter", 0, 255, nothing)
cv2.createTrackbar("T2", "conversion parameter", 0, 50, nothing)
cv2.createTrackbar("T3", "conversion parameter", 0, 50, nothing)
cv2.moveWindow("conversion parameter", 0, 800)
cv2.resizeWindow("conversion parameter", 500, 50)

while True:
    T1 = int(cv2.getTrackbarPos("T1", "conversion parameter"))
    T2 = int(cv2.getTrackbarPos("T2", "conversion parameter"))
    T3 = int(cv2.getTrackbarPos("T3", "conversion parameter"))
    try:
        adaptiveThreshBinaryPicture222resizeGray = cv2.adaptiveThreshold(picture222resizeGray, T1, cv2.ADAPTIVE_THRESH_MEAN_C, cv2.THRESH_BINARY, T2, T3)
        cv2.imshow('adaptiveTHRESH_TRUNC', adaptiveThreshBinaryPicture222resizeGray)
        cv2.moveWindow('adaptiveTHRESH_TRUNC', coordPictireX, coordPictireY)
    except cv2.error:
        pass
    if cv2.waitKey(1) == ord('q'):
        break

cv2.destroyWindow('adaptiveTHRESH_TRUNC')

while True:
    T1 = cv2.getTrackbarPos("T1", "conversion parameter")
    T2 = cv2.getTrackbarPos("T2", "conversion parameter")
    T3 = cv2.getTrackbarPos("T3", "conversion parameter")
    try:
        adaptiveThreshBinaryInvPicture222resizeGray = cv2.adaptiveThreshold(picture222resizeGray, T1, cv2.ADAPTIVE_THRESH_GAUSSIAN_C, cv2.THRESH_BINARY_INV, T2, T3)
        cv2.imshow('adaptiveTHRESH_BINARY_INV', adaptiveThreshBinaryInvPicture222resizeGray)
        cv2.moveWindow('adaptiveTHRESH_BINARY_INV', coordPictireX, coordPictireY)
    except cv2.error:
        pass
    if cv2.waitKey(1) == ord('q'):
        break

cv2.destroyWindow('adaptiveTHRESH_BINARY_INV')
cv2.destroyWindow('conversion parameter')

# задание 3

def nothing(x):
    pass

coordPictireX = 0
coordPictireY = 0

video23 = cv2.VideoCapture('lr2/23.mov')
# video23 = cv2.VideoCapture(0)

while True:
    try:
        _, frame = video23.read()
        frame = cv2.resize(frame, (frame.shape[1] // 3, frame.shape[0] // 3))
        cv2.imshow('23.mp4', frame)
        cv2.moveWindow('23.mp4', coordPictireX, coordPictireY)
        if cv2.waitKey(1) == ord('q'):
            break
    except AttributeError:
        break

cv2.destroyWindow('23.mp4')

cv2.namedWindow("conversion parameter")
cv2.createTrackbar("T1", "conversion parameter", 0, 255, nothing)
cv2.createTrackbar("T2", "conversion parameter", 0, 255, nothing)
cv2.moveWindow("conversion parameter", 0, 800)
cv2.resizeWindow("conversion parameter", 500, 50)

while True:
    T1 = int(cv2.getTrackbarPos("T1", "conversion parameter"))
    T2 = int(cv2.getTrackbarPos("T2", "conversion parameter"))
    try:
        _, frame = video23.read()
        frame = cv2.resize(frame, (frame.shape[1] // 3, frame.shape[0] // 3))
        frameGray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        _, frameTHRESH_BINARY = cv2.threshold(frameGray, T1, T2, cv2.THRESH_BINARY)
        cv2.imshow('23threshBinary.mp4', frameTHRESH_BINARY)
        cv2.moveWindow('23threshBinary.mp4', coordPictireX, coordPictireY)
        if cv2.waitKey(1) == ord('q'):
            break
    except AttributeError:
        break

cv2.destroyWindow('23threshBinary.mp4')
cv2.destroyWindow('conversion parameter')

cv2.namedWindow("conversion parameter")
cv2.createTrackbar("T1", "conversion parameter", 0, 255, nothing)
cv2.createTrackbar("T2", "conversion parameter", 0, 50, nothing)
cv2.createTrackbar("T3", "conversion parameter", 0, 50, nothing)
cv2.moveWindow("conversion parameter", 0, 800)
cv2.resizeWindow("conversion parameter", 500, 50)

while True:
    T1 = int(cv2.getTrackbarPos("T1", "conversion parameter"))
    T2 = int(cv2.getTrackbarPos("T2", "conversion parameter"))
    T3 = int(cv2.getTrackbarPos("T3", "conversion parameter"))
    try:
        try:
            _, frame = video23.read()
            frame = cv2.resize(frame, (frame.shape[1] // 3, frame.shape[0] // 3))
            frameGray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
            adaptiveFrameTHRESH_BINARY = cv2.adaptiveThreshold(frameGray, T1, cv2.ADAPTIVE_THRESH_MEAN_C, cv2.THRESH_BINARY, T2, T3)
            cv2.imshow('23adaptiveThreshBinary.mp4', adaptiveFrameTHRESH_BINARY)
            cv2.moveWindow('23adaptiveThreshBinary.mp4', coordPictireX, coordPictireY)
        except cv2.error:
            pass
        if cv2.waitKey(1) == ord('q'):
            break
    except AttributeError:
        break

cv2.destroyWindow('23adaptiveThreshBinary.mp4')

while True:
    T1 = int(cv2.getTrackbarPos("T1", "conversion parameter"))
    T2 = int(cv2.getTrackbarPos("T2", "conversion parameter"))
    T3 = int(cv2.getTrackbarPos("T3", "conversion parameter"))
    try:
        try:
            _, frame = video23.read()
            frame = cv2.resize(frame, (frame.shape[1] // 3, frame.shape[0] // 3))
            frameGray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
            adaptiveFrameTHRESH_BINARY_INV = cv2.adaptiveThreshold(frameGray, T1, cv2.ADAPTIVE_THRESH_GAUSSIAN_C, cv2.THRESH_BINARY_INV, T2, T3)
            cv2.imshow('23adaptiveThreshBinaryInv.mp4', adaptiveFrameTHRESH_BINARY_INV)
            cv2.moveWindow('23adaptiveThreshBinaryInv.mp4', coordPictireX, coordPictireY)
        except cv2.error:
            pass
        if cv2.waitKey(1) == ord('q'):
            break
    except AttributeError:
        break

cv2.destroyWindow('23adaptiveThreshBinaryInv.mp4')
cv2.destroyWindow('conversion parameter')