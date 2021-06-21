# Findupe
This is an ML-based project which separates duplicate images from a bunch of images.

# How to use
```
optional arguments:
  -h, --help  show this help message and exit
  -p PATH     source directory path
  -s          strict (only exact copies will be detected)
  ```
Here `-p` flag is necessary followed by the full path of the directory which contains the images.
The program will create 2 directories, inside the current working directory, `Dupes` and `Original`. `Dupes` will contain all the duplicates of an image (if there are n similar looking images then it will contain n-1 of them). `Original` will contain uniques images.

`-s` is an optional flag (no argument required) which will result in separating only the exact copies of images (if 2 images are similar looking but not exactly the same, this will treat them as 2 different images).

e.g. :
```
python main.py -p /path/to/dir
```
![image](https://user-images.githubusercontent.com/33330452/122761114-8067c880-d2b9-11eb-8da2-0438f5ec5ced.png)

 
