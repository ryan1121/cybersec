# Python Wrangling

[toc]

## Question
AUTHOR: SYREAL

Description
Python scripts are invoked kind of like programs in the Terminal... Can you run this [Python script](././ende.py) using this [password](././pw.txt) to get the [flag](././flag.txt.en)?

<hr>

## Solution
--> ende.py is a python script provided for us to run
--> pw.txt is the password file provided for us to use in python script
--> flag.txt.en is the file with the final flag's content

First, we can try to run ende.py by using Python
```
> python ende.py
Output : Usage: ende.py (-e/-d) [file]
```
The usage message is telling us to pass argument vector(argv) either -e or -d when running this script

-e is stands for encrypt
-d is stands for decrypt

After we check the content inside flag.txt.en, we know that it is an encrypted message, we need to use the script to decrypt it so we are passing -d argv to the script and specify the file name.

```
>> python ende.py -d flag.txt.en
Please enter the password: aa821c16aa821c16aa821c16aa821c16
```

Then, enter the password. Finally, we got the flag.

## Result
```Result : picoCTF{4p0110_1n_7h3_h0us3_aa821c16}```