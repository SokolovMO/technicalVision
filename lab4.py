import cv2
import numpy as np

def nothing(x):
    pass

picture = cv2.imread('lr4/picture.jpg')

# original

while True:
    cv2.imshow('picture', picture)
    if cv2.waitKey(1) == ord('q'):
        break

cv2.destroyWindow('picture')

cv2.namedWindow("conversion parameter")
cv2.createTrackbar("iterations", "conversion parameter", 1, 10, nothing)
cv2.createTrackbar("kernelSize", "conversion parameter", 1, 10, nothing)

cv2.moveWindow("conversion parameter", 0, 800)
cv2.resizeWindow("conversion parameter", 500, 50)

# dilate

while True:

    iter4tions = int(cv2.getTrackbarPos("iterations", "conversion parameter"))
    kernelSize = int(cv2.getTrackbarPos("kernelSize", "conversion parameter"))
    kernel = np.ones((kernelSize, kernelSize), 'uint8')
    pictureDilate = cv2.dilate(picture, kernel, iterations=iter4tions)
    cv2.imshow('pictureDilate', pictureDilate)
    if cv2.waitKey(1) == ord('q'):
        break

cv2.imwrite('lr4/pictureDilate.jpg', pictureDilate)
cv2.destroyWindow('pictureDilate')

#  erode

while True:

    iter4tions = int(cv2.getTrackbarPos("iterations", "conversion parameter"))
    kernelSize = int(cv2.getTrackbarPos("kernelSize", "conversion parameter"))
    kernel = np.ones((kernelSize, kernelSize), 'uint8')
    pictureErode = cv2.erode(picture, kernel, iterations=iter4tions)
    cv2.imshow('pictureErode', pictureErode)
    if cv2.waitKey(1) == ord('q'):
        break

cv2.imwrite('lr4/pictureErode.jpg', pictureErode)
cv2.destroyWindow('pictureErode')

# OPEN

while True:

    iter4tions = int(cv2.getTrackbarPos("iterations", "conversion parameter"))
    kernelSize = int(cv2.getTrackbarPos("kernelSize", "conversion parameter"))
    kernel = np.ones((kernelSize, kernelSize), 'uint8')
    pictureMORPH_OPEN = cv2.morphologyEx(picture, cv2.MORPH_OPEN, kernel, iterations=iter4tions)
    cv2.imshow('pictureMORPH_OPEN', pictureMORPH_OPEN)
    if cv2.waitKey(1) == ord('q'):
        break

cv2.imwrite('lr4/pictureMORPH_OPEN.jpg', pictureMORPH_OPEN)
cv2.destroyWindow('pictureMORPH_OPEN')

# CLOSE

while True:

    iter4tions = int(cv2.getTrackbarPos("iterations", "conversion parameter"))
    kernelSize = int(cv2.getTrackbarPos("kernelSize", "conversion parameter"))
    kernel = np.ones((kernelSize, kernelSize), 'uint8')
    pictureMORPH_CLOSE = cv2.morphologyEx(picture, cv2.MORPH_CLOSE, kernel, iterations=iter4tions)
    cv2.imshow('pictureMORPH_CLOSE', pictureMORPH_CLOSE)
    if cv2.waitKey(1) == ord('q'):
        break

cv2.imwrite('lr4/pictureMORPH_CLOSE.jpg', pictureMORPH_CLOSE)
cv2.destroyWindow('pictureMORPH_CLOSE')

# GRADIENT

while True:

    iter4tions = int(cv2.getTrackbarPos("iterations", "conversion parameter"))
    kernelSize = int(cv2.getTrackbarPos("kernelSize", "conversion parameter"))
    kernel = np.ones((kernelSize, kernelSize), 'uint8')
    pictureMORPH_GRADIENT = cv2.morphologyEx(picture, cv2.MORPH_GRADIENT, kernel, iterations=iter4tions)
    cv2.imshow('pictureMORPH_GRADIENT', pictureMORPH_GRADIENT)
    if cv2.waitKey(1) == ord('q'):
        break

cv2.imwrite('lr4/pictureMORPH_GRADIENT.jpg', pictureMORPH_GRADIENT)
cv2.destroyWindow('pictureMORPH_GRADIENT')

# TOPHAT

while True:

    iter4tions = int(cv2.getTrackbarPos("iterations", "conversion parameter"))
    kernelSize = int(cv2.getTrackbarPos("kernelSize", "conversion parameter"))
    kernel = np.ones((kernelSize, kernelSize), 'uint8')
    pictureMORPH_TOPHAT = cv2.morphologyEx(picture, cv2.MORPH_TOPHAT, kernel, iterations=iter4tions)
    cv2.imshow('pictureMORPH_TOPHAT', pictureMORPH_TOPHAT)
    if cv2.waitKey(1) == ord('q'):
        break

cv2.imwrite('lr4/pictureMORPH_TOPHAT.jpg', pictureMORPH_TOPHAT)
cv2.destroyWindow('pictureMORPH_TOPHAT')

# BLACKHAT

while True:

    iter4tions = int(cv2.getTrackbarPos("iterations", "conversion parameter"))
    kernelSize = int(cv2.getTrackbarPos("kernelSize", "conversion parameter"))
    kernel = np.ones((kernelSize, kernelSize), 'uint8')
    pictureMORPH_BLACKHAT = cv2.morphologyEx(picture, cv2.MORPH_BLACKHAT, kernel, iterations=iter4tions)
    cv2.imshow('pictureMORPH_BLACKHAT', pictureMORPH_BLACKHAT)
    if cv2.waitKey(1) == ord('q'):
        break

cv2.imwrite('lr4/pictureMORPH_BLACKHAT.jpg', pictureMORPH_BLACKHAT)
cv2.destroyWindow('pictureMORPH_BLACKHAT')