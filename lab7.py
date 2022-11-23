import cv2
import numpy as np
import math as math
import os

def nothing(x):

    pass

def createTrackbarForHoughLines():

    cv2.namedWindow("hough lines conversion parameter")

    cv2.createTrackbar("rho_res", "hough lines conversion parameter", 1, 10, nothing)
    cv2.createTrackbar("theta_res", "hough lines conversion parameter", 1, 360, nothing)
    cv2.createTrackbar("threshold", "hough lines conversion parameter", 0, 255, nothing)

    cv2.moveWindow("hough lines conversion parameter", 1440, 50)

def handlingTrackbarForHoughLines():

    rho_res = int(cv2.getTrackbarPos("rho_res", "hough lines conversion parameter"))
    theta_res = int(cv2.getTrackbarPos("theta_res", "hough lines conversion parameter"))
    threshold = int(cv2.getTrackbarPos("threshold", "hough lines conversion parameter"))

    return rho_res, theta_res, threshold

def createTrackbarForHoughPLines():

    cv2.namedWindow("hough P lines conversion parameter")

    cv2.createTrackbar("rho_res", "hough P lines conversion parameter", 1, 10, nothing)
    cv2.createTrackbar("theta_res", "hough P lines conversion parameter", 1, 360, nothing)
    cv2.createTrackbar("threshold", "hough P lines conversion parameter", 0, 255, nothing)
    cv2.createTrackbar("minLineLength", "hough P lines conversion parameter", 0, 255, nothing)
    cv2.createTrackbar("maxLineGap", "hough P lines conversion parameter", 0, 255, nothing)

    cv2.moveWindow("hough P lines conversion parameter", 1440, 50)

def handlingTrackbarForHoughPLines():

    rho_res = int(cv2.getTrackbarPos("rho_res", "hough P lines conversion parameter"))
    theta_res = int(cv2.getTrackbarPos("theta_res", "hough P lines conversion parameter"))
    threshold = int(cv2.getTrackbarPos("threshold", "hough P lines conversion parameter"))
    minLineLength = int(cv2.getTrackbarPos("minLineLength", "hough P lines conversion parameter"))
    maxLineGap = int(cv2.getTrackbarPos("maxLineGap", "hough P lines conversion parameter"))

    return rho_res, theta_res, threshold, minLineLength, maxLineGap

def createTrackbarForHoughCircles():

    cv2.namedWindow("hough circles conversion parameter")

    cv2.createTrackbar("dp", "hough circles conversion parameter", 1, 100, nothing)
    cv2.createTrackbar("minDist", "hough circles conversion parameter", 1, 100, nothing)
    cv2.createTrackbar("param1", "hough circles conversion parameter", 50, 300, nothing)
    cv2.createTrackbar("param2", "hough circles conversion parameter", 30, 300, nothing)
    cv2.createTrackbar("minRadius", "hough circles conversion parameter", 1, 100, nothing)
    cv2.createTrackbar("maxRadius", "hough circles conversion parameter", 1, 100, nothing)

    cv2.moveWindow("hough circles conversion parameter", 1440, 350)

def handlingTrackbarForHoughCircles():

    dp = int(cv2.getTrackbarPos("dp", "hough circles conversion parameter"))
    minDist = int(cv2.getTrackbarPos("minDist", "hough circles conversion parameter"))
    param1 = int(cv2.getTrackbarPos("param1", "hough circles conversion parameter"))
    param2 = int(cv2.getTrackbarPos("param2", "hough circles conversion parameter"))
    minRadius = int(cv2.getTrackbarPos("minRadius", "hough circles conversion parameter"))
    maxRadius = int(cv2.getTrackbarPos("maxRadius", "hough circles conversion parameter"))

    return dp, minDist, param1, param2, minRadius, maxRadius

def createTrackbarForCanny():

    cv2.namedWindow("canny conversion parameter")

    cv2.createTrackbar("threshold1", "canny conversion parameter", 0, 255, nothing)
    cv2.createTrackbar("threshold2", "canny conversion parameter", 0, 255, nothing)

    cv2.moveWindow("canny conversion parameter", 1440, 650)

