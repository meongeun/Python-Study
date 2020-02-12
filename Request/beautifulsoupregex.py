import re
from bs4 import BeautifulSoup
import requests

url = 'https://news.v.daum.net/v/20190728165812603'
resp = requests.get(url)
soup = BeautifulSoup(resp.text, "lxml")
soup.find_all(re.compile('h\d'))

soup.find_all('img', attrs = {'src': re.compile('.+\.jpg')})
soup.find_all('h3', class_ = re.compile('.+newsview$'))


