import requests
from bs4 import BeautifulSoup

url = 'https://news.v.daum.net/v/20190728165812603'
resp = requests.get(url)

soup = BeautifulSoup(resp.text, "lxml")
soup.select('h3')	#list로 받아오기
soup.select('#harmonyContainer p')	#ID는 # harmonyContainer에 존재하는 모든 p를 찾아라 
#자손은 띄어쓰기 그냥 아래  자식은 > 바로 하위에 있음
soup.select('h3.tit_view')	#CLASS명은 .으로

soup.select('h3[class="tit_view"]')
#속성은 [name='test'] name^은 시작하는 이름 name$은 끝나는 이름
#name*은 포함하는 것을 찾겠다.

print(soup.select('span.txt_info:nth-child(1)'))





 
