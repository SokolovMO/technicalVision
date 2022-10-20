import cv2
import numpy as np

def nothing(x):
    pass

picture = cv2.imread('lr4/prikoldesy.jpg')

while True:
    cv2.imshow('prikoldesy', picture)
    if cv2.waitKey(1) == ord('q'):
        break

cv2.namedWindow("conversion parameter")
cv2.createTrackbar("iterations", "conversion parameter", 1, 10, nothing)
cv2.moveWindow("conversion parameter", 0, 800)
cv2.resizeWindow("conversion parameter", 500, 50)

kernel = np.ones((3, 3), 'uint8')

while True:

    iter4tions = int(cv2.getTrackbarPos("iterations", "conversion parameter"))

    pictureDilate = cv2.dilate(picture, kernel, iterations=iter4tions)
    cv2.imshow('prikoldesyDilate', pictureDilate)
    if cv2.waitKey(1) == ord('q'):
        break

cv2.imwrite('lr4/prikoldesyDilate.jpg', pictureDilate)

# pictureMorphologyEx = cv2.morphologyEx(picture,