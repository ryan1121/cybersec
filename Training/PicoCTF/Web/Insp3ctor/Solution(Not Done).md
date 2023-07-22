
# Insp3ctor

[toc]

## Description
Author: zaratec/danny
Description
Kishor Balan tipped us off that the following code may need inspection: https://jupiter.challenges.picoctf.org/problem/44924/ (link) or http://jupiter.challenges.picoctf.org:44924

## Solution
From the title of this question, we know that it is about the inspector.
How do we inspect web code on a browser ? Use the **inspector** mode (Click F12 on browser).

There are two button on the page : What and How
We clicked the "How" Button, it is telling us that this website is making with HTML, CSS and JS.
So, it may be a clue. Let's try to see the source codes for this three types of file.

First, we go the `Inspector` section, and check the HTML code.
We found that there is a command in the body section :
```
<!-- Html is neat. Anyways have 1/3 of the flag: picoCTF{tru3_d3 -->
```
That's is the 1/3 of the flag. :D

Next, we check the CSS file. We go the `Style Editor` and look for the file which named "mycss.css"
Scoll down, then we got the second part of the flag in the command:
```
/* You need CSS to make pretty pages. Here's part 2/3 of the flag: t3ct1ve_0r_ju5t */
```

Last, we check the JavaScript(JS) file. We need to go to the `Internet` and look for a file which named "myjs.js".
We can get the last part of the flag in command too :
```
/* Javascript sure is neat. Anyways part 3/3 of the flag: _lucky?f10be399} */

```

## Result
Combine three of them together, we got the final flag :
```
picoCTF{tru3_d3t3ct1ve_0r_ju5t_lucky?f10be399}
```

