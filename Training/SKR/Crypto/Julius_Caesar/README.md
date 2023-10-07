# Julius Caesar [ 100 Points ]

[toc]

## Description
Found a fortune cookie in Kuki Godam's place. The message inside is weird, seems is encrypted. Can you decode it?

Difficulty: Easy

## Solution
From the title of this challenge, we can guess that this challenge is about Caesar Encryption.
We know the format of Flag should be : SKR{flag_flag}
The starting of the flag is SKR, by comparing with the encrypted message given, we can know that it is using ROT13 encryption
```
Encrypted message : FXE{Pnrfne_Pvcure_Qrpbqre}
Flag : SKR{xxxxxx_xxxxxx_xxxxxxx}
```
Alphabet `F` is in the 5th place while alphabet `S` is in the 18th place of the alphabetical order
> 5(F) + 13 = 18(S)

So we can just moving each of the encrypted message 13 positions to get the flag.
we can either using [Online decoder](https://cryptii.com/pipes/caesar-cipher) or Write a code to decrypt it [solution.pu](./solutiom.py')

## Flag
Flag : SKR{Caesar_Cipher_Decoder}
```

```
