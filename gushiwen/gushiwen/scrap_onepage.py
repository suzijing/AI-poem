import requests
from bs4 import BeautifulSoup
url='https://www.gushiwen.org/shiwen/default.aspx?page=1'
web_data = requests.get(url)

soup = BeautifulSoup(web_data.text, 'lxml')
contents=soup.select('div[class="main3"]')[0]
contents=contents.select('div[class="left"]')[0]
contents=list(contents.select('div[class="sons"]'))

for c in contents:
    title=c.select('b')[0].text
    author=c.select('p[class="source"]')[0].text
    text=c.select('div[class="contson"]')[0].text
    #text=re.sub(rex,"",text)
    #text=text.replace('\n','')
    print('标题:'+title)
    print('作者:'+author)
    print(text)

