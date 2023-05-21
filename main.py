# this is a basic web scraper that counts how many times a word appears on a website

import requests

response = requests.get('https://en.wikipedia.org/wiki/Computer_science')
print("connected to website")
