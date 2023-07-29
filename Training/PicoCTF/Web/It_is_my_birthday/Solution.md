# It is my Birthday

[toc]

## Description
Author: madStacks

Description
I sent out 2 invitations to all of my friends for my birthday! I'll know if they get stolen because the two invites look similar, and they even have the same md5 hash, but they are slightly different! You wouldn't believe how long it took me to find a collision. Anyway, see if you're invited by submitting 2 PDFs to my website. http://mercury.picoctf.net:11590/

## Solution
From the quition we can get the clue : Two invites with same md5 hash, but there are slightly different.
So we know that this is the same characteristic with the **MD5 COLLISION**.

The **HINTS** are telling us that, this question is about `WEB EXPLOTATION` and `PHP SITE CHECKING RULES`.

`PHP SITE CHECKING RULES` is refer to how PHP site checking PDFs file and md5 hash.


<h3 id="md5_col">MD5 COLLISION </h3>
First, what is a MD5 Collision ?
If we try to explain it in a simple way, it means that we can get two same md5 hash value with two different content of file. The probability is very same in usual way. Before 2005, the MD5 crytographyc has function is still secure. The crytographic hash function MD5 has been broken when 2005 and proved by Xiaoyun Wang and Hongbo Yu of Shandong University in China.
For more details, can look for this <a href="https://www.mathstat.dal.ca/~selinger/md5collision/">website</a>

### PHP site checking rules
1. How PHP site check the file uploaded is a valid PDF file?
   
Below is the sample PHP code telling us how PHP checking rules on PDF file :
```php
$_FILES['form_name_for_input_type_equals_file']['type'] ---> check if mime type here is application/pdf
```
From the code above, we know that the file that we choose to upload must with the content-type which is **application/pdf**.

2. How PHP site check the files uploaded with two same hash value ?
   
Below is the sample PHP code using md5_file to get the md5 hash value of the files :
```php

$filename = "test.txt";
$md5file = md5_file($filename);
```
So, when the site received two files uploaded by the user, the php code will get the md5 hash values of these two files and then do the comparison. In this question, the two hash values mush be the same. [(MD5 COLLISION)](#md5_col)

<hr>
Let's get started to solve it.

First, open the Burpsuite. Then, we enter to the proxy section, and open the Burp's embedded browser. 
Visit the link in the question http://mercury.picoctf.net:11590/.

Then, we move forward to the page, and upload two files with same hash value.

We can just download two examples file from the [here](https://www.mathstat.dal.ca/~selinger/md5collision/) which are `hello` and `erase` (two pairs of executable programs which have same hash value).

After we uploaded them to the website, we can alter the request in BurpSuite.

The Content-Type of the executable programs that we uploaded is application/octet-stream, so we need to change it to application/pdf to let the php site think that they are PDF files.
```
------WebKitFormBoundaryYh7VZThJTtwMVn7q
Content-Disposition: form-data; name="file1"; filename="hello"
Content-Type: application/pdf
```

```
------WebKitFormBoundaryYh7VZThJTtwMVn7q
Content-Disposition: form-data; name="file2"; filename="erase"
Content-Type: application/pdf
```

After forwarded the request, we can get the source code in the browser which with the php script
```html
<?php

if (isset($_POST["submit"])) {
    $type1 = $_FILES["file1"]["type"];
    $type2 = $_FILES["file2"]["type"];
    $size1 = $_FILES["file1"]["size"];
    $size2 = $_FILES["file2"]["size"];
    $SIZE_LIMIT = 18 * 1024;

    if (($size1 < $SIZE_LIMIT) && ($size2 < $SIZE_LIMIT)) {
        if (($type1 == "application/pdf") && ($type2 == "application/pdf")) {
            $contents1 = file_get_contents($_FILES["file1"]["tmp_name"]);
            $contents2 = file_get_contents($_FILES["file2"]["tmp_name"]);

            if ($contents1 != $contents2) {
                if (md5_file($_FILES["file1"]["tmp_name"]) == md5_file($_FILES["file2"]["tmp_name"])) {
                    highlight_file("index.php");
                    die();
                } else {
                    echo "MD5 hashes do not match!";
                    die();
                }
            } else {
                echo "Files are not different!";
                die();
            }
        } else {
            echo "Not a PDF!";
            die();
        }
    } else {
        echo "File too large!";
        die();
    }
}

// FLAG: picoCTF{c0ngr4ts_u_r_1nv1t3d_3d3e4c57}

?>
<!DOCTYPE html>
<html lang="en">

<head>
    <title>It is my Birthday</title>


    <link href="https://maxcdn.bootstrapcdn.com/bootstrap/3.2.0/css/bootstrap.min.css" rel="stylesheet">

    <link href="https://getbootstrap.com/docs/3.3/examples/jumbotron-narrow/jumbotron-narrow.css" rel="stylesheet">

    <script src="https://ajax.googleapis.com/ajax/libs/jquery/3.3.1/jquery.min.js"></script>

    <script src="https://maxcdn.bootstrapcdn.com/bootstrap/3.3.7/js/bootstrap.min.js"></script>


</head>

<body>

    <div class="container">
        <div class="header">
            <h3 class="text-muted">It is my Birthday</h3>
        </div>
        <div class="jumbotron">
            <p class="lead"></p>
            <div class="row">
                <div class="col-xs-12 col-sm-12 col-md-12">
                    <h3>See if you are invited to my party!</h3>
                </div>
            </div>
            <br/>
            <div class="upload-form">
                <form role="form" action="/index.php" method="post" enctype="multipart/form-data">
                <div class="row">
                    <div class="form-group">
                        <input type="file" name="file1" id="file1" class="form-control input-lg">
                        <input type="file" name="file2" id="file2" class="form-control input-lg">
                    </div>
                </div>
                <div class="row">
                    <div class="col-xs-12 col-sm-12 col-md-12">
                        <input type="submit" class="btn btn-lg btn-success btn-block" name="submit" value="Upload">
                    </div>
                </div>
                </form>
            </div>
        </div>
    </div>
    <footer class="footer">
        <p>&copy; PicoCTF</p>
    </footer>

</div>

<script>
$(document).ready(function(){
    $(".close").click(function(){
        $("myAlert").alert("close");
    });
});
</script>
</body>

</html>

```

### Result
We can get the flag from the source code.
```
// FLAG: picoCTF{c0ngr4ts_u_r_1nv1t3d_3d3e4c57}
```
