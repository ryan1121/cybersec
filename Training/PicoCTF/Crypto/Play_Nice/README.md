# Play Nice

[toc]

## Description
Author: madStacks
Description
Not all ancient ciphers were so bad... The flag is not in standard format. `nc mercury.picoctf.net 30568` [playfair.py](./playfair.py)

## Solution
From the python file provided, we can get one important information, which is the size of the matrix is *6x6*
```python
SQUARE_SIZE = 6
```

Next, I used the command provided to connect to the server : `nc mercury.picoctf.net 30568`
```
Here is the alphabet: 0fkdwu6rp8zvsnlj3iytxmeh72ca9bg5o41q
Here is the encrypted message: herfayo7oqxrz7jwxx15ie20p40u1i
What is the plaintext message? 
```
We got the alphabet which is for the matrix table, and the encrypted message that we need to decrypt.
So I wrote a python script to generate the matrix and a list of encrypted message's pairs : [gen_matrix.py](./gen_matrix.py)
After running the script, I got them :
```
['0', 'f', 'k', 'd', 'w', 'u']
['6', 'r', 'p', '8', 'z', 'v']
['s', 'n', 'l', 'j', '3', 'i']
['y', 't', 'x', 'm', 'e', 'h']
['7', '2', 'c', 'a', '9', 'b']
['g', '5', 'o', '4', '1', 'q']

['he', 'rf', 'ay', 'o7', 'oq', 'xr', 'z7', 'jw', 'xx', '15', 'ie', '20', 'p4', '0u', '1i']
```

I started to decrypt them one pair by one pair using the matrix table :
```
he --> em (take the left one)
rf --> f5 (take upward)
ay --> 7m (take the end of the square)
...


Then I got the plaintext message : emf57mgc51tp693dtt4g3h7f8ouwq3
```

I entered the plaintext message into the server, it showed the flag :
```
Congratulations! Here's the flag: 007d0a696aaad7fb5ec21c7698e4f754
```

## Flag
```
007d0a696aaad7fb5ec21c7698e4f754
```
