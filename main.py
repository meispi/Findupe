import cv2
import numpy as np
img1 = cv2.imread('C:\\Users\\hp\\Desktop\\c_dog.1.jpg', -1)
img2 = cv2.imread('C:\\Users\\hp\\Desktop\\c_dog.2.jpg')
wt = 8
ht = 8
dim = (wt, ht)
#print(img.shape)
resized1 = cv2.resize(img1, dim, interpolation=cv2.INTER_AREA)
resized2 = cv2.resize(img2, dim, interpolation=cv2.INTER_AREA)
cv2.imwrite('C:\\Users\\hp\\Desktop\\resized1.jpg', resized1)
cv2.imwrite('C:\\Users\\hp\\Desktop\\resized2.jpg', resized2)
#print(resized.shape)
gray1 = cv2.imread('C:\\Users\\hp\\Desktop\\resized1.jpg', 0)
gray2 = cv2.imread('C:\\Users\\hp\\Desktop\\resized2.jpg', 0)
cv2.imwrite('C:\\Users\\hp\\Desktop\\gray1.jpg', gray1)
cv2.imwrite('C:\\Users\\hp\\Desktop\\gray2.jpg', gray2)
#print(gray.shape)
mean1 = np.mean(gray1)
mean2 = np.mean(gray2)
str1=''
str2=''
#print(gray)
for i in gray1:
    for j in i:
        if j -  mean1 > 0:
            str1 += '1'
        else:
            str1 += '0'

for i in gray2:
    for j in i:
        if j -  mean2 > 0:
            str2 += '1'
        else:
            str2 += '0'
val = (bin(int(str1, 2)^int(str2, 2))).count('1')
if val >= 10:
    print("Different Pictures")
else:
    print("Same pictures")