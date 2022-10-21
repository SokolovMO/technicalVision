import cv2
import numpy as np

def nothing(x):
    pass

def morphologyTransform(picture, kernel, iter4tions, conversionType):

    if conversionType == 0:
        pictureMorphologyTransform = picture
    elif conversionType == 1:
        pictureMorphologyTransform = cv2.dilate(picture, kernel, iterations=iter4tions)
    elif conversionType == 2:
        pictureMorphologyTransform = cv2.erode(picture, kernel, iterations=iter4tions)
    elif conversionType == 3:
        pictureMorphologyTransform = cv2.morphologyEx(picture, cv2.MORPH_OPEN, kernel, iterations=iter4tions)
    elif conversionType == 4:
        pictureMorphologyTransform = cv2.morphologyEx(picture, cv2.MORPH_CLOSE, kernel, iterations=iter4tions)
    elif conversionType == 5:
        pictureMorphologyTransform = cv2.morphologyEx(picture, cv2.MORPH_GRADIENT, kernel, iterations=iter4tions)
    elif conversionType == 6:
        pictureMorphologycv2.destroyWindow('picture')Transform = cv2.morphologyEx(picture, cv2.MORPH_TOPHAT, kernel, iterations=iter4tions)
    elif conversionType == 7:
        pictureMorphologyTransform = cv2.morphologyEx(picture, cv2.MORPH_BLACKHAT, kernel, iterations=iter4tions)

    return pictureMorphologyTransform

def createTrackbar():
    cv2.namedWindow("conversion parameter")
    cv2.createTrackbar("iterations", "conversion parameter", 1, 10, nothing)
    cv2.createTrackbar("kernelSize", "conversion parameter", 1, 10, nothing)
    cv2.createTrackbar("conversionType", "conversion parameter", 0, 7, nothing)
    cv2.moveWindow("conversion parameter", 0, 800)
    cv2.resizeWindow("conversion parameter", 500, 50)

picture = cv2.imread('lr4/picture.jpg')

createTrackbar()

while True:

    iter4tions = int(cv2.getTrackbarPos("iterations", "conversion parameter"))
    kernelSize = int(cv2.getTrackbarPos("kernelSize", "conversion parameter"))
    conversionType = int(cv2.getTrackbarPos("conversionType", "conversion parameter"))
    kernel = np.ones((kernelSize, kernelSize), 'uint8')
    pictureMorphologyTransform = morphologyTransform(picture, kernel, iter4tions, conversionType)
    cv2.putText(pictureMorphologyTransform, 'select transform type', (10, 20), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 255, 0), 2)
    cv2.putText(pictureMorphologyTransform, '0 - ORIGINAL', (10, 20 + 20), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 255, 0), 2)
    cv2.putText(pictureMorphologyTransform, '1 - DILATE', (10, 20 + 40), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 255, 0), 2)
    cv2.putText(pictureMorphologyTransform, '2 - ERODE', (10, 20 + 60), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 255, 0), 2)
    cv2.putText(pictureMorphologyTransform, '3 - OPEN', (10, 20 + 80), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 255, 0), 2)
    cv2.putText(pictureMorphologyTransform, '4 - CLOSE', (10, 20 + 100), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 255, 0), 2)
    cv2.putText(pictureMorphologyTransform, '5 - GRADIENT', (10, 20 + 120), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 255, 0), 2)
    cv2.putText(pictureMorphologyTransform, '6 - TOPHAT', (10, 20 + 140), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 255, 0), 2)
    cv2.putText(pictureMorphologyTransform, '7 - BLACKHAT', (10, 20 + 160), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 255, 0), 2)
    cv2.imshow('pictureMorphologyEx', pictureMorphologyTransform)
    if cv2.waitKey(1) == ord('q'):
        break

cv2.imwrite('lr4/pictureMorphologyEx.jpg', pictureMorphologyTransform)
cv2.destroyAllWindows()