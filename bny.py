# web-scraping for the "bondnewyork.com" using Beautifulsoup, selenium and put the data by using pandas (CSV file)
# with python

from bs4 import BeautifulSoup
from urllib.parse import urljoin
import pandas as pd
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import NoSuchElementException
import requests
import time
import pymysql 
import json
import re

headers = requests.utils.default_headers()
headers.update({'User-Agent': 'Mozilla/5.0'})

var1 = 1 
var2 = 8
lists = []
agent = []

# Fetching Url  
base_url = "https://www.bondnewyork.com"
url = "https://www.bondnewyork.com/index.cfm?page=agents&state=search&term=&office=6"

driver= webdriver.Firefox()
driver.get(url)

for i in range(var1,var2):
      
      # wait, refresh and reload
      wait =  WebDriverWait(driver, 10)
      element = wait.until(EC.presence_of_element_located((By.XPATH,'//li//a[@class="paging"]')))
     
      content = driver.page_source 
      soup = BeautifulSoup(content,"lxml")

      get_url = soup.find_all('li', attrs={'class':'item'}) 

      for a in get_url:
          x = a.find('a').get("href")
          link = urljoin(base_url,x)
          # print(link)
          lists.append({"url": link})
          # print(lists)

      # if there are pages keeping clicking and looping, otherwise "stop" (break)
      try:
          driver.find_element_by_xpath('//li//a[@class="paging"][text()="' + str(i+1) + '"]').click()
      except NoSuchElementException:
            break
    
for info in lists:

    samplePage = requests.get(info["url"], headers=headers)
    bs = BeautifulSoup(samplePage.text, 'html.parser')
    # print(link)
    names = bs.find_all('span', attrs = {'class':'title'}
    phones = bs.find_all('div', attrs = {'class':'col-xs-12 col-lg-4 agent-contact-links'})
    for div in phones:
        phone = div.find('a')['href']
        # print(phone)

    emails = bs.find_all('input', attrs = {'name': 'agentEmail'})
    
    for email,name,phonenum in zip (emails,names,phone):
        email = emails[0].attrs
        y = json.dumps(email)         # outputing string from a dict using json.dumps
        x = json.loads(y)             # parse y 
        value = x['value']            # result is a python dictionary
        name = names[0].text
        phonenum = phone
        agent.append({"Agent-name": name ,"Phone": phonenum, "Email": value})
        print(agent) 
  # print('//li//a[@class="paging"][text()="' + str(i+1) + '"]')

driver.quit()

# putting data by using pandas (CSV file)  
data = agent
df = pd.DataFrame(data)
print(df)
print("Data have been saved !!! ")
df.to_csv('bny_HQ.csv', index=False, encoding='utf-8')
