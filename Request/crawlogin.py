import requests
from bs4 import BeautifulSoup

url = 'https://www.kangcom.com/member/member_check.asp'

data = {
'id': 'macmath22',
'pwd': 'Test1367!'
}

s = requests.Session()

s.post(url, data=data)
print(resp)

my_page = 'https://www.kangcom.com/mypage/'
resp = s.get(my_page)

soup = BeautifulSoup(resp.text, "lxml")
td=soup.select_one('td.a_bbslist55:nth-child(3)')
mileage = td.get_text()

mileage
