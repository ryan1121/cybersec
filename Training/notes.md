
# Notes for CTF

[toc]

## Web
### web directory
./robots.txt --> is a text file with instructions for search engine crawlers.

./.htaccess --> On servers that run Apache (a web server software), the .htaccess file allows you to make changes to your website’s configuration without having to edit server configuration files.

./.DS_Store --> A .DS_Store, short for Desktop Services Store, is an invisible file on the macOS operating system that gets automatically created anytime you look into a folder with ‘Finder.’

## Tools
### Forensic

#### File

The file command is used to determine the file type of a file. There may be times when you are given a file that does not have an extension or the incorrect extension has been applied to add confusion and misdirection.

```
$ file dolls.jpg 
dolls.jpg: PNG image data, 594 x 1104, 8-bit/color RGBA, non-interlaced

```

<hr>

#### strings
Strings --> strings command is used to return the string characters into files. It primarily focuses on determining the contents of and extracting text from the binary files (non-text file). It is a complex task for a human to find out text from an executable file.

<hr>

#### steghide
Steghide --> steganography tool that uses a passcode to hide private files within the image or audio file. BMP and JPEG picture types are supported, as well as AU and WAV audio formats. 

<hr>

#### binwalk
Binwalk is a tool that allows you to search binary images for embedded files and executable code. We can use binwalk to search images for embedded files such as flags or files that may contain clues to the flag.

You may need to download binwalk on your system. Run the following command to install binwalk.

```
sudo apt install binwalk -y
```

Example 1:
You are provided an image named dog.jpg.
Run the following command to see if Binwalk finds any embedded files.

```
$ binwalk dog.jpg
DECIMAL       HEXADECIMAL     DESCRIPTION
-------------------------------------------------------------------
0             0x0             JPEG image data, JFIF standard 1.01
88221         0x1589D         Zip archive ... name: hidden_text.txt
88384         0x15940         End of Zip archive, footer length: 22

```

Binwalk detects a zip file embedded within dog.jpg. The file within the zip file is named hidden_text.txt.

You can **extract** hidden files by running the following command.

```
$ binwalk -e dog.jpgDECIMAL
HEXADECIMAL  DESCRIPTION
-------------------------------------------------------------------
0           0x0             JPEG image data, JFIF standard 1.01
88221       0x1589D         Zip archive data, ... hidden_text.txt
88384       0x15940         End of Zip archive, footer length: 22
```

A directory named ‘_dog.jpg.extracted’ has been created with the file automatically unzipped.

```
$ cd _dog.jpg.extracted/
$ ls -l
total 8
-rw-r--r-- 1 pi pi 185 Jul  5 19:50 1589D.zip
-rw-r--r-- 1 pi pi  21 Jul  5 15:39 hidden_text.txt

$ cat hidden_text.txt
THIS IS A HIDDEN FLAG
```

Running the cat command on the embedded text file reveals “THIS IS A HIDDEN FLAG.”


<hr>
