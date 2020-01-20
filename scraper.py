from bs4 import BeautifulSoup
from selenium import webdriver
import requests
import pymysql
  

db = pymysql.connect(
      host = "koriny-db.c3opeumbjgdz.us-east-1.rds.amazonaws.com",
      user = "mtyuser",
      password = "mtygroup1234",
      database = "mty"
)
   
headers = requests.utils.default_headers()
headers.update({ 'User-Agent': 'Google Chrome/77.0.3865.120',})

for i in range(1):
    webpage = requests.get("https://www.cssanyu.org/bbs2/forum.php?mod=forumdisplay&fid=41&page=%variable%", headers=headers)
    soup = BeautifulSoup(webpage.text,'html.parser')

    title_list = soup.find_all('a',href=True, attrs={'class':'s xst'})
    user_name = soup.find_all('a', href=True, attrs= {'c':'1'})


    cursor = db.cursor()
    
    for lists, name in zip(title_list, user_name):

        new_lists = []
        new_lists.append(lists.text)
        new_lists.append(name.text)
        print(new_lists)

        x = "INSERT INTO mty.cssa_rent (title, username) VALUES (%s, %s)"
        val = (new_lists)

        cursor.execute(x, val)


# fetches all the rows of a query result
remaining_rows = cursor.fetchall()   

#db.commit()
print(cursor.rowcount, "Record Inserted")
db.close()
    
    
    
    
    
