from bs4  import BeautifulSoup
import lxml#backup parser
import os
import requests

#Pulling from a live webpage
response = requests.get('https://news.ycombinator.com/news')
print(response.text)