# Nice Netcat..

[toc]

## Description
Author: syreal
Description
There is a nice program that you can talk to by using this command in a shell: $ nc mercury.picoctf.net 43239, but it doesn't speak English...

There are two question is the hint, let's try to complete them first before start with this question. ⬇️⬇️⬇️⬇️⬇️

### Hint 1's Question : What's a Netcat
#### Description
Author: Sanjay C/Danny Tunitis
Description
Using netcat (nc) is going to be pretty important. Can you connect to **jupiter.challenges.picoctf.org** at port **25103** to get the flag?

#### Solution
We can just solve it by using netcat command as below
```
nc jupiter.challenges.picoctf.org 25103
```
After that, we can get the **output** with the flag
```
You're on your way to becoming the net cat master
picoCTF{nEtCat_Mast3ry_d0c64587}
```


### Hint 2's Question : Lets Warm Up
#### Description
Author: Sanjay C/Danny Tunitis
Description
If I told you a word started with 0x70 in hexadecimal, what would it start with in ASCII? 

### Solution
From the description, we can know that this question is about **ASCII**
The hint 1 is asking us to answer with flag format : `submit 'picoCTF{hello}' as the flag.`

Then, we can just compare with the ASCII table, we know that 0x70 in hexadecimal is referring to letter 'p'
So the **answer** is :
```
picoCTF{p}
```

## Solution(Nice Netcat..)
From the description, the question is asking us to use netcat to connect to the specified url with the port number.
So, we can just try to type the command in terminal
```
nc mercury.picoctf.net 43239
```
Then, we get the output with many numbers in different lines.
Let's save the output in a txt file which called `output.txt`
```
112 
105 
99 
111 
67 
84 
70 
123 
103 
48 
48 
100 
95 
107 
49 
116 
116 
121 
33 
95 
110 
49 
99 
51 
95 
107 
49 
116 
116 
121 
33 
95 
55 
99 
48 
56 
50 
49 
102 
53 
125 
10 
```
We know that this question is about ASCII from the hints we did. So these numbers should be the word in hexadecimal.
As usual, we can try to solve it by using **python** code. There is function called `chr()` which can help us to get the character from hexadecimal number.
```python
with open('output.txt','r') as f:
    outputList = f.readlines()

# Define a result string variable
result = ''

# Using for loop to read line by line
for i in outputList :
    # We are using the int() function to convert the 'i' variable which is string data type to integer data type
    result += chr(int(i))

print("Result : ", result)

```
We can run the code, and get the result
```
Result :  picoCTF{g00d_k1tty!_n1c3_k1tty!_7c0821f5}
```
