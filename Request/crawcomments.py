import requests

url = 'https://comment.daum.net/apis/v1/posts/@20190728165812603'

resp = requests.get(url)
print(resp)

headers = {
    'Authorization': 'Bearer eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJncmFudF90eXBlIjoiYWxleF9jcmVkZW50aWFscyIsInNjb3BlIjpbXSwiZXhwIjoxNTY0NjcxNDAwLCJhdXRob3JpdGllcyI6WyJST0xFX0NMSUVOVCJdLCJqdGkiOiI3MDllNDI5MC0yZmJjLTRmOTUtOTJlOC1mMTAzMDk5ZjYyYTciLCJjbGllbnRfaWQiOiIyNkJYQXZLbnk1V0Y1WjA5bHI1azc3WTgifQ.fQU2739LvY9EZLlNs-Go1VlCVEtz-I-JdS_kKJeOLDc',
    'Origin': 'https://news.v.daum.net',
    'Referer': 'https://news.v.daum.net/v/20190728165812603',
    'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/75.0.3770.142 Safari/537.36'
}
resp = requests.get(url, headers=headers)
resp.json()['commentCount']

#data = resp.json()
#data['commentCount']







