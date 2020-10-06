import cv2
import numpy as np
import os
import shutil


def isdupe(img1, img2):
    dim = (8, 8)
    rimg1 = cv2.resize(img1, dim, interpolation=cv2.INTER_AREA)
    rimg2 = cv2.resize(img2, dim, interpolation=cv2.INTER_AREA)
    mean1 = np.mean(rimg1)
    mean2 = np.mean(rimg2)
    str1 = ''
    str2 = ''
    for i in rimg1:
        for j in i:
            if j - mean1 > 0:
                str1 += '1'
            else:
                str1 += '0'

    for i in rimg2:
        for j in i:
            if j - mean2 > 0:
                str2 += '1'
            else:
                str2 += '0'
    val = (bin(int(str1, 2)^int(str2, 2))).count('1')
    if val >= 10:
        return False
    else:
        return True


src = 'path/to/images_dir'
des = 'path/to/any_dir'
images = [f for f in os.listdir(src)]
check = [False]*len(images)
flag = True
flag2 = True

for img1 in images:
    if (not check[images.index(img1)]) and images.index(img1) != len(images)-1:
        #shutil.copy(src + img1, des + 'Original')
        for img2 in images[images.index(img1)+1:]:
            if isdupe(cv2.imread(src+img1, 0), cv2.imread(src+img2, 0)):
                flag2 = False
                if flag:
                    shutil.copy(src+img1, des+'Dupes')
                    flag = False
                shutil.copy(src+img2, des+'Dupes')
                check[images.index(img2)] = True
    if flag2:
        shutil.copy(src + img1, des + 'Original')
    flag = True
    flag2 = True
    
