import cv2
import numpy as np

def nothing(x):
    pass

def Dilate(picture):
    iter4tions = int(cv2.getTrackbarPos("iterations", "conversion parameter"))
    kernelSize = int(cv2.getTrackbarPos("kernelSize", "conversion parameter"))
    kernel = np.ones((kernelSize, kernelSize), 'uint8')
    pictureDilate = cv2.dilate(picture, kernel, iterations=iter4tions)
    return pictureDilate

def Erode(picture):
    iter4tions = int(cv2.getTrackbarPos("iterations", "conversion parameter"))
    kernelSize = int(cv2.getTrackbarPos("kernelSize", "conversion parameter"))
    kernel = np.ones((kernelSize, kernelSize), 'uint8')
    pictureErode = cv2.erode(picture, kernel, iterations=iter4tions)
    return pictureErode

def MORPH_OPEN(picture):
    iter4tions = int(cv2.getTrackbarPos("iterations", "conversion parameter"))
    kernelSize = int(cv2.getTrackbarPos("kernelSize", "conversion parameter"))
    kernel = np.ones((kernelSize, kernelSize), 'uint8')
    pictureMORPH_OPEN = cv2.morphologyEx(picture, cv2.MORPH_OPEN, kernel, iterations=iter4tions)
    return pictureMORPH_OPEN

def MORPH_CLOSE(picture):
    iter4tions = int(cv2.getTrackbarPos("iterations", "conversion parameter"))
    kernelSize = int(cv2.getTrackbarPos("kernelSize", "conversion parameter"))
    kernel = np.ones((kernelSize, kernelSize), 'uint8')
    pictureMORPH_CLOSE = cv2.morphologyEx(picture, cv2.MORPH_CLOSE, kernel, iterations=iter4tions)
    return pictureMORPH_CLOSE

def MORPH_GRADIENT(picture):
    iter4tions = int(cv2.getTrackbarPos("iterations", "conversion parameter"))
    kernelSize = int(cv2.getTrackbarPos("kernelSize", "conversion parameter"))
    kernel = np.ones((kernelSize, kernelSize), 'uint8')
    pictureMORPH_GRADIENT = cv2.morphologyEx(picture, cv2.MORPH_GRADIENT, kernel, iterations=iter4tions)
    return pictureMORPH_GRADIENT

def MORPH_TOPHAT(picture):
    iter4tions = int(cv2.getTrackbarPos("iterations", "conversion parameter"))
    kernelSize = int(cv2.getTrackbarPos("kernelSize", "conversion parameter"))
    kernel = np.ones((kernelSize, kernelSize), 'uint8')
    pictureMORPH_TOPHAT = cv2.morphologyEx(picture, cv2.MORPH_TOPHAT, kernel, iterations=iter4tions)
    return pictureMORPH_TOPHAT

def MORPH_BLACKHAT(picture):
    iter4tions = int(cv2.getTrackbarPos("iterations", "conversion parameter"))
    kernelSize = int(cv2.getTrackbarPos("kernelSize", "conversion parameter"))
    kernel = np.ones((kernelSize, kernelSize), 'uint8')
    pictureMORPH_BLACKHAT = cv2.morphologyEx(picture, cv2.MORPH_BLACKHAT, kernel, iterations=iter4tions)
    return pictureMORPH_BLACKHAT

def morphologyEx(picture):

    iter4tions = int(cv2.getTrackbarPos("iterations", "conversion parameter"))
    kernelSize = int(cv2.getTrackbarPos("kernelSize", "conversion parameter"))
    conversionType = int(cv2.getTrackbarPos("conversionType", "conversion parameter"))
    kernel = np.ones((kernelSize, kernelSize), 'uint8')

    if conversionType == 1:
        pictureMorphologyEx = cv2.morphologyEx(picture, cv2.MORPH_OPEN, kernel, iterations=iter4tions)
    elif conversionType == 2:
        pictureMorphologyEx = cv2.morphologyEx(picture, cv2.MORPH_CLOSE, kernel, iterations=iter4tions)
    elif conversionType == 3:
        pictureMorphologyEx = cv2.morphologyEx(picture, cv2.MORPH_GRADIENT, kernel, iterations=iter4tions)
    elif conversionType == 4:
        pictureMorphologyEx = cv2.morphologyEx(picture, cv2.MORPH_TOPHAT, kernel, iterations=iter4tions)
    elif conversionType == 5:
        pictureMorphologyEx = cv2.morphologyEx(picture, cv2.MORPH_TOPHAT, kernel, iterations=iter4tions)
    else:
        print("поставьте ползунок в положение 1-5")

    return pictureMorphologyEx

def createTrackbar1():
    cv2.namedWindow("conversion parameter")
    cv2.createTrackbar("iterations", "conversion parameter", 1, 10, nothing)
    cv2.createTrackbar("kernelSize", "conversion parameter", 1, 10, nothing)
    cv2.moveWindow("conversion parameter", 0, 800)
    cv2.resizeWindow("conversion parameter", 500, 50)

def createTrackbar2():
    cv2.namedWindow("conversion parameter")
    cv2.createTrackbar("iterations", "conversion parameter", 1, 10, nothing)
    cv2.createTrackbar("kernelSize", "conversion parameter", 1, 10, nothing)
    cv2.createTrackbar("conversionType", "conversion parameter", 1, 5, nothing)
    cv2.moveWindow("conversion parameter", 0, 800)
    cv2.resizeWindow("conversion parameter", 500, 50)

picture = cv2.imread('lr4/picture.jpg')

# original

while True:
    cv2.imshow('picture', picture)
    if cv2.waitKey(1) == ord('q'):
        break

cv2.destroyWindow('picture')

createTrackbar1()

# dilate

while True:

    pictureDilate = Dilate(picture)
    cv2.imshow('pictureDilate', pictureDilate)
    if cv2.waitKey(1) == ord('q'):
        break

cv2.imwrite('lr4/pictureDilate.jpg', pictureDilate)
cv2.destroyWindow('pictureDilate')

#  erode

while True:

    pictureErode = Erode(picture)
    cv2.imshow('pictureErode', pictureErode)
    if cv2.waitKey(1) == ord('q'):
        break

cv2.imwrite('lr4/pictureErode.jpg', pictureErode)
cv2.destroyWindow('pictureErode')
cv2.destroyWindow('conversion parameter')

createTrackbar1()

# morphologyEx

while True:

    pictureMorphologyEx = morphologyEx(picture)
    cv2.imshow('pictureMorphologyEx', pictureMorphologyEx)
    if cv2.waitKey(1) == ord('q'):
        break

cv2.imwrite('lr4/pictureMorphologyEx.jpg', pictureMorphologyEx)
cv2.destroyAllWindows()