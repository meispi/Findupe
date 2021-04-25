import cv2
import numpy as np
import os
import shutil
from skimage.metrics import structural_similarity as ssim

def isdupe(img1, img2):
    dim = (8, 8)
    rimg1 = cv2.resize(img1, dim, interpolation=cv2.INTER_AREA)
    rimg2 = cv2.resize(img2, dim, interpolation=cv2.INTER_AREA)
    (score, diff) = ssim(rimg1,rimg2,full=True)
    if score >= 0.9:
        return True
    else:
        return False


src = r'D:\\Python_Projects\\aug_dogs\\' # read How to use section in the readme to assign values to these variables
des = r'D:\\Python_Projects\\'
images = sorted([f for f in os.listdir(src)])
check = [False]*len(images)

for img1 in images:
    if (not check[images.index(img1)]) and images.index(img1) != len(images)-1:
        for img2 in images[images.index(img1)+1:]:
            if isdupe(cv2.imread(src+img1, 0), cv2.imread(src+img2, 0)):
                shutil.copy(src+img2, des+'Dupes')
                check[images.index(img2)] = True

    if not check[images.index(img1)]:
        shutil.copy(src + img1, des + 'Original')
