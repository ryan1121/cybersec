# login

[toc]

## Description
My dog-sitter's brother made this website but I can't get in; can you help? login.mars.picoctf.net

## Solution
First, let's take a look for the website given.

We can saw a login interface with username and password input boxes.
So, let's try to fill in the input boxes with anything.
Before that, we should remember to open **INSPECTOR** mode, by clicking `F12` or `right click > Inspect`

After random login, we found that there is no requests for login validation which checking the username and password.
There is no any requests packet, but it is showing `Incorrect Username` which means that it should be somewhere to authenticate the correctivity of username and password. I guess it is using Javascript to check the username and password.

Then, I inspected the Javascript file which called `index.js` in this website.

I successfully found the validation code in the file.
The Javascript is using `btoa` method to creates a Base64-encoded ASCII string from a binary string.

Below is the main clue for us to solve this question.
```
t[e] = btoa(document.querySelector(r[e]).value).replace(/=/g, '');
``` 
The code is using `btoa` method to convert the value of input(Username & Password) to base64.

Below is the validation condition for Username and Password
```
return 'YWRtaW4' !== t.u ? alert('Incorrect Username') : 'cGljb0NURns1M3J2M3JfNTNydjNyXzUzcnYzcl81M3J2M3JfNTNydjNyfQ' !== t.p ? alert('Incorrect Password') : void alert(`Correct Password! Your flag is ${ atob(t.p) }.`)
```

The ways to get validated for login, is to convert `YWRtaW4` (Correct Username) and `cGljb0NURns1M3J2M3JfNTNydjNyXzUzcnYzcl81M3J2M3JfNTNydjNyfQ`(Correct Password) from Base64 to ASCII string.

Then we get :
```
Username : admin
Password : picoCTF{53rv3r_53rv3r_53rv3r_53rv3r_53rv3r}
```

Finally, we got the flag !!
```
picoCTF{53rv3r_53rv3r_53rv3r_53rv3r_53rv3r}
```
