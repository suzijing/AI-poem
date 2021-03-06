import requests
from bs4 import BeautifulSoup
import sqlite3
conn=sqlite3.connect('test.db')
cur=conn.cursor()

url='https://www.gushiwen.org/shiwen/default.aspx?page=1'
web_data = requests.get(url)
soup = BeautifulSoup(web_data.text, 'lxml')
contents=soup.select('div[class="main3"]')[0].select('div[class="left"]')[0]
contents=list(contents.select('div[class="sons"]'))

for c in contents:
    title=c.select('b')[0].text
    author=c.select('p[class="source"]')[0].text
    text=c.select('div[class="contson"]')[0].text
    sql="insert into poetry values(?,?,?)"
    data=(title,author,text)
    cur.execute(sql,data)
    conn.commit()
conn.close()
    

