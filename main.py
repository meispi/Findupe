import cv2
import numpy as np
import os
import shutil

imgdict = {}

def isdupe(img1, img2):
    dim = (8, 8)
    rimg1 = cv2.resize(img1, dim, interpolation=cv2.INTER_AREA)
    rimg2 = cv2.resize(img2, dim, interpolation=cv2.INTER_AREA)
    l = str(list(np.concatenate(rimg2).flat))
    if l in imgdict:
        return True
    else:
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
        if val >= 5:
            return False
        else:
            return True


src = r'D:\\Python_Projects\\aug_dogs\\' # read How to use section in the readme to assign values to these variables
des = r'D:\\Python_Projects\\'
images = sorted([f for f in os.listdir(src)])
check = [False]*len(images)
flag = True
flag2 = True
# temp1 = cv2.imread(src+'n@dog.1000.jpg',0)
# temp2 = cv2.imread(src+'dog.1000.jpg',0)
# print(cv2.resize(temp1,(8,8),interpolation=cv2.INTER_AREA))
# print(cv2.resize(temp2,(8,8),interpolation=cv2.INTER_AREA))
# if (temp1 == temp2).all():
#     print("YO!!!")
# print(images.index('dog.1.jpg'))
for img1 in images:
    print(img1)
    if (not check[images.index(img1)]) and images.index(img1) != len(images)-1:
        #shutil.copy(src + img1, des + 'Original')
        temp = cv2.imread(src+img1, 0)
        l = str(list(np.concatenate(cv2.resize(temp,(8,8),interpolation=cv2.INTER_AREA)).flat))
        imgdict[l] = 1
        for img2 in images[images.index(img1)+1:]:
            if isdupe(cv2.imread(src+img1, 0), cv2.imread(src+img2, 0)):
                flag2 = False
                # if flag:
                #     shutil.copy(src+img1, des+'Dupes')
                #     flag = False
                shutil.copy(src+img2, des+'Dupes')
                check[images.index(img2)] = True
    if not check[images.index(img1)]:
        shutil.copy(src + img1, des + 'Original')
    flag = True
    flag2 = True
    
