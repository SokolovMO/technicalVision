import cv2
import numpy as np
import math

# задача 1

t = input("введите температуру на улице в градусах Цельсия: ")
t=float(t)
Wind = input("введите скорость ветра в м/с: ")
Wind = float(Wind)
while True:
    Rain = input("вцените дождь на улице от 0 до 5 (баллов): ")
    if not 0 <= float(Rain) <= 5:
        print("вы ввели число вне диапазона. попробуйте снова")
    else:
        Rain = float(Rain)
        break
otsenka = 0
if t > 30 or t < -10:
    print("\nтемпература не комфортная для прогулки")
    otsenka = otsenka+1
else:
    print("\nхорошая температура")
if Wind > 15:
    print("ветер слишком сильный")
    otsenka = otsenka+1
elif Wind > 8:
    print("советую надеть ветровку")
    otsenka = otsenka+0.5
else:
    print("ветер не помешает прогулке")
if Rain == 0:
    print("дождя нет")
elif Rain < 3:
    print("советую захватить с собой зонт")
else:
    print("намечается гроза")
print("\nИтого ")
if otsenka == 0:
    print("можно идти на прогулку")
elif otsenka < 2:
    print("можно идти на прогулку при большом желании")
else:
    print("прогулка может испортить вам настроение и одежду")

# задача 2

import math
lisT = [11, 5, 8, 32, 15, 3, 20, 132, 21, 4, 555, 9, 20]
suM = 0
for i in lisT:
    if i < 30 and i % 3 == 0:
        print(i)
    else:
         suM = suM+i
print(suM)

# задача 3

import math
def date(year, month, day):
    feedback = False
    if type(year) == int and  type(month) == int and type(day) == int and year > 0:
        if month in [1, 3, 5, 7, 8, 10, 12] and 32 > day > 0:
            feedback = True
        elif month in [4, 5, 9, 11] and 31 > day > 0:
            feedback = True
        elif month == 2 and (29+(year % 4 == 0)) > day > 0:
            feedback = True
    return feedback

# задача 4

n = input("введите желаемое число строк, n: ")
n = int(n)
m = input("введите желаемое число столбцов, m: ")
m = int(m)
Array=[0] * n
for i in range(n):
    Array[i] = [0] * m
for i in range(n):
    for j in range(m):
        Array[i][j] = 5-(j+i)%2
for i in range(n):
    print(Array[i])

# задача 5

n = input('введите число: ')
print('развернутое число:',n[::-1])