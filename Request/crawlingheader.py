import requests 

url = 'https://news.v.daum.net/v/20190728165812603'
headers = {
	'user-agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/75.0.3770.142 Safari/537.36'
}

resp = requests.get(url, headers = headers)
resp.text

