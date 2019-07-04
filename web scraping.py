import pymysql
import requests
from bs4 import BeautifulSoup

#Web Scraping (100 movies)
result=requests.get("https://www.imdb.com/list/ls006266261/")
soup=BeautifulSoup(result.text,features="html.parser")

l=soup.find_all('h3',{'class':'lister-item-header'})
m_name=[]
for x in l:
    for y in x.find_all('a'):
        m_name.append(y.text)
        
m_rate=[]      
r=soup.find_all('div',{'class':'ipl-rating-star small'})
for x in r:
    for y in x.find_all("span",{'class':'ipl-rating-star__rating'}):
        m_rate.append(y.text)
print(m_name)
print(m_rate)
