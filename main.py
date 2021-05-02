import cv2
import numpy as np
import os
import shutil
import argparse
from skimage.metrics import structural_similarity as ssim

imgdict = {}

def isStrictdupe(rimg1,rimg2):
    if str(np.array(rimg2).flatten()) in imgdict:
        return True
    else:
        return False

def isSim(rimg1, rimg2):
    (score, diff) = ssim(rimg1,rimg2,full=True)
    if score >= 0.9:
        return True
    else:
        return False


parser = argparse.ArgumentParser()

parser.add_argument('-p', help='source directory path',dest='path')
parser.add_argument('-s', help='strict (only exact copies will be detected)', dest='strict', action='store_true')

args = parser.parse_args()
if args.path:
    src = args.path 

try:
    images = sorted([f for f in os.listdir(src)])
    check = [False]*len(images)
    des = os.getcwd()
    dupes = os.path.join(des,"Dupes")
    os.mkdir(dupes,0o666)
    org = os.path.join(des,"Original")
    os.mkdir(org,0o666)

    for img1 in images:
        if (not check[images.index(img1)]) and images.index(img1) != len(images)-1:
            shutil.copy(src+'\\'+img1, org)
            temp1 = cv2.imread(src+'\\'+img1, 0)
            rimg1 = cv2.resize(temp1, (8,8), interpolation=cv2.INTER_AREA)
            imgdict[str(np.array(rimg1).flatten())] = 1

            for img2 in images[images.index(img1)+1:]:
                temp2 = cv2.imread(src+'\\'+img2, 0)
                rimg2 = cv2.resize(temp2, (8,8), interpolation=cv2.INTER_AREA)
                if args.strict:
                    if isStrictdupe(rimg1, rimg2):
                        shutil.copy(src+'\\'+img2, dupes)
                        check[images.index(img2)] = True
                else:
                    if isSim(rimg1, rimg2):
                        shutil.copy(src+'\\'+img2, dupes)
                        check[images.index(img2)] = True            

except FileNotFoundError:
    exit('The specified directory wasn\'t found, please provide the full path!')