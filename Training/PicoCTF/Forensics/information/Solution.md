#information

[toc]

## Description
Author: susie
Description
Files can always be changed in a secret way. Can you find the flag? cat.jpg

## Solution
First, let's see the details at this file.
We can use this [website](https://29a.ch/photo-forensics/#strings) to get the strings from the image file.

```
JFIF
0Photoshop 3.0
8BIM
PicoCTF
http://ns.adobe.com/xap/1.0/
<?xpacket begin='
' id='W5M0MpCehiHzreSzNTczkc9d'?>
<x:xmpmeta xmlns:x='adobe:ns:meta/' x:xmptk='Image::ExifTool 10.80'>
<rdf:RDF xmlns:rdf='http://www.w3.org/1999/02/22-rdf-syntax-ns#'>
 <rdf:Description rdf:about=''
  xmlns:cc='http://creativecommons.org/ns#'>
  <cc:license rdf:resource='cGljb0NURnt0aGVfbTN0YWRhdGFfMXNfbW9kaWZpZWR9'/>
 </rdf:Description>
 <rdf:Description rdf:about=''
  xmlns:dc='http://purl.org/dc/elements/1.1/'>
  <dc:rights>
   <rdf:Alt>
    <rdf:li xml:lang='x-default'>PicoCTF</rdf:li>
   </rdf:Alt>
  </dc:rights>
 </rdf:Description>
</rdf:RDF>
</x:xmpmeta>
```

We can saw that there is a suspicious strings which might be a base64 encoded strings
```
cGljb0NURnt0aGVfbTN0YWRhdGFfMXNfbW9kaWZpZWR9
```
Let's try to decode it using this [website](https://gchq.github.io/CyberChef/)

Then we get the flag ! :D
```
picoCTF{the_m3tadata_1s_modified}
```


## Flag
```
picoCTF{the_m3tadata_1s_modified}
```


