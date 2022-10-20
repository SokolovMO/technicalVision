import cv2
import numpy as np

def nothing(x):
    pass

picture = cv2.imread('lr4/picture.jpg')

while True:
    cv2.imshow('picture', picture)
    if cv2.waitKey(1) == ord('q'):
        break

cv2.destroyWindow('picture')

cv2.namedWindow("conversion parameter")
cv2.createTrackbar("iterations", "conversion parameter", 0, 10, nothing)
cv2.moveWindow("conversion parameter", 0, 800)
cv2.resizeWindow("conversion parameter", 500, 50)

kernel = np.ones((3, 3), 'uint8')

while True:

    iter4tions = int(cv2.getTrackbarPos("iterations", "conversion parameter"))

    pictureDilate = cv2.dilate(picture, kernel, iterations=iter4tions)
    cv2.imshow('pictureDilate', pictureDilate)
    if cv2.waitKey(1) == ord('q'):
        break

cv2.imwrite('lr4/pictureDilate.jpg', pictureDilate)
cv2.destroyWindow('pictureDilate')

while True:

    iter4tions = int(cv2.getTrackbarPos("iterations", "conversion parameter"))

    pictureErode = cv2.erode(picture, kernel, iterations=iter4tions)
    cv2.imshow('pictureErode', pictureErode)
    if cv2.waitKey(1) == ord('q'):
        break

cv2.imwrite('lr4/pictureErode.jpg', pictureErode)
cv2.destroyWindow('pictureErode')

while True:

    iter4tions = int(cv2.getTrackbarPos("iterations", "conversion parameter"))

    pictureMorphologyEx = cv2.morphologyEx(picture, cv2.MORPH_OPEN, kernel, iterations=iter4tions)
    cv2.imshow('pictureMorphologyEx', pictureMorphologyEx)
    if cv2.waitKey(1) == ord('q'):
        break