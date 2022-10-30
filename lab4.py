import cv2
import numpy as np
import time

def nothing(x):
    pass

def morphologyTransform(picture, kernel, iter4tions, conversionType):

    if conversionType == 0:
        pictureMorphologyTransform = picture
    elif conversionType == 1:
        pictureMorphologyTransform = cv2.dilate(picture, kernel, iterations=iter4tions) # "приклеивание" к белым областям белых областей
    elif conversionType == 2:
        pictureMorphologyTransform = cv2.erode(picture, kernel, iterations=iter4tions) # "стирание" белых областей к черным
    elif conversionType == 3:
        pictureMorphologyTransform = cv2.morphologyEx(picture, cv2.MORPH_OPEN, kernel, iterations=iter4tions) # сначала применяется эрозия, потом наращивание; если итераций несколько, они повторяются по кругу
    elif conversionType == 4:
        pictureMorphologyTransform = cv2.morphologyEx(picture, cv2.MORPH_CLOSE, kernel, iterations=iter4tions) # сначала наращивание, потом эрозия; аналогично при повторении
    elif conversionType == 5:
        pictureMorphologyTransform = cv2.morphologyEx(picture, cv2.MORPH_GRADIENT, kernel, iterations=iter4tions) # разность между результатом наращивания и результатом эрозии
    elif conversionType == 6:
        pictureMorphologyTransform = cv2.morphologyEx(picture, cv2.MORPH_TOPHAT, kernel, iterations=iter4tions) # из исходного изображения вычитается его размыкание
    elif conversionType == 7:
        pictureMorphologyTransform = cv2.morphologyEx(picture, cv2.MORPH_BLACKHAT, kernel, iterations=iter4tions) # из замыкания вычитается само изображение

    return pictureMorphologyTransform

def createTrackbar():
    cv2.namedWindow("conversion parameter")
    cv2.createTrackbar("iterations", "conversion parameter", 1, 10, nothing)
    cv2.createTrackbar("kernelSize", "conversion parameter", 1, 10, nothing)
    cv2.createTrackbar("conversionType", "conversion parameter", 0, 7, nothing)
    cv2.moveWindow("conversion parameter", 960, 100)

def helpWindow():
    background = np.full((200, 200, 3), 255, dtype='uint8')
    cv2.putText(background, 'select transform type', (10, 20), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 0, 0), 2)
    cv2.putText(background, '0 - ORIGINAL', (10, 20 + 20), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 0, 0), 2)
    cv2.putText(background, '1 - DILATE', (10, 20 + 40), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 0, 0), 2)
    cv2.putText(background, '2 - ERODE', (10, 20 + 60), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 0, 0), 2)
    cv2.putText(background, '3 - OPEN', (10, 20 + 80), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 0, 0), 2)
    cv2.putText(background, '4 - CLOSE', (10, 20 + 100), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 0, 0), 2)
    cv2.putText(background, '5 - GRADIENT', (10, 20 + 120), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 0, 0), 2)
    cv2.putText(background, '6 - TOPHAT', (10, 20 + 140), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 0, 0), 2)
    cv2.putText(background, '7 - BLACKHAT', (10, 20 + 160), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 0, 0), 2)
    cv2.imshow('help', background)
    cv2.moveWindow("help", 960, 350)

picture = cv2.imread('lr4/picture.jpg', cv2.IMREAD_GRAYSCALE)

# video = cv2.VideoCapture('lr2/23.mov')

createTrackbar()

helpWindow()

while True:

    # _, picture = video.read()
    # time.sleep(0.05)
    # picture = cv2.resize(picture, (picture.shape[1] // 3, picture.shape[0] // 3))
    # picture = cv2.cvtColor(picture, cv2.COLOR_BGR2GRAY)
    # _, picture = cv2.threshold(picture, 87, 255, cv2.THRESH_BINARY)

    iter4tions = int(cv2.getTrackbarPos("iterations", "conversion parameter"))
    kernelSize = int(cv2.getTrackbarPos("kernelSize", "conversion parameter"))
    conversionType = int(cv2.getTrackbarPos("conversionType", "conversion parameter"))
    kernel = np.full((kernelSize, kernelSize), 1, dtype='uint8')
    pictureMorphologyTransform = morphologyTransform(picture, kernel, iter4tions, conversionType)
    cv2.imshow('pictureMorphologyEx', pictureMorphologyTransform)
    if cv2.waitKey(1) == ord('q'):
        break

cv2.imwrite('lr4/pictureMorphologyEx.jpg', pictureMorphologyTransform)
cv2.destroyAllWindows()