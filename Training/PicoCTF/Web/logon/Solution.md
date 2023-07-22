# logon

[toc]

## Question
Author: bobson
Description
The factory is hiding things from all of its users. Can you login as Joe and find what they've been looking at? https://jupiter.challenges.picoctf.org/problem/15796/ (link) or http://jupiter.challenges.picoctf.org:15796

<hr>

## Solution
>Everytime when we are doing web explotation, we should use the `inspector` to see the source code and the network request packet to collect information.

First, let's get to the link given : https://jupiter.challenges.picoctf.org/problem/15796/
From the description of the question, it is asking us to login as Joe, so let's try with username as Joe.
We can try some weak password, for example : joe, 123, admin.

We found that the login page is no confirmation for the password :D
After login to the factory website, we saw a BIG words telling us : **No flag for you**

There's a network packet which called "flag", let's check the header of this packet.
From the headers, we found that the cookies value is :
```
_ga=GA1.2.819216009.1689170711; _ga_L6FT52K063=GS1.2.1690015485.5.1.1690016916.0.0.0; __cf_bm=S5zxvu3_77MY0kw3LAczHxJp8Zhma4mRGqt0PZ9gelE-1690017284-0-AYMxGweeYEY37LKUjkNe5r4PdkA8A15V1OQJtIoFh/Wh3QDemU221pLfUQu/O90nUIzkxnLgUVBqh+8AqNEo/2U=; _gid=GA1.2.1631485059.1690015484; cf_clearance=mR69C31fIFZaZALFq88dPRcWJ2sk2ZoSlTFgN6sqAYg-1690015484-0-0.2.1690015484; password=123; username=joe; admin=False
```
We found that the `admin` key with a value `False`, that's may be the result why we can't see the flag.

We can use **BurpSuite** to modify the request, change the value from False to True.

```
Cookie: password=joe; username=joe; admin=False

to 

Cookie: password=joe; username=joe; admin=True

```
Then, we got the flag display on the page:
```
Flag: picoCTF{th3_c0nsp1r4cy_l1v3s_6edb3f5f}
```

## Result
```
Flag: picoCTF{th3_c0nsp1r4cy_l1v3s_6edb3f5f}
```


