# this is a basic web scraper that counts how many times a word appears on a website

import requests
import webdriver_manager.drivers.chrome
from bs4 import BeautifulSoup
from selenium.webdriver import Chrome
from selenium import webdriver
from selenium.webdriver.common.by import By

word_choice = input("choose a word to search...")

link1 = 'https://en.wikipedia.org/wiki/Computer_science'
response = requests.get(link1)
print("connected to website")
soup = BeautifulSoup(response.text, "html.parser")
print(soup.title)

driver = webdriver.Chrome()
driver.get(link1)


count = 0
# Getting current URL source code
get_source = driver.page_source

# Text you want to search
search_text = word_choice


for search_text in get_source:
    count = count + 1

print(count)
