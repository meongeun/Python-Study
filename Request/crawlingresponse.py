import requests
url = 'https://news.v.daum.net/v/20190728165812603'
resp = requests.get(url)

if resp.status_code == 200:
	resp.headers
else:
	print('error')
