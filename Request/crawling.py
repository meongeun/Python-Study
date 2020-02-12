import requests
url = 'https://news.v.daum.net/v/20190728165812603'
resp = requests.get(url)

print(resp) 

print(resp.text)
