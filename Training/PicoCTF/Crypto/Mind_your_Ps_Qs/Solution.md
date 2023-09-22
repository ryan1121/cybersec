# Mind your Ps and Qs

[toc]

## Description
> Author: Sara
> Description
> In RSA, a small e value can be problematic, but what about N? Can you decrypt this? values

## Solution
As the description mentioned, it is using **RSA Cryptosystem**.
After download the `values` file, we got the `cipher(c)`, `n(the product of p and q)` and `e(encryption key)`

First, we need to find the two prime numbers (p and q), we can use [FactorDB](http://factordb.com) to get them.
Then, we got it :
```
1280678415...23<82> = 1899107986527483535344517113948531328331<40> · 674357869540600933870145899564746495319033<42>
```

Next, I wrote a **Python** code to solve it : [solve.py](./solve.py)

```python
from Crypto.Util.number import inverse, long_to_bytes

c = 62324783949134119159408816513334912534343517300880137691662780895409992760262021
n = 1280678415822214057864524798453297819181910621573945477544758171055968245116423923
e = 65537

# Use Factordb.com to find the two factor of n, which is p and q
p = 1899107986527483535344517113948531328331
q = 674357869540600933870145899564746495319033

phi = (p-1)*(q-1)

# Find the inverse modular of e
d = inverse(e, phi)

# Decrypt using RSA formula
res = pow(c, d, n)

# Convert long data type to bytes, then we got the flag
print(long_to_bytes(res))

```

Run the python code, then we got the flag : b'picoCTF{sma11_N_n0_g0od_05012767}'


## Flag
```
picoCTF{sma11_N_n0_g0od_05012767}
```
