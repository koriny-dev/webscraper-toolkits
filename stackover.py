# web-scraping for the "stackoverflow.com" using Beautifulsoup, selenium with python

from bs4 import BeautifulSoup
from urllib.parse import urljoin
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import requests
import json
import re


question = []
lists = []

headers = requests.utils.default_headers()
headers.update({'User-Agent':'Mozilla/5.0'})

var1 = 0 
var2 = 1

for i in range(var1,var2):
   # Fetching Url  
    base_url = "https://stackoverflow.com/"
    url = "https://stackoverflow.com/questions/59078411/setting-react-props-state-from-jquery-tree-event"

    driver = webdriver.Firefox()
    driver.get(url+str(i))

    content = driver.page_source
    soup = BeautifulSoup(content,"lxml")

    #fetching URLs 
    rents = soup.find_all('a', attrs={'class':'question-hyperlink'})

    for rent in rents:
            x = rent.get("href")
            link = urljoin(base_url,x)
            lists.append({"url": link})
            print(lists)
     
    cursor = db.cursor()

    for info in lists:

        samplePage = requests.get(info["url"], headers=headers)
        bs = BeautifulSoup(samplePage.text, 'html.parser')
        # print(link)
        users = bs.find_all('span', attrs = {'class':'d-none'})
        titles = bs.find_all('a', attrs = {'class':'question-hyperlink'})
        for title,user in zip (titles,users):
            title = titles[0].text
            user = users[0].text
            question.append({"title": title ,"User_id" : user})
            print(question)
        
        driver.quit()