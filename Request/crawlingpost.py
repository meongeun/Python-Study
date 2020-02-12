import requests
url = 'https://www.kangcom.com/member/member_check.asp'
data = {
	'id': 'macmath22',
	'pwd': 'Test1357!'
}

resp = requests.post(url, data = data)
print(resp.text)

