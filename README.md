# Findupe
A tool that helps you separate similar looking images from a bunch of images. It has 2 modes `similar` (default) and `strict`, in `similar` mode if 2 images are `90%` or more similar on the basis of [structural similarity index](https://medium.com/srm-mic/all-about-structural-similarity-index-ssim-theory-code-in-pytorch-6551b455541e) then they are considered to be duplicates. In `strict` mode, if 2 images are exact copy of each other only then they are considered to be duplicates.

## Installation

Make sure you have python (or python3) installed on your system and have it set as an environment variable. You can get it from [here](https://www.python.org/downloads/)

```
$ git clone https://github.com/meispi/Findupe
$ cd Findupe
$ python setup.py install
```

## How to use
```
optional arguments:
  -h, --help  show this help message and exit
  -p PATH     source directory path
  -s          strict (only exact copies will be detected)
```
Here `-p` flag is necessary followed by the full path of the directory which contains the images.
The program will create 2 directories, inside the current working directory, `Dupes` and `Original`(so make sure you don't have directories/folders of same name). `Dupes` will contain all the duplicates of an image (if there are n similar looking images then it will contain n-1 of them). `Original` will contain uniques images.

`-s` is an optional flag (no argument required) which will result in separating only the exact copies of images (if 2 images are similar looking but not exactly the same, this will treat them as 2 different images).

e.g. :

For separating similar looking images
```
$ python findupe.py -p /path/to/dir
```
![image](https://user-images.githubusercontent.com/33330452/123267452-a7710500-d51a-11eb-9a67-ecf736ef8ed7.png)


**Dupes**

![image](https://user-images.githubusercontent.com/33330452/123267765-ff0f7080-d51a-11eb-8534-4ab161159b24.png)


**Original**

![image](https://user-images.githubusercontent.com/33330452/123267857-177f8b00-d51b-11eb-89ff-51dad26f43a5.png)



For separating exact same images
```
$ python findupe.py -p /path/to/dir -s
```
![image](https://user-images.githubusercontent.com/33330452/123273558-60860e00-d520-11eb-8940-a5435cc04df7.png)


**Dupes**

![image](https://user-images.githubusercontent.com/33330452/123273132-fec5a400-d51f-11eb-816f-558430c3c896.png)


**Original**

![image](https://user-images.githubusercontent.com/33330452/123273215-1309a100-d520-11eb-8fb7-4b07ac8b7783.png)
