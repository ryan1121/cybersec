# Tab, Tab, Attack

[toc]

## Description
Author: syreal
Description
Using tabcomplete in the Terminal will add years to your life, esp. when dealing with long rambling directory structures and filenames: **Addadshashanammu.zip**

## Solution
First, we saw that there is a clue in the description :  **dealing with long rambling directory structures and filenames**

After that, let's try to download the **Addadshashanammu.zip** zip file and unzip it.

In linux :
```
unzip Addadshashanammu.zip
```

We try to click into the folder, and we found that it is corresponding to the clue we found in the description just now.
`dealing with long rambling directory structures and filenames`

Steps :
1. We can either writing a script to get into the last directory of this folder or click into the folder  by manually
2. After we get into the last directory, we found that there is an `executable file` inside the folder which called `fang-of-haynekhtnamet`
3. Let's try to run it
	```
	chmod +a fang-of-haynekhtnamet

	./fang-of-haynekhtnamet	
	```
4. Then, we got the output.
	```
	*ZAP!* picoCTF{l3v3l_up!_t4k3_4_r35t!_524e3dc4}

	```
## Result
```Result : picoCTF{l3v3l_up!_t4k3_4_r35t!_524e3dc4}```


