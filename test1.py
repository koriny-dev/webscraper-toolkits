from bs4 import BeautifulSoup
from urllib.parse import urljoin
import requests
import pymysql 
import json
import re


db = pymysql.connect(
    host = "koriny-db.c3opeumbjgdz.us-east-1.rds.amazonaws.com",
    user = "mtyuser",
    password = "mtygroup1234",
    database = "mty",
    charset='utf8mb4',
)

headers = requests.utils.default_headers()
headers.update({ 'User-Agent': 'Google Chrome/77.0.3865.120',})

var1 = 0 
var2 = 1

for i in range(var1,var2):
   # Fetching Url  
    base_url = "https://www.cssanyu.org/bbs2/"
    url = "https://www.cssanyu.org/bbs2/forum.php?mod=forumdisplay&fid=41&page=1"

    webpage = requests.get(url, headers=headers)
    soup = BeautifulSoup(webpage.text,'html.parser')

    #fetching URLs 
    rents = soup.find_all('a', attrs={'class':'s xst'})
    lists = []

    for rent in rents:
            x = rent.get("href")
            link = urljoin(base_url,x)
            lists.append({"url": link, "title": rent.text})
            # print(lists)
     

    rent_new = []
    cursor = db.cursor()

    for info in lists:

        samplePage = requests.get(info["url"], headers=headers)
        bs = BeautifulSoup(samplePage.text, 'html.parser')
        # print(link)
        describes = bs.find_all('td', attrs = {'class':'t_f'})
        titles = bs.find_all('h1', attrs = {'class':'ts'})
        for title,describe in zip (titles,describes):
            title = titles[0].text.strip()
            describe = describes[0].text.strip()
            rent_new.append({"title": title ,"description" : describe})
            print(rent_new)
