import cv2
import numpy as np
import math

#задание 1 ВАРИАНТ 1

# пункт 1
me = cv2.imread('lr1/me.jpg')
cv2.imshow('me', me)
cv2.waitKey(1000)
cv2.destroyAllWindows()
# пункт 2
meGray = cv2.cvtColor(me, cv2.COLOR_BGR2GRAY)
cv2.imshow('me gray', meGray)
cv2.waitKey(2000)
cv2.destroyAllWindows()
# пункт 3
meSmall = cv2.resize(me, (me.shape[1] // 2, me.shape[0] // 2))
cv2.imshow('me small', meSmall)
cv2.waitKey(3000)
cv2.destroyAllWindows()
# пункт 4
meGraySmall = cv2.resize(meGray, (me.shape[1] // 4, me.shape[0] // 4))
cv2.imshow('me gray small', meGraySmall)
cv2.waitKey(4000)
cv2.destroyAllWindows()
# пункт 5
b, g, r = cv2.split(me)
meInvers = cv2.merge([b, r, g])
cv2.imshow('me invers', meInvers)
cv2.waitKey(5000)
cv2.destroyAllWindows()

#задание 1 ВАРИАНТ 2

# пункт 1
me = cv2.imread('lr1/me.jpg', flags = cv2.IMREAD_REDUCED_COLOR_4 )
cv2.imshow('me', me)
cv2.waitKey(1000)
cv2.destroyAllWindows()
# пункт 2
meGray = cv2.cvtColor(me, cv2.COLOR_BGR2GRAY)
cv2.imshow('me gray', meGray)
cv2.waitKey(2000)
cv2.destroyAllWindows()
# пункт 3
meSmall = cv2.resize(me, (me.shape[1] // 2, me.shape[0] // 2))
cv2.imshow('me small', meSmall)
cv2.waitKey(3000)
cv2.destroyAllWindows()
# пункт 4
meGraySmall = cv2.resize(meGray, (me.shape[1] // 4, me.shape[0] // 4))
cv2.imshow('me gray small', meGraySmall)
cv2.waitKey(4000)
cv2.destroyAllWindows()
# пункт 5
b, g, r = cv2.split(me)
meInvers = cv2.merge([b, r, g])
cv2.imshow('me invers', meInvers)
cv2.waitKey(5000)
cv2.destroyAllWindows()

#задание 2

myPicture = np.zeros((480, 640, 3), dtype='uint8')
myPicture[:] = 255, 255, 255
cv2.circle(myPicture, (myPicture.shape[0] // 2, myPicture.shape[1] // 2), 30, (0, 0, 255), 3)
cv2.putText(myPicture, 'circle', (myPicture.shape[0] // 2 + 50, myPicture.shape[1] // 2), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 0, 0), 2)
cv2.rectangle(myPicture, (250, 50), (300, 150), (255, 0, 139), 3)
cv2.putText(myPicture, 'rectangle', (320, 100), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 0, 0), 2)
cv2.line(myPicture, (0, 0), (myPicture.shape[1], myPicture.shape[0]), (255, 191, 0), 3)
cv2.putText(myPicture, 'line', (myPicture.shape[0] // 2 - 200, myPicture.shape[1] // 2 - 200), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 0, 0), 2)
cv2.imshow('my picture', myPicture)
cv2.waitKey(5000)
cv2.destroyAllWindows()

#задание 3

n = int(40)
m = int(15)
myChess = np.zeros((40, 15, 3), dtype='uint8')
for i in range(n+1):
    for j in range(m+1):
        if (j+i) % 2 == 0:
            cv2.rectangle(myChess, (j, i), (j, i), (255, 0, 139), 3)
        else:
            cv2.rectangle(myChess, (j, i), (j, i), (255, 255, 255), 3)
myChessResize = cv2.resize(myChess, (myChess.shape[1] * 10, myChess.shape[0] * 10), interpolation=cv2.INTER_AREA)
cv2.imshow('my_chess', myChessResize)
cv2.waitKey(5000)
cv2.destroyAllWindows()

# доп задание

myCam = cv2.VideoCapture(0)
myCam.set(3, 500)
myCam.set(4, 300)
while True:
    success, frame = myCam.read()
    frameGray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    cv2.imshow('myCamGray', frameGray)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break