def handlingTrackbarForCanny():

    threshold1 = int(cv2.getTrackbarPos("threshold1", "canny conversion parameter"))
    threshold2 = int(cv2.getTrackbarPos("threshold2", "canny conversion parameter"))

    return threshold1, threshold2

def createTrackbarForColor():

    cv2.namedWindow("color")

    cv2.createTrackbar("colorB", "color", 0, 255, nothing)
    cv2.createTrackbar("colorG", "color", 0, 255, nothing)
    cv2.createTrackbar("colorR", "color", 0, 255, nothing)

    cv2.moveWindow("color", 1440, 800)

def handlingTrackbarForColor():

    colorB = int(cv2.getTrackbarPos("colorB", "color"))
    colorG = int(cv2.getTrackbarPos("colorG", "color"))
    colorR = int(cv2.getTrackbarPos("colorR", "color"))

    return colorB, colorG, colorR

if __name__ == "__main__":

    os.system('cls||clear')

    # задание 1

    picture7_1 = cv2.imread('lr7/7_1.jpg', cv2.IMREAD_GRAYSCALE)

    while True:

        cv2.imshow("original", picture7_1)

        if cv2.waitKey(1) == ord('q'):
            break

    cv2.destroyAllWindows()

    createTrackbarForHoughLines()
    createTrackbarForCanny()
    createTrackbarForColor()

    while True:
        
        os.system('cls||clear')

        try:

            threshold1, threshold2 = handlingTrackbarForCanny()
            rho_res, theta_res, threshold = handlingTrackbarForHoughLines()
            colorB, colorG, colorR = handlingTrackbarForColor()

            pictureAfterCanny = cv2.Canny(picture7_1, threshold1, threshold2, apertureSize=3, L2gradient=False)
            pictureAfterCannyBGR = cv2.cvtColor( pictureAfterCanny, cv2.COLOR_GRAY2BGR)
            lines = cv2.HoughLines(pictureAfterCanny, rho_res, theta_res * np.pi / 180, threshold, min_theta=None, max_theta=None)

            if lines is not None:
                for i in range(0, len(lines)):
                    rho = lines[i][0][0]
                    theta = lines[i][0][1]
                    a = math.cos(theta)
                    b = math.sin(theta)
                    x0 = a * rho
                    y0 = b * rho
                    pt1 = (int(x0 + 1000 * (-b)), int(y0 + 1000 * (a)))
                    pt2 = (int(x0 - 1000 * (-b)), int(y0 - 1000 * (a)))
                    cv2.line(pictureAfterCannyBGR, pt1, pt2, (colorB, colorG, colorR), 3, cv2.LINE_AA)

            cv2.imshow("result of standard hough line transform", pictureAfterCannyBGR)

        except cv2.error as err:
            print(err)
            pass

        if cv2.waitKey(1) == ord('q'):
            break

    cv2.destroyAllWindows()

    createTrackbarForHoughPLines()
    createTrackbarForCanny()
    createTrackbarForColor()

    while True:
        
        os.system('cls||clear')

        try:

            threshold1, threshold2 = handlingTrackbarForCanny()
            rho_res, theta_res, threshold, minLineLength, maxLineGap = handlingTrackbarForHoughPLines()
            colorB, colorG, colorR = handlingTrackbarForColor()

            pictureAfterCanny = cv2.Canny(picture7_1, threshold1, threshold2, apertureSize=3, L2gradient=False)
            pictureAfterCannyBGR = cv2.cvtColor( pictureAfterCanny, cv2.COLOR_GRAY2BGR)
            linesP = cv2.HoughLinesP(pictureAfterCanny, rho_res, theta_res * np.pi / 180, threshold, None, minLineLength, maxLineGap)

            if linesP is not None:
                for i in range(0, len(linesP)):
                    l = linesP[i][0]
                    cv2.line(pictureAfterCannyBGR, (l[0], l[1]), (l[2], l[3]), (colorB, colorG, colorR), 3, cv2.LINE_AA)

            cv2.imshow("result of probabilistic line transform", pictureAfterCannyBGR)

        except cv2.error as err:
            print(err)
            pass

        if cv2.waitKey(1) == ord('q'):
            break

    cv2.destroyAllWindows()

    # задание 2

    pictureP2 = cv2.imread('lr7/pictureP2.png', cv2.IMREAD_GRAYSCALE)

    while True:

        cv2.imshow("original", pictureP2)

        if cv2.waitKey(1) == ord('q'):
            break

    cv2.destroyAllWindows()

    createTrackbarForHoughPLines()
    createTrackbarForHoughCircles()
    createTrackbarForCanny()
    createTrackbarForColor()

    while True:
        
        os.system('cls||clear')

        try:

            pictureP2 = cv2.imread('lr7/pictureP2.png')
            pictureP2gray = cv2.imread('lr7/pictureP2.png', cv2.IMREAD_GRAYSCALE)

            threshold1, threshold2 = handlingTrackbarForCanny()
            rho_res, theta_res, threshold, minLineLength, maxLineGap = handlingTrackbarForHoughPLines()
            dp, minDist, param1, param2, minRadius, maxRadius = handlingTrackbarForHoughCircles()
            colorB, colorG, colorR = handlingTrackbarForColor()

            pictureAfterCanny = cv2.Canny(pictureP2gray, threshold1, threshold2, apertureSize=3, L2gradient=False)

            linesP = cv2.HoughLinesP(pictureAfterCanny, rho_res, theta_res * np.pi / 180, threshold, None, minLineLength, maxLineGap)
            circles = cv2.HoughCircles(pictureAfterCanny, cv2.HOUGH_GRADIENT, dp, minDist, param1, param2, minRadius, maxRadius)
            circles = np.uint16(np.around(circles))

            if linesP is not None:
                for i in range(0, len(linesP)):
                    l = linesP[i][0]
                    cv2.line(pictureP2, (l[0], l[1]), (l[2], l[3]), (colorB, colorG, colorR), 3, cv2.LINE_AA)

            if circles is not None:
                for i in circles[0, :]:
                    # draw the outer circle
                    cv2.circle(pictureP2, (i[0], i[1]), i[2], (colorB, colorG, colorR), 2)
                    # draw the center of the circle
                    cv2.circle(pictureP2, (i[0], i[1]), 2, (colorB, colorG, colorR), 3)

            cv2.imshow("result of hough circle transform", pictureP2)

        except cv2.error as err:
            print(err)
            pass

        if cv2.waitKey(1) == ord('q'):
            break

    cv2.destroyAllWindows()

    # задание 3

    video = cv2.VideoCapture('lr5/road.mp4')

    createTrackbarForHoughPLines()
    createTrackbarForCanny()
    createTrackbarForColor()

    while True:
        
        os.system('cls||clear')

        try:

            _, picture = video.read()
            picture = cv2.resize(picture, (picture.shape[1] // 2, picture.shape[0] // 2))
            picture = cv2.cvtColor(picture, cv2.COLOR_BGR2GRAY)

            threshold1, threshold2 = handlingTrackbarForCanny()
            rho_res, theta_res, threshold, minLineLength, maxLineGap = handlingTrackbarForHoughPLines()
            colorB, colorG, colorR = handlingTrackbarForColor()

            pictureAfterCanny = cv2.Canny(picture, threshold1, threshold2, apertureSize=3, L2gradient=False)
            pictureAfterCannyBGR = cv2.cvtColor( pictureAfterCanny, cv2.COLOR_GRAY2BGR)
            linesP = cv2.HoughLinesP(pictureAfterCanny, rho_res, theta_res * np.pi / 180, threshold, None, minLineLength, maxLineGap)

            if linesP is not None:
                for i in range(0, len(linesP)):
                    l = linesP[i][0]
                    cv2.line(pictureAfterCannyBGR, (l[0], l[1]), (l[2], l[3]), (colorB, colorG, colorR), 3, cv2.LINE_AA)

            cv2.imshow("result of probabilistic line transform", pictureAfterCannyBGR)

            if cv2.waitKey(1) == ord('q'):
                break

        except AttributeError as err:
            print(err)
            break
        except cv2.error as err:
            print(err)
            pass

    cv2.destroyAllWindows()

    # задание 4

    pictureP4 = cv2.imread('lr7/pictureP4.jpg', cv2.IMREAD_GRAYSCALE)

    while True:

        cv2.imshow("original", pictureP4)

        if cv2.waitKey(1) == ord('q'):
            break

    cv2.destroyAllWindows()

    createTrackbarForHoughPLines()
    createTrackbarForCanny()
    createTrackbarForColor()

    while True:
        
        os.system('cls||clear')

        try:

            threshold1, threshold2 = handlingTrackbarForCanny()
            rho_res, theta_res, threshold, minLineLength, maxLineGap = handlingTrackbarForHoughPLines()
            colorB, colorG, colorR = handlingTrackbarForColor()

            pictureAfterCanny = cv2.Canny(pictureP4, threshold1, threshold2, apertureSize=3, L2gradient=False)
            pictureAfterCannyBGR = cv2.cvtColor( pictureAfterCanny, cv2.COLOR_GRAY2BGR)
            linesP = cv2.HoughLinesP(pictureAfterCanny, rho_res, theta_res * np.pi / 180, threshold, None, minLineLength, maxLineGap)

            if linesP is not None:
                for i in range(0, len(linesP)):
                    l = linesP[i][0]
                    cv2.line(pictureAfterCannyBGR, (l[0], l[1]), (l[2], l[3]), (colorB, colorG, colorR), 3, cv2.LINE_AA)

            cv2.imshow("result of probabilistic line transform", pictureAfterCannyBGR)

        except cv2.error as err:
            print(err)
            pass

        if cv2.waitKey(1) == ord('q'):
            break

    cv2.destroyAllWindows()

    # задание 5

    picture7_5_X = cv2.imread('lr7/7_5_1.jpg', cv2.IMREAD_GRAYSCALE)
    picture7_5_X = cv2.resize(picture7_5_X, (picture7_5_X.shape[1] // 6, picture7_5_X.shape[0] // 6))

    while True:

        cv2.imshow("original", picture7_5_X)

        if cv2.waitKey(1) == ord('q'):
            break

    cv2.destroyAllWindows()

    createTrackbarForHoughCircles()
    createTrackbarForCanny()
    createTrackbarForColor()

    while True:
        
        os.system('cls||clear')

        try:

            picture7_5_X = cv2.imread('lr7/7_5_1.jpg')
            picture7_5_X = cv2.resize(picture7_5_X, (picture7_5_X.shape[1] // 6, picture7_5_X.shape[0] // 6))

            picture7_5_Xgray = cv2.imread('lr7/7_5_1.jpg', cv2.IMREAD_GRAYSCALE)
            picture7_5_Xgray = cv2.resize(picture7_5_Xgray, (picture7_5_Xgray.shape[1] // 6, picture7_5_Xgray.shape[0] // 6))

            threshold1, threshold2 = handlingTrackbarForCanny()
            dp, minDist, param1, param2, minRadius, maxRadius = handlingTrackbarForHoughCircles()
            colorB, colorG, colorR = handlingTrackbarForColor()

            pictureAfterCanny = cv2.Canny(picture7_5_Xgray, threshold1, threshold2, apertureSize=3, L2gradient=False)

            circles = cv2.HoughCircles(pictureAfterCanny, cv2.HOUGH_GRADIENT, dp, minDist, param1, param2, minRadius, maxRadius)
            circles = np.uint16(np.around(circles))

            if circles is not None:
                for i in circles[0, :]:
                    # draw the outer circle
                    cv2.circle(picture7_5_X, (i[0], i[1]), i[2], (colorB, colorG, colorR), 2)
                    # draw the center of the circle
                    cv2.circle(picture7_5_X, (i[0], i[1]), 2, (colorB, colorG, colorR), 3)

            cv2.imshow("result of hough circle transform", picture7_5_X)

        except cv2.error as err:
            print(err)
            pass

        if cv2.waitKey(1) == ord('q'):
            break

    cv2.destroyAllWindows()

    os.system('cls||clear')