# Lookey Here

[toc]


## Description
Attackers have hidden information in a very large mass of data in the past, maybe they are still doing it. Download the data here.

## Solution
First, let me take a look for the file that we downloaded.
There are very large mass of data as the description mentioned before in the file.

We can just try to using `grep` command to search for the flag based on the known prefix : `pico`
Using the command below

```
cat anthem.flag.txt | grep pico
```

Then, we found the result with the flag !
```
      we think that the men of picoCTF{gr3p_15_@w3s0m3_2116b979}
```

## Flag
```
picoCTF{gr3p_15_@w3s0m3_2116b979}
```
