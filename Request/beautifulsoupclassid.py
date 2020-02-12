import requests
from bs4 import BeautifulSoup

url = 'https://news.v.daum.net/v/20190728165812603'
resp = requests.get(url)
resp.text

soup = BeautifulSoup(resp.text, "lxml")
title = soup.find('h3', class_='tit_view')
title.get_text()

soup.find_all('span', class_ = 'txt_info')[0]
soup.find_all('span', class_ = 'txt_info')[1]

info =soup.find('span', class_ ='info_view')
info.find('span', class_ ='txt_info')

container = soup.find('div', id = 'harmonyContainer')
contents = ''
for p in container.find_all('p'):
	contents += p.get_text().strip()

print(contents)


