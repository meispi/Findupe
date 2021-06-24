import cv2
import numpy as np
import os
import shutil
import argparse
from skimage.metrics import structural_similarity as ssim

imgdict = {}
def flat(a):
    x = ""
    for i in a:
        x += str(i)
    return x

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
    images = [f for f in os.listdir(src)]
    check = {}
    for img in images:
        check[str(img)] = False
    des = os.getcwd()
    dupes = os.path.join(des,"Dupes")
    org = os.path.join(des,"Original")
    try:
        os.mkdir(dupes,0o666)
        os.mkdir(org,0o666)

        cntdupe, cntorg, cnt = 0, 0, 1

        print("[INFO] Processing Images...")
        if args.strict:
            for (i,img) in enumerate(images):
                temp = cv2.imread(os.path.join(src,img), 0)
                rimg = cv2.resize(temp, (8,8), interpolation=cv2.INTER_AREA)
                if flat(np.array(rimg)) in imgdict:
                    cntdupe += 1
                    shutil.copy(os.path.join(src,img), dupes)
                else:
                    imgdict[flat(np.array(rimg))] = 1
                    cntorg += 1
                    shutil.copy(os.path.join(src,img), org)

                print("[INFO] Images Processed {}/{}".format(i+1,len(images)), end='')
                print(f"\t dupes: {cntdupe}, org: {cntorg}")
        else:
            for (i,img1) in enumerate(images):
                if (not check[img1]) and i != len(images)-1:
                    shutil.copy(os.path.join(src,img1), org)
                    cntorg += 1
                    temp1 = cv2.imread(os.path.join(src,img1), 0)
                    rimg1 = cv2.resize(temp1, (8,8), interpolation=cv2.INTER_AREA)

                    for img2 in images[i+1:]:
                        temp2 = cv2.imread(os.path.join(src,img2), 0)
                        rimg2 = cv2.resize(temp2, (8,8), interpolation=cv2.INTER_AREA)

                        if isSim(rimg1, rimg2):
                            shutil.copy(os.path.join(src,img2), dupes)
                            cntdupe += 1
                            check[str(img2)] = True

                print("[INFO] Images Processed {}/{}".format(i+1,len(images)), end='')
                print(f"\t dupes: {cntdupe}, org: {cntorg}")
        

        print(f'No. of dupes found: {cntdupe}')
        print(f'No. of originals found: {cntorg}')
    
    except FileExistsError:
        print("[FileExistsError]: There already exists 2 folders called Dupes and Original in this directory, please make sure to remove them and try again")

except FileNotFoundError:
    exit('[FileNotFoundError]: The specified directory wasn\'t found, please provide the full path!')