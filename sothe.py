# web-scraping for the "www.sothebyshomes.com" using Beautifulsoup, selenium and put the data into pandas (CSV file)
# with python

from bs4 import BeautifulSoup
from urllib.parse import urljoin
import pandas as pd
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import requests
import time
import pymysql 
import json
import re

headers = requests.utils.default_headers()
headers.update({'User-Agent': 'Mozilla/5.0'})

name = []
mPh = []
oPh = []
eAdd = []

var1 = 1 
var2 = 13

for i in range(var1,var2):
   # Fetching Url  
    base_url = "https://www.sothebyshomes.com"
    url = "https://www.sothebyshomes.com/nyc/agents?page="

    driver= webdriver.Firefox()
    driver.get(url+ str(i))

    content = driver.page_source
    soup = BeautifulSoup(content,"lxml")
    # print (soup)
    
    # fetching URLs 
    get_url = soup.find_all('div', attrs={'class':'agents-thumb-cell-left'})
    lists = []

    for a in get_url:
        x = a.find('a').get("href")
        link = urljoin(base_url,x)
        # print(link)
        lists.append({"url": link})
        # print(lists)

    for info in lists:

        samplePage = requests.get(info["url"], headers=headers)
        bs = BeautifulSoup(samplePage.text, 'html.parser')
        users = bs.find_all('input', attrs = {'type':'text'})
        jsonData = json.loads(users[0]['value'])
        
        fullName = jsonData['fullName']
        mobilePhone = jsonData['mobilePhone']
        officePhone = jsonData['officePhone']
        email = jsonData['email']
        name.append(fullName)
        mPh.append(mobilePhone)
        oPh.append(officePhone)
        eAdd.append(email)
        # print(name,oPh)
    driver.quit()

data = {'Name':name,'Mobile': mPh,'Office': oPh, 'Email': eAdd}
df = pd.DataFrame(data)
# print(df)
print("Data have been saved !!! ")
# df.to_csv('sothe.csv', index=False, encoding='utf-8')
