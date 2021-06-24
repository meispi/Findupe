# Findupe
This is an ML-based project which separates duplicate images from a bunch of images.

## Installation

Make sure you have python3 installed on your system. You can get it from [here](https://www.python.org/downloads/)

### Ubuntu
```
$ git clone https://github.com/meispi/Findupe
$ cd Findupe
$ python3 setup.py install
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
$ python3 findupe.py -p /path/to/dir
```
For separating exact same images
```
$ python3 findupe.py -p /path/to/dir -s
```