import cv2
import numpy as np
import os
import shutil
import argparse
from skimage.metrics import structural_similarity as ssim

imgdict = {}

def isStrictdupe(rimg1,rimg2):
    if str(np.array(rimg2).ravel()) in imgdict:
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

else:
    parser.print_help()
    exit(0)
try:
    images = sorted([f for f in os.listdir(src)])
    check = {}
    for img in images:
        check[str(img)] = False
    des = os.getcwd()
    dupes = os.path.join(des,"Dupes")
    os.mkdir(dupes,0o666)
    org = os.path.join(des,"Original")
    os.mkdir(org,0o666)

    cntdupe, cntorg, i = 0, 0, 0

    for img1 in images:
        if (not check[img1]) and i != len(images)-1:
            shutil.copy(os.path.join(src,img1), org)
            cntorg += 1
            temp1 = cv2.imread(os.path.join(src,img1), 0)
            rimg1 = cv2.resize(temp1, (8,8), interpolation=cv2.INTER_AREA)
            imgdict[str(np.array(rimg1).ravel())] = 1

            for img2 in images[i+1:]:
                temp2 = cv2.imread(os.path.join(src,img2), 0)
                rimg2 = cv2.resize(temp2, (8,8), interpolation=cv2.INTER_AREA)
                if args.strict:
                    if isStrictdupe(rimg1, rimg2):
                        shutil.copy(os.path.join(src,img2), dupes)
                        cntdupe += 1
                        check[str(img2)] = True
                else:
                    if isSim(rimg1, rimg2):
                        shutil.copy(os.path.join(src,img2), dupes)
                        cntdupe += 1
                        check[str(img2)] = True

        print("[INFO] images processed {}/{}".format(i+1,len(images)), end='')
        print(f"\t dupes: {cntdupe}, org: {cntorg}")
        i += 1
        

    print(f'No. of dupes found: {cntdupe}')
    print(f'No. of originals found: {cntorg}')

except FileNotFoundError:
    exit('The specified directory wasn\'t found, please provide the full path!')