from bs4 import BeautifulSoup
import requests

url='https://www.gushiwen.org/shiwen/default.aspx?page=1'
web_data = requests.get(url)
soup = BeautifulSoup(web_data.text, 'lxml')
content=soup.select('div[class="main3"]')[0]
content=content.select('div[class="left"]')[0]
#每一首诗都在一个class为sons的div里，其中第0个div为《将进酒》
content=content.select('div[class="sons"]')[0]
title=content.select('b')
print(title[0].text)

