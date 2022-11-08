import cv2
import numpy as np
import time
import math

def nothing(x):
    pass
def createTrackbarForCannyAndHoughLines():
    cv2.namedWindow("conversion parameter")

    cv2.createTrackbar("threshold1", "conversion parameter", 0, 255, nothing)
    cv2.createTrackbar("threshold2", "conversion parameter", 0, 255, nothing)

    cv2.createTrackbar("rho_res", "conversion parameter", 1, 10, nothing)
    cv2.createTrackbar("theta_res", "conversion parameter", 1, 360, nothing)
    cv2.createTrackbar("threshold", "conversion parameter", 0, 255, nothing)

    cv2.createTrackbar("colorB", "conversion parameter", 0, 255, nothing)
    cv2.createTrackbar("colorG", "conversion parameter", 0, 255, nothing)
    cv2.createTrackbar("colorR", "conversion parameter", 0, 255, nothing)

    cv2.moveWindow("conversion parameter", 960, 100)

def createTrackbarForCannyAndHoughLinesP():
    cv2.namedWindow("conversion parameter")

    cv2.createTrackbar("threshold1", "conversion parameter", 0, 255, nothing)
    cv2.createTrackbar("threshold2", "conversion parameter", 0, 255, nothing)

    cv2.createTrackbar("rho_res", "conversion parameter", 1, 10, nothing)
    cv2.createTrackbar("theta_res", "conversion parameter", 1, 360, nothing)
    cv2.createTrackbar("threshold", "conversion parameter", 0, 255, nothing)

    cv2.createTrackbar("minLineLength", "conversion parameter", 0, 255, nothing)
    cv2.createTrackbar("maxLineGap", "conversion parameter", 0, 255, nothing)

    cv2.createTrackbar("colorB", "conversion parameter", 0, 255, nothing)
    cv2.createTrackbar("colorG", "conversion parameter", 0, 255, nothing)
    cv2.createTrackbar("colorR", "conversion parameter", 0, 255, nothing)

    cv2.moveWindow("conversion parameter", 960, 100)

# решение 1

picture7_1 = cv2.imread('lr7/7_1.jpg', cv2.IMREAD_GRAYSCALE)

while True:

    cv2.imshow("original", picture7_1)

    if cv2.waitKey(1) == ord('q'):
        break

cv2.destroyAllWindows()

createTrackbarForCannyAndHoughLines()

while True:

    try:

        threshold1 = int(cv2.getTrackbarPos("threshold1", "conversion parameter"))
        threshold2 = int(cv2.getTrackbarPos("threshold2", "conversion parameter"))

        rho_res = int(cv2.getTrackbarPos("rho_res", "conversion parameter"))
        theta_res = int(cv2.getTrackbarPos("theta_res", "conversion parameter"))
        threshold = int(cv2.getTrackbarPos("threshold", "conversion parameter"))

        colorB = int(cv2.getTrackbarPos("colorB", "conversion parameter"))
        colorG = int(cv2.getTrackbarPos("colorG", "conversion parameter"))
        colorR = int(cv2.getTrackbarPos("colorR", "conversion parameter"))

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

    except cv2.error:
        pass

    if cv2.waitKey(1) == ord('q'):
        break

cv2.destroyAllWindows()

createTrackbarForCannyAndHoughLinesP()

while True:

    try:

        threshold1 = int(cv2.getTrackbarPos("threshold1", "conversion parameter"))
        threshold2 = int(cv2.getTrackbarPos("threshold2", "conversion parameter"))

        rho_res = int(cv2.getTrackbarPos("rho_res", "conversion parameter"))
        theta_res = int(cv2.getTrackbarPos("theta_res", "conversion parameter"))
        threshold = int(cv2.getTrackbarPos("threshold", "conversion parameter"))
        minLineLength = int(cv2.getTrackbarPos("minLineLength", "conversion parameter"))
        maxLineGap = int(cv2.getTrackbarPos("maxLineGap", "conversion parameter"))

        colorB = int(cv2.getTrackbarPos("colorB", "conversion parameter"))
        colorG = int(cv2.getTrackbarPos("colorG", "conversion parameter"))
        colorR = int(cv2.getTrackbarPos("colorR", "conversion parameter"))

        pictureAfterCanny = cv2.Canny(picture7_1, threshold1, threshold2, apertureSize=3, L2gradient=False)
        pictureAfterCannyBGR = cv2.cvtColor( pictureAfterCanny, cv2.COLOR_GRAY2BGR)
        linesP = cv2.HoughLinesP(pictureAfterCanny, rho_res, theta_res * np.pi / 180, threshold, None, minLineLength, maxLineGap)

        if linesP is not None:
            for i in range(0, len(linesP)):
                l = linesP[i][0]
                cv2.line(pictureAfterCannyBGR, (l[0], l[1]), (l[2], l[3]), (colorB, colorG, colorR), 3, cv2.LINE_AA)

        cv2.imshow("result of probabilistic line transform", pictureAfterCannyBGR)

    except cv2.error:
        pass
    if cv2.waitKey(1) == ord('q'):
        break

cv2.destroyAllWindows()

# решение 2

pictureP2 = cv2.imread('lr7/pictureP2.png', cv2.IMREAD_GRAYSCALE)

while True:

    cv2.imshow("original", pictureP2)

    if cv2.waitKey(1) == ord('q'):
        break

cv2.destroyAllWindows()

createTrackbarForCannyAndHoughLinesP()

while True:

    try:

        threshold1 = int(cv2.getTrackbarPos("threshold1", "conversion parameter"))
        threshold2 = int(cv2.getTrackbarPos("threshold2", "conversion parameter"))

        rho_res = int(cv2.getTrackbarPos("rho_res", "conversion parameter"))
        theta_res = int(cv2.getTrackbarPos("theta_res", "conversion parameter"))
        threshold = int(cv2.getTrackbarPos("threshold", "conversion parameter"))
        minLineLength = int(cv2.getTrackbarPos("minpictureLineLength", "conversion parameter"))
        maxLineGap = int(cv2.getTrackbarPos("maxLineGap", "conversion parameter"))

        colorB = int(cv2.getTrackbarPos("colorB", "conversion parameter"))
        colorG = int(cv2.getTrackbarPos("colorG", "conversion parameter"))
        colorR = int(cv2.getTrackbarPos("colorR", "conversion parameter"))

        pictureAfterCanny = cv2.Canny(pictureP2, threshold1, threshold2, apertureSize=3, L2gradient=False)
        pictureAfterCannyBGR = cv2.cvtColor( pictureAfterCanny, cv2.COLOR_GRAY2BGR)
        linesP = cv2.HoughLinesP(pictureAfterCanny, rho_res, theta_res * np.pi / 180, threshold, None, minLineLength, maxLineGap)

        if linesP is not None:
            for i in range(0, len(linesP)):
                l = linesP[i][0]
                cv2.line(pictureAfterCannyBGR, (l[0], l[1]), (l[2], l[3]), (colorB, colorG, colorR), 3, cv2.LINE_AA)

        cv2.imshow("result of probabilistic line transform", pictureAfterCannyBGR)

    except cv2.error:
        pass
    if cv2.waitKey(1) == ord('q'):
        break