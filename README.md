# Image-Processing
This is an ML-based project which separates duplicate images from a bunch of images. [Still under development]

# How to use
On line `40` and `41` you can see `src` and `des` variables. These are the source (where your images are stored) and destination (where you want the duplicates to be copied to) 
respectively.
You have to put the correct source and destination of your directories. (In windows you have to escape `\` so your path will look like `C:\\path\\to\\dir\\`).
Put an extra `/` or `\\` at the end depending on the OS you are using because the code traverses the files **inside** the directory.
Make sure to have two directories `Dupes` and `Original` in the `des` directory.
 
# Issues
The time complexity of finding and separating images is not the best, so I have to work on that.
