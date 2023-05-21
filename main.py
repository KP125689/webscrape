# this is a basic web scraper that counts how many times a word appears on a website

import requests
from bs4 import BeautifulSoup
from selenium.webdriver import Chrome
from selenium.webdriver.common.by import By

response = requests.get('https://en.wikipedia.org/wiki/Computer_science')
print("connected to website")
soup = BeautifulSoup(response.text, "html.parser")
print(soup.title)

driver = Chrome(executable_path='/path/to/driver')
driver.get('https://oxylabs.io/blog')

