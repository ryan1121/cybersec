# Tools that usually using for CTFs
There are some basic information about the tools and some example of command usually using.

[toc]

## dirbuster
DirBuster is a multi threaded java application designed to brute force directories and files names on web/application servers.

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

<hr>

## nikto
Vulnerability scanning

```
nikto -h http://192.168.1.14 /
```

