from turtle import st
import cv2
import numpy as np
import os
import shutil
import argparse
from skimage.metrics import structural_similarity as ssim

class TrieNode():
    def __init__(self):
        self.children = {}
        self.eow = False
        self.ind = []

class Trie():
    def __init__(self):
        self.root = TrieNode()
    
    def Insert(self, s, i):
        ptr = self.root
        for c in s:
            if c not in ptr.children:
                ptr.children[c] = TrieNode()
            ptr = ptr.children[c]
            ptr.ind.append(i)
        ptr.eow = True

    def Search(self, s):
        ptr = self.root
        for c in s:
            if c not in ptr.children:
                return []
            ptr = ptr.children[c]
        return ptr.ind

class Findupe:
    def flat(self, a):
        x = ""
        for i in a:
            x += str(i)
        return x

    def isSim(self, imgx, imgy):
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
    
    des = os.getcwd()
    dupes = os.path.join(des,"Dupes")
    org = os.path.join(des,"Original")

    try:
        os.mkdir(dupes,0o666)
        os.mkdir(org,0o666)

        check = [False]*len(images)
        cntdupe, cntorg, cnt = 0, 0, 1

        trie = Trie()
        obj = Findupe()

        print("[INFO] Processing Images...")
        
        for (i, img) in enumerate(images):
            temp = cv2.imread(os.path.join(src,img), 0)
            img = cv2.resize(temp, (8,8), interpolation=cv2.INTER_AREA)
            flat_img = obj.flat(img)
            trie.Insert(flat_img, i)

        if args.strict:
            for (i, img) in enumerate(images):
                if check[i]:
                    continue

                temp = cv2.imread(os.path.join(src,img), 0)
                rimg = cv2.resize(temp, (8,8), interpolation=cv2.INTER_AREA)
                flat_img = obj.flat(rimg)

                ind = trie.Search(flat_img)
                sz = len(ind)
                if sz == 0:
                    continue
                
                cntorg += 1
                img = images[ind[0]]
                shutil.copy(os.path.join(src,img), org)
                cntdupe += sz-1
                for j in ind[1:]:
                    img = images[j]
                    shutil.copy(os.path.join(src,img), dupes)
                    check[j] = True

                print("[INFO] Images Processed ", end='')
                print(f"\t dupes: {cntdupe}, org: {cntorg}")

        else:
            for (i, img1) in enumerate(images):
                if not check[i]:
                    shutil.copy(os.path.join(src,img1), org)
                    cntorg += 1
                    temp1 = cv2.imread(os.path.join(src,img1), 0)
                    rimg1 = cv2.resize(temp1, (8,8), interpolation=cv2.INTER_AREA)
                    flat_img = obj.flat(rimg1)

                    ind = trie.Search(flat_img)
                    sz = len(ind)
                    if sz == 0:
                        continue

                    cntdupe += sz-1
                    for j in ind[1:]:
                        img = images[j]
                        shutil.copy(os.path.join(src,img), dupes)
                        check[j] = True

                    for j in range(i+1, len(images)):
                        if check[j]:
                            continue

                        img2 = images[j]
                        temp2 = cv2.imread(os.path.join(src,img2), 0)
                        rimg2 = cv2.resize(temp2, (8,8), interpolation=cv2.INTER_AREA)

                        if obj.isSim(rimg1, rimg2):
                            shutil.copy(os.path.join(src,img2), dupes)
                            cntdupe += 1
                            check[j] = True

                print("[INFO] Images Processed {}/{}".format(i+1,len(images)), end='')
                print(f"\t dupes: {cntdupe}, org: {cntorg}")
        

        print(f'No. of dupes found: {cntdupe}')
        print(f'No. of originals found: {cntorg}')
    
    except FileExistsError:
        print("[FileExistsError]: There already exists 2 folders called Dupes and Original in this directory, please make sure to remove them and try again")

except FileNotFoundError:
    exit('[FileNotFoundError]: The specified directory wasn\'t found, please provide the full path!')