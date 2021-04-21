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
        for i in range(8):
            for j in range(8):
                if rimg1[i][j] - mean1 > 0:
                    str1 += '1'
                else:
                    str1 += '0'
                if rimg2[i][j] - mean2 > 0:
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

for img1 in images:
    print(img1)
    if (not check[images.index(img1)]) and images.index(img1) != len(images)-1:

        temp = cv2.imread(src+img1, 0)
        l = str(list(np.concatenate(cv2.resize(temp,(8,8),interpolation=cv2.INTER_AREA)).flat))
        imgdict[l] = 1
        for img2 in images[images.index(img1)+1:]:
            if isdupe(cv2.imread(src+img1, 0), cv2.imread(src+img2, 0)):
                shutil.copy(src+img2, des+'Dupes')
                check[images.index(img2)] = True

    if not check[images.index(img1)]:
        shutil.copy(src + img1, des + 'Original')
