# like1000

[toc]

## Description
Author: Danny
Description
This .tar file got tarred a lot.

## Solution
After downloaded the .tar file, we can try to 'unzip' it by using `tar` command
```
tar -xf 1000.tar
```
After extracted, we got another tar file which called 999.tar
From this result, we know that we might need to extract for total 1000 times.
So I wrote a Python code to extract it, and another Python code to delete the tar file that extracted : [tar.py](./tar.py) & [del_tar.py](./del_tar.py)

I run this two codes together, and finally I got the last tar file which called `1.tar` and [`flag.png`](./flag.png).
Finally, we got the flag inside the image.

## Flag
```
picoCTF{l0t5_0f_TAR5}
```
