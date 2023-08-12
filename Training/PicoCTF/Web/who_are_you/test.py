
import requests

url = "http://mercury.picoctf.net:1270/"

headers = {
	'User-Agent': 'picobrowser',
    'referer' : 'mercury.picoctf.net:1270',
    'Date' : '2018',
    # DNT (Do not track)
    'DNT' : '1',
    'X-Forwarded-For' : '2.16.66.0',
    'Accept-Language' : 'sv'
}


res =requests.get(url, headers=headers)

print(res.status_code)


with open("response.html","w", encoding="utf-8") as f:
	f.write(res.content.decode())
