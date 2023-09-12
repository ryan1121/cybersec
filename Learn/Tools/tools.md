# Tools that usually using for CTFs
There are some basic information about the tools and some example of command usually using.

[toc]

## dirbuster
Some common parameters using in `dirbuster` command

```
-u, --url <url>
-c, --cookies <cookies>
-t, --threads <int>
-w, --wordlist <word list>
-x, --extensions <extensions separated by commas>
```
```
gobuster dir -u https://mysite.com/path/to/folder -c ‘session=123456’ -t 50 -w /usr/share/dirb/common.txt -x .php,.html
```
