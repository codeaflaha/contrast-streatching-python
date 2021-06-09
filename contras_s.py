import cv2
from copy import deepcopy

def setGraycolor(color) :
    return [color, color, color]
  
img = cv2.imread('lena.jpg')
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
  

hasil = deepcopy(img)
r1 = 100
r2 = 150
s1 =50
s2 = 200

for i in range(len(img)):
    for j in range(len(img[i])):
        x = gray[i][j]
        if(0 <= x and x <= r1):
            hasil[i][j] = setGraycolor(s1/r1*x)
        elif(r1 < x and x <= r2):
            hasil[i][j] = setGraycolor(((s2-s1)/(r2-r1))*(x-r1)+s1)
        elif(r2 < x and x <= 255):
            hasil[i][j] = setGraycolor(((255-s2)/(255-r2))*(x-r2)+s2)

cv2.imshow('Original image',img)
cv2.imshow('Gray image', gray)
cv2.imshow('Contrast Streaching', hasil)

cv2.waitKey(0)
cv2.destroyAllWindows()