# Crypto
> Here are notes on cryptography using Python

[toc]

## ASCII
In Python, the chr() function can be used to convert an ASCII ordinal number to a character (the ord() function does the opposite).

```
[99, 114, 121, 112, 116, 111, 123, 65, 83, 67, 73, 73, 95, 112, 114, 49, 110, 116, 52, 98, 108, 51, 125]
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

```
byte_data = b'r\xbc\xa9\xb6\x8f\xc1j\xc7\xbe\xeb\x8f\x84\x9d\xca\x1d\x8ax>\x8a\xcf\x96y\xbf\x92i\xf7\xbf'

# encode it into Base64
import base64

b64_data = base64.b64encode(bytes_data)
```

