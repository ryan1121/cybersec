# Crypto
Here are notes on Cryptography using Python

Message usually can be converted into ASCII bytes, hex bytes, hexadecimal(base-16) and decimal(base-10) :
> message: HELLO
> ascii bytes: [72, 69, 76, 76, 79]
> hex bytes: [0x48, 0x45, 0x4c, 0x4c, 0x4f]
> base-16: 0x48454c4c4f
> base-10: 310400273487 

[toc]

## ASCII
In Python, the chr() function can be used to convert an ASCII ordinal number to a character (the ord() function does the opposite).

Below is a list of ASCII ordinal numbers :
```
[99, 114, 121, 112, 116, 111, 123, 65, 83, 67, 73, 73, 95, 112, 114, 49, 110, 116, 52, 98, 108, 51, 125]
```

Example :
```python
print(chr(65))	# Output : A


print(ord("A"))	# Output : 64
```

## Hex to bytes
In Python, the bytes.fromhex() function can be used to convert hex to bytes. The .hex() instance method can be called on byte strings to get the hex representation.

Below is a hex string :
```
63727970746f7b596f755f77696c6c5f62655f776f726b696e675f776974685f6865785f737472696e67735f615f6c6f747d
```

Example :
```python

str_data = "Hello"

# Converting string data to bytes
byte_data = bytes(str_data, "ascii")

# Converting bytes data to hex data
hex_data = byte_data.hex()
```

## Base64

Below is a bytes data :

```python
import base64

byte_data = b'r\xbc\xa9\xb6\x8f\xc1j\xc7\xbe\xeb\x8f\x84\x9d\xca\x1d\x8ax>\x8a\xcf\x96y\xbf\x92i\xf7\xbf'

# encode it into Base64

b64_data = base64.b64encode(bytes_data)
```

## PyCryptodome library
Install :

```
pip install pycryptodome
```

### bytes_to_long() & long_to_bytes()
`bytes_to_long()` - convert bytes string to long
`long_to_bytes()` - convert long to byte string

Example : 

```python
from Crypto.Util.number import *


print(long_to_bytes(126943972912743))   # Output : string

print(bytes_to_long(b"string"))         # Output : 126943972912743

```

## pwntools library
Install :

```
pip install pwntools
```
### xor()
For longer binary numbers we XOR bit by bit: 0110 ^ 1010 = 1100
The Python `pwntools` library has a convenient `xor()` function that can XOR together data of different types and lengths.

```python
from pwn import *

a = "hello world"
b = "hi"

print(xor(a,b)) # Output : b'\x00\x0c\x04\x05\x07I\x1f\x06\x1a\x05\x0c'

```

## telnetlib library
Telnet is a networking protocol that follows a client-server model. It uses TCP as its underlying communication protocol. It is typically used to start and a remote command-line session, typically on a server.  

Example :
```python
import telnetlib

HOST_IP = "mercury.picoctf.net"
HOST_PORT = 34938
tn = telnetlib.Telnet(HOST_IP, HOST_PORT)

for i in range(9):	# the number should be changed according to the situation
	# Read output line by line
	print(tn.read_until(b"\n"))

# read until the specified string appeared
tn.read_until(b"Choose an option: ")

# send message to the server
tn.write("0".encode("ascii") + b"\n")

tn.read_until(b"How many do you want to buy?")

tn.write("1".encode("ascii") + b"\n")

print(tn.read_all().decode('ascii'))


```
