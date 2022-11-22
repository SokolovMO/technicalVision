import cv2
# import numpy as np
import random
import time

pattern_color = cv2.imread('lr8/pattern.png', cv2.IMREAD_COLOR)
pattern = cv2.cvtColor(pattern_color, cv2.COLOR_BGR2GRAY)
pattern = 255 - pattern
pattern = cv2.GaussianBlur(pattern, (3, 3), 0)

img_color = cv2.imread('lr8/task.png', cv2.IMREAD_COLOR)
img = cv2.cvtColor(img_color, cv2.COLOR_BGR2GRAY)
img = 255 - img
img = cv2.GaussianBlur(img, (3, 3), 0)

contours_pattern, _ = cv2.findContours(pattern, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_NONE)
contours_img, _ = cv2.findContours(img, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_NONE)

m10 = cv2.moments(contours_pattern[0])
hu10 = cv2.HuMoments(m10)

if __name__ == "__main__":

    while True:

        color = random.randint(0,255), random.randint(0,255), random.randint(0,255)

        for i in range(len(contours_img)):
            
            m2i = cv2.moments(contours_img[i])
            hu2i = cv2.HuMoments(m2i)

            if abs((hu10[0] - hu2i[0]) / hu10[0]) <= 0.04:
                if abs((m10['m00'] - m2i['m00']) / m10['m00']) <= 0.01:
                    if not abs((m10['mu20'] - m2i['mu20']) / m10['mu20']) <= 0.01:
                        cv2.drawContours(img_color, contours_img, i, color, 5)

        cv2.imshow('result', img_color)

        time.sleep(0.25)

        if cv2.waitKey(1) == ord('q'):
                    break