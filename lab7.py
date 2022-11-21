import cv2
import numpy as np

def nothing(x):

    pass

def createTrackbarForCannyAndHoughLines():

    cv2.namedWindow("hough lines conversion parameter")

    cv2.createTrackbar("threshold1", "hough lines conversion parameter", 0, 255, nothing)
    cv2.createTrackbar("threshold2", "hough lines conversion parameter", 0, 255, nothing)

    cv2.createTrackbar("rho_res", "hough lines conversion parameter", 1, 10, nothing)
    cv2.createTrackbar("theta_res", "hough lines conversion parameter", 1, 360, nothing)
    cv2.createTrackbar("threshold", "hough lines conversion parameter", 0, 255, nothing)

    cv2.createTrackbar("colorB", "hough lines conversion parameter", 0, 255, nothing)
    cv2.createTrackbar("colorG", "hough lines conversion parameter", 0, 255, nothing)
    cv2.createTrackbar("colorR", "hough lines conversion parameter", 0, 255, nothing)

    cv2.moveWindow("hough lines conversion parameter", 960, 100)

def createTrackbarForCannyAndHoughLinesP():

    cv2.namedWindow("hough lines conversion parameter P")

    cv2.createTrackbar("threshold1", "hough lines conversion parameter P", 0, 255, nothing)
    cv2.createTrackbar("threshold2", "hough lines conversion parameter P", 0, 255, nothing)

    cv2.createTrackbar("rho_res", "hough lines conversion parameter P", 1, 10, nothing)
    cv2.createTrackbar("theta_res", "hough lines conversion parameter P", 1, 360, nothing)
    cv2.createTrackbar("threshold", "hough lines conversion parameter P", 0, 255, nothing)

    cv2.createTrackbar("minLineLength", "hough lines conversion parameter P", 0, 255, nothing)
    cv2.createTrackbar("maxLineGap", "hough lines conversion parameter P", 0, 255, nothing)

    cv2.createTrackbar("colorB", "hough lines conversion parameter P", 0, 255, nothing)
    cv2.createTrackbar("colorG", "hough lines conversion parameter P", 0, 255, nothing)
    cv2.createTrackbar("colorR", "hough lines conversion parameter P", 0, 255, nothing)

    cv2.moveWindow("hough lines conversion parameter P", 960, 100)

def createTrackbarForCircles():

    cv2.namedWindow("hough circles conversion parameter")

    cv2.createTrackbar("dp", "hough circles conversion parameter", 0, 255, nothing)
    cv2.createTrackbar("minDist", "hough circles conversion parameter", 0, 255, nothing)
    cv2.createTrackbar("param1", "hough circles conversion parameter", 1, 10, nothing)
    cv2.createTrackbar("param2", "hough circles conversion parameter", 1, 360, nothing)
    cv2.createTrackbar("minRadius", "hough circles conversion parameter", 0, 255, nothing)
    cv2.createTrackbar("maxRadius", "hough circles conversion parameter", 0, 255, nothing)

    cv2.createTrackbar("colorB", "hough circles conversion parameter", 0, 255, nothing)
    cv2.createTrackbar("colorG", "hough circles conversion parameter", 0, 255, nothing)
    cv2.createTrackbar("colorR", "hough circles conversion parameter", 0, 255, nothing)

    cv2.moveWindow("hough circles conversion parameter", 1440, 100)

