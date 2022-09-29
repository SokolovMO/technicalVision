import cv2
import numpy as np

p3_1 = cv2.imread('lr3/3-1.PNG')
p3_1blur = cv2.blur(p3_1, (5, 5))
p3_1box = cv2.boxFilter(p3_1, -1, (5, 5))
p3_1median = cv2.medianBlur(p3_1, (5, 5))


p3_1gray = cv2.cvtColor(p3_1, cv2.COLOR_BGR2GRAY)

cv2.imshow('p3_1', p3_1)
cv2.waitKey(1000)
cv2.imshow('p3_1blur', p3_1blur)
cv2.waitKey(1000)
cv2.imshow('p3_1box', p3_1box)
cv2.waitKey(1000)