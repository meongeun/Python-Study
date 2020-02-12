from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By

from bs4 import BeautifulSoup

import time

chrome_driver = '~/Users/chormedriver'

driver = webdriver.Chrome(chrome_driver)
driver.get('https://www.python.org')

time.sleep(2)

driver.close()





