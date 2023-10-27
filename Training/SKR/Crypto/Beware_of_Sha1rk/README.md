# Beware of SHA1rk

[toc]

## Description
I break into md5hashing.net database found a password hash but I do not know how to decrypt it. `90cf686245ad80dccbb421148dfb5768498c6669`

Flag format: SKR{Decrypted Password}

## Solution
By visting the website provided in the description, we know that it is a website using for hash/unhash.
Due to unknown type of the hash value provided, we can use the unhash function with `Select all types` to search for the value of the hash value.

Wait for a while, then we got it :
```
Hash type : Sha1
Value : D4ta_Bre4ches
```

## Flag :
```
SKR{D4ta_Bre4ches}
```