if __name__ == "__main__":

    # задание 1

    # picture7_1 = cv2.imread('lr7/7_1.jpg', cv2.IMREAD_GRAYSCALE)

    # while True:

    #     cv2.imshow("original", picture7_1)

    #     if cv2.waitKey(1) == ord('q'):
    #         break

    # cv2.destroyAllWindows()

    # createTrackbarForCannyAndHoughLines()

    # while True:

    #     try:

    #         threshold1 = int(cv2.getTrackbarPos("threshold1", "hough lines conversion parameter"))
    #         threshold2 = int(cv2.getTrackbarPos("threshold2", "hough lines conversion parameter"))

    #         rho_res = int(cv2.getTrackbarPos("rho_res", "hough lines conversion parameter"))
    #         theta_res = int(cv2.getTrackbarPos("theta_res", "hough lines conversion parameter"))
    #         threshold = int(cv2.getTrackbarPos("threshold", "hough lines conversion parameter"))

    #         colorB = int(cv2.getTrackbarPos("colorB", "hough lines conversion parameter"))
    #         colorG = int(cv2.getTrackbarPos("colorG", "hough lines conversion parameter"))
    #         colorR = int(cv2.getTrackbarPos("colorR", "hough lines conversion parameter"))

    #         pictureAfterCanny = cv2.Canny(picture7_1, threshold1, threshold2, apertureSize=3, L2gradient=False)
    #         pictureAfterCannyBGR = cv2.cvtColor( pictureAfterCanny, cv2.COLOR_GRAY2BGR)
    #         lines = cv2.HoughLines(pictureAfterCanny, rho_res, theta_res * np.pi / 180, threshold, min_theta=None, max_theta=None)

    #         if lines is not None:
    #             for i in range(0, len(lines)):
    #                 rho = lines[i][0][0]
    #                 theta = lines[i][0][1]
    #                 a = math.cos(theta)
    #                 b = math.sin(theta)
    #                 x0 = a * rho
    #                 y0 = b * rho
    #                 pt1 = (int(x0 + 1000 * (-b)), int(y0 + 1000 * (a)))
    #                 pt2 = (int(x0 - 1000 * (-b)), int(y0 - 1000 * (a)))
    #                 cv2.line(pictureAfterCannyBGR, pt1, pt2, (colorB, colorG, colorR), 3, cv2.LINE_AA)

    #         cv2.imshow("result of standard hough line transform", pictureAfterCannyBGR)

    #     except cv2.error:
    #         pass

    #     if cv2.waitKey(1) == ord('q'):
    #         break

    # cv2.destroyAllWindows()

    # createTrackbarForCannyAndHoughLinesP()

    # while True:

    #     try:

    #         threshold1 = int(cv2.getTrackbarPos("threshold1", "hough lines conversion parameter P"))
    #         threshold2 = int(cv2.getTrackbarPos("threshold2", "hough lines conversion parameter P"))

    #         rho_res = int(cv2.getTrackbarPos("rho_res", "hough lines conversion parameter P"))
    #         theta_res = int(cv2.getTrackbarPos("theta_res", "hough lines conversion parameter P"))
    #         threshold = int(cv2.getTrackbarPos("threshold", "hough lines conversion parameter P"))
    #         minLineLength = int(cv2.getTrackbarPos("minLineLength", "hough lines conversion parameter P"))
    #         maxLineGap = int(cv2.getTrackbarPos("maxLineGap", "hough lines conversion parameter P"))

    #         colorB = int(cv2.getTrackbarPos("colorB", "hough lines conversion parameter P"))
    #         colorG = int(cv2.getTrackbarPos("colorG", "hough lines conversion parameter P"))
    #         colorR = int(cv2.getTrackbarPos("colorR", "hough lines conversion parameter P"))

    #         pictureAfterCanny = cv2.Canny(picture7_1, threshold1, threshold2, apertureSize=3, L2gradient=False)
    #         pictureAfterCannyBGR = cv2.cvtColor( pictureAfterCanny, cv2.COLOR_GRAY2BGR)
    #         linesP = cv2.HoughLinesP(pictureAfterCanny, rho_res, theta_res * np.pi / 180, threshold, None, minLineLength, maxLineGap)

    #         if linesP is not None:
    #             for i in range(0, len(linesP)):
    #                 l = linesP[i][0]
    #                 cv2.line(pictureAfterCannyBGR, (l[0], l[1]), (l[2], l[3]), (colorB, colorG, colorR), 3, cv2.LINE_AA)

    #         cv2.imshow("result of probabilistic line transform", pictureAfterCannyBGR)

    #     except cv2.error:
    #         pass

    #     if cv2.waitKey(1) == ord('q'):
    #         break

    # cv2.destroyAllWindows()

    # задание 2

    # pictureP2 = cv2.imread('lr7/pictureP2.png', cv2.IMREAD_GRAYSCALE)

    # while True:

    #     cv2.imshow("original", pictureP2)

    #     if cv2.waitKey(1) == ord('q'):
    #         break

    # cv2.destroyAllWindows()

    # createTrackbarForCannyAndHoughLinesP()
    # createTrackbarForCircles()

    # while True:

    #     try:

    #         threshold1 = int(cv2.getTrackbarPos("threshold1", "hough lines conversion parameter P"))
    #         threshold2 = int(cv2.getTrackbarPos("threshold2", "hough lines conversion parameter P"))

    #         rho_res = int(cv2.getTrackbarPos("rho_res", "hough lines conversion parameter P"))
    #         theta_res = int(cv2.getTrackbarPos("theta_res", "hough lines conversion parameter P"))
    #         threshold = int(cv2.getTrackbarPos("threshold", "hough lines conversion parameter P"))
    #         minLineLength = int(cv2.getTrackbarPos("minLineLength", "hough lines conversion parameter P"))
    #         maxLineGap = int(cv2.getTrackbarPos("maxLineGap", "hough lines conversion parameter P"))

    #         colorB = int(cv2.getTrackbarPos("colorB", "hough lines conversion parameter P"))
    #         colorG = int(cv2.getTrackbarPos("colorG", "hough lines conversion parameter P"))
    #         colorR = int(cv2.getTrackbarPos("colorR", "hough lines conversion parameter P"))

    #         dp = int(cv2.getTrackbarPos("rho_res", "conversion parameter"))
    #         minDist = int(cv2.getTrackbarPos("theta_res", "conversion parameter"))
    #         param1 = int(cv2.getTrackbarPos("param1", "conversion parameter"))
    #         param2 = int(cv2.getTrackbarPos("param2", "conversion parameter"))
    #         minRadius = int(cv2.getTrackbarPos("minRadius", "conversion parameter"))
    #         maxRadius = int(cv2.getTrackbarPos("maxRadius", "conversion parameter"))

    #         pictureAfterCanny = cv2.Canny(pictureP2, threshold1, threshold2, apertureSize=3, L2gradient=False)
    #         pictureAfterCannyBGR = cv2.cvtColor( pictureAfterCanny, cv2.COLOR_GRAY2BGR)

    #         linesP = cv2.HoughLinesP(pictureAfterCanny, rho_res, theta_res * np.pi / 180, threshold, None, minLineLength, maxLineGap)
    #         circles = cv2.HoughCircles(pictureAfterCanny, cv2.HOUGH_GRADIENT, dp, minDist, param1, param2, minRadius, maxRadius)
    #         circles = np.uint16(np.around(circles))

    #         if linesP is not None:
    #             for i in range(0, len(linesP)):
    #                 l = linesP[i][0]
    #                 cv2.line(pictureAfterCannyBGR, (l[0], l[1]), (l[2], l[3]), (colorB, colorG, colorR), 3, cv2.LINE_AA)

    #         if circles is not None:
    #             for i in circles[0, :]:
    #                 # draw the outer circle
    #                 cv2.circle(pictureAfterCannyBGR, (i[0], i[1]), i[2], (255 - colorB, colorG, 255 - colorR), 2)
    #                 # draw the center of the circle
    #                 cv2.circle(pictureAfterCannyBGR, (i[0], i[1]), 2, (colorB, 255 - colorG, colorR), 3)

    #         cv2.imshow("result of hough circle transform", pictureAfterCannyBGR)

    #     except cv2.error:
    #         pass

    #     if cv2.waitKey(1) == ord('q'):
    #         break

    # cv2.destroyAllWindows()

    # задание 3

    video = cv2.VideoCapture('lr5/road.mp4')

    createTrackbarForCannyAndHoughLinesP()

    while True:

        try:

            _, picture = video.read()
            picture = cv2.resize(picture, (picture.shape[1] // 2, picture.shape[0] // 2))
            picture = cv2.cvtColor(picture, cv2.COLOR_BGR2GRAY)

            threshold1 = int(cv2.getTrackbarPos("threshold1", "hough lines conversion parameter P"))
            threshold2 = int(cv2.getTrackbarPos("threshold2", "hough lines conversion parameter P"))

            rho_res = int(cv2.getTrackbarPos("rho_res", "hough lines conversion parameter P"))
            theta_res = int(cv2.getTrackbarPos("theta_res", "hough lines conversion parameter P"))
            threshold = int(cv2.getTrackbarPos("threshold", "hough lines conversion parameter P"))
            minLineLength = int(cv2.getTrackbarPos("minLineLength", "hough lines conversion parameter P"))
            maxLineGap = int(cv2.getTrackbarPos("maxLineGap", "hough lines conversion parameter P"))

            colorB = int(cv2.getTrackbarPos("colorB", "hough lines conversion parameter P"))
            colorG = int(cv2.getTrackbarPos("colorG", "hough lines conversion parameter P"))
            colorR = int(cv2.getTrackbarPos("colorR", "hough lines conversion parameter P"))

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

        except AttributeError:
            break
        except cv2.error:
            pass

    # cv2.destroyAllWindows()

    # задание 4

    # pictureP4 = cv2.imread('lr7/pictureP4.jpg', cv2.IMREAD_GRAYSCALE)

    # while True:

    #     cv2.imshow("original", pictureP4)

    #     if cv2.waitKey(1) == ord('q'):
    #         break

    # cv2.destroyAllWindows()

    # createTrackbarForCannyAndHoughLinesP()

    # while True:

    #     try:

    #         threshold1 = int(cv2.getTrackbarPos("threshold1", "hough lines conversion parameter P"))
    #         threshold2 = int(cv2.getTrackbarPos("threshold2", "hough lines conversion parameter P"))

    #         rho_res = int(cv2.getTrackbarPos("rho_res", "hough lines conversion parameter P"))
    #         theta_res = int(cv2.getTrackbarPos("theta_res", "hough lines conversion parameter P"))
    #         threshold = int(cv2.getTrackbarPos("threshold", "hough lines conversion parameter P"))
    #         minLineLength = int(cv2.getTrackbarPos("minLineLength", "hough lines conversion parameter P"))
    #         maxLineGap = int(cv2.getTrackbarPos("maxLineGap", "hough lines conversion parameter P"))

    #         colorB = int(cv2.getTrackbarPos("colorB", "hough lines conversion parameter P"))
    #         colorG = int(cv2.getTrackbarPos("colorG", "hough lines conversion parameter P"))
    #         colorR = int(cv2.getTrackbarPos("colorR", "hough lines conversion parameter P"))

    #         pictureAfterCanny = cv2.Canny(pictureP4, threshold1, threshold2, apertureSize=3, L2gradient=False)
    #         pictureAfterCannyBGR = cv2.cvtColor( pictureAfterCanny, cv2.COLOR_GRAY2BGR)
    #         linesP = cv2.HoughLinesP(pictureAfterCanny, rho_res, theta_res * np.pi / 180, threshold, None, minLineLength, maxLineGap)

    #         if linesP is not None:
    #             for i in range(0, len(linesP)):
    #                 l = linesP[i][0]
    #                 cv2.line(pictureAfterCannyBGR, (l[0], l[1]), (l[2], l[3]), (colorB, colorG, colorR), 3, cv2.LINE_AA)

    #         cv2.imshow("result of probabilistic line transform", pictureAfterCannyBGR)

    #     except cv2.error:
    #         pass

    #     if cv2.waitKey(1) == ord('q'):
    #         break

    # cv2.destroyAllWindows()

    # задание 5

    picture7_5_X = cv2.imread('lr7/7_5_1.jpg', cv2.IMREAD_GRAYSCALE)
    picture7_5_X = cv2.resize(picture7_5_X, (picture7_5_X.shape[1] // 6, picture7_5_X.shape[0] // 6))

    while True:

        cv2.imshow("original", picture7_5_X)

        if cv2.waitKey(1) == ord('q'):
            break

    cv2.destroyAllWindows()

    createTrackbarForCannyAndHoughLinesP()
    createTrackbarForCircles()

    while True:

        try:

            threshold1 = int(cv2.getTrackbarPos("threshold1", "hough lines conversion parameter P"))
            threshold2 = int(cv2.getTrackbarPos("threshold2", "hough lines conversion parameter P"))

            colorB = int(cv2.getTrackbarPos("colorB", "hough lines conversion parameter P"))
            colorG = int(cv2.getTrackbarPos("colorG", "hough lines conversion parameter P"))
            colorR = int(cv2.getTrackbarPos("colorR", "hough lines conversion parameter P"))

            dp = int(cv2.getTrackbarPos("rho_res", "conversion parameter"))
            minDist = int(cv2.getTrackbarPos("theta_res", "conversion parameter"))
            param1 = int(cv2.getTrackbarPos("param1", "conversion parameter"))
            param2 = int(cv2.getTrackbarPos("param2", "conversion parameter"))
            minRadius = int(cv2.getTrackbarPos("minRadius", "conversion parameter"))
            maxRadius = int(cv2.getTrackbarPos("maxRadius", "conversion parameter"))

            pictureAfterCanny = cv2.Canny(picture7_5_X, threshold1, threshold2, apertureSize=3, L2gradient=False)
            pictureAfterCannyBGR = cv2.cvtColor( pictureAfterCanny, cv2.COLOR_GRAY2BGR)

            circles = cv2.HoughCircles(pictureAfterCanny, cv2.HOUGH_GRADIENT, dp, minDist, param1, param2, minRadius, maxRadius)
            circles = np.uint16(np.around(circles))

            if circles is not None:
                for i in circles[0, :]:
                    # draw the outer circle
                    cv2.circle(pictureAfterCannyBGR, (i[0], i[1]), i[2], (255 - colorB, colorG, 255 - colorR), 2)
                    # draw the center of the circle
                    cv2.circle(pictureAfterCannyBGR, (i[0], i[1]), 2, (colorB, 255 - colorG, colorR), 3)

            cv2.imshow("result of hough circle transform", pictureAfterCannyBGR)

        except cv2.error:
            pass

        if cv2.waitKey(1) == ord('q'):
            break

    cv2.destroyAllWindows()