import cv2
import numpy as np

def nothing(x):
    pass

def createTrackbar():
    cv2.namedWindow("conversion parameter")

    cv2.createTrackbar("threshold1canny", "conversion parameter", 0, 255, nothing)
    cv2.createTrackbar("threshold2canny", "conversion parameter", 0, 255, nothing)
    cv2.createTrackbar("thickness", "conversion parameter", 0, 50, nothing)
    
    cv2.moveWindow("conversion parameter", 960, 100)


if __name__ == "__main__":

    createTrackbar()

    picture = cv2.imread('lr6/picture.png', cv2.IMREAD_GRAYSCALE)
    picture = cv2.resize(picture, (picture.shape[1] // 2, picture.shape[0] // 2))
    picture = cv2.blur(picture, (3,3))

    while True:

        threshold1canny = int(cv2.getTrackbarPos("threshold1canny", "conversion parameter"))
        threshold2canny = int(cv2.getTrackbarPos("threshold2canny", "conversion parameter"))
        thickness = int(cv2.getTrackbarPos("thickness", "conversion parameter"))

        pictureCanny = cv2.Canny(picture, threshold1canny, threshold2canny, apertureSize=3, L2gradient=False)

        contours, hierarchy = cv2.findContours(pictureCanny, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

        contours_poly = [None]*len(contours)
        boundRect = [None]*len(contours)
        centers = [None]*len(contours)
        radius = [None]*len(contours)

        for i, c in enumerate(contours):
            contours_poly[i] = cv2.approxPolyDP(c, 3, True)
            boundRect[i] = cv2.boundingRect(contours_poly[i])
            centers[i], radius[i] = cv2.minEnclosingCircle(contours_poly[i])

        result = np.zeros((pictureCanny.shape[0], pictureCanny.shape[1], 3), dtype=np.uint8)

        for i in range(len(contours)):

            # boundRect[i][0] - x
            # boundRect[i][1] - y
            # boundRect[i][2] - w
            # boundRect[i][3] - h
            # centers[i][0] - x
            # centers[i][1] - y
            # radius[i] - r

            factP = cv2.arcLength(contours_poly[i], True)
            boundRestP = 2 * (boundRect[i][2] + boundRect[i][3])
            boundCircP = 2 * 3.141 * radius[i]

            if factP/boundRestP >= 0.95 and factP/boundRestP <= 1.05:
                color = (255, 255, 0)
            elif factP/boundCircP >= 0.95 and factP/boundCircP <= 1.05:
                color = (0, 0, 255)
            else:
                color = (255, 0, 255)
            cv2.drawContours(result, contours, i, color, thickness)

        cv2.imshow('result', result)
        cv2.imshow('pictureAfterCanny', pictureCanny)
        cv2.imshow('picture', picture)

        if cv2.waitKey(1) == ord('q'):
            break