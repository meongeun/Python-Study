from bs4 import BeautifulSoup

html = '''
<html>
  <head>
    <title>BeautifulSoup test</title>
  </head>
  <body>
    <div id='upper' class='test' custom='good'>
      <h3 title='Good Content Title'>Contents Title</h3>
      <p>Test contents</p>
    </div>
    <div id='lower' class='test' custom='nice'>
      <p>Test Test Test 1</p>
      <p>Test Test Test 2</p>
      <p>Test Test Test 3</p>
    </div>
  </body>
</html>'''

soup = BeautifulSoup(html, "lxml")
print(soup.find('h3'))
tag = soup.find('h3')
print(tag.get_text().strip())

soup.find('p')
soup.find('div', custom= 'nice')	#속성을 줌
soup.find('div', class_='test')
attrs = {'id': 'upper', 'class':'test'}
soup.find('div', attrs = attrs)	#multi 속성
soup.find_all('p')	#리스트 형식으로 반환
soup.find_all('div', class_='test')

#attribute값 추출
tag = soup.find('h3')
print(tag)
tag['title']


