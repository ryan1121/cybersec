# extensions

[toc]

## Description
Author: Sanjay C/Danny
Description
This is a really weird text file TXT? Can you find the flag?

## Solution
After downloaded the weird txt file, the first thing to do is check the file type of this txt file
We can use `file` command to check the type of the file
```
file flag.txt
```

Then, we got the output with the file type :
```
flag.txt: PNG image data, 1697 x 608, 8-bit/color RGB, non-interlaced
```

It is actually PNG image data in this file with .txt extension.
So we can just copy the image data into a new file with `.png` extenstion using `cp` command
```
cp flag.txt flag.png
```

After copied the image data, we just open the png file then we got the flag inside the image :D

## Flag
```
picoCTF{now_you_know_about_extensions}
```

