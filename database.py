# web-scraping for the "heykorea.com" using Beautifulsoup, selenium, and put the data in to the database with python

from bs4 import BeautifulSoup
from urllib.parse import urljoin
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
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

###  INSERT RECORD  ### 
insert = "INSERT INTO mty.rent_sample(title, rent_type, rent_location, rent_price) VALUES ('{0}', '{1}', '{2}', '{3}')".format(title_list,rent_room,rent_loc,rent_price)
cursor.execute(insert)
remaining_rows = cursor.fetchall()  ## fetches all the rows of a query result
# db.commit()
print(cursor.rowcount, "Record Inserted")
db.rollback()
db.close()


###  CREATE A TABLE  ###
create = "CREATE TABLE mty.rent_sample(id INT NOT NULL AUTO_INCREMENT, title VARCHAR(100), rent_type VARCHAR(50),rent_location VARCHAR(50), rent_price VARCHAR(50), primary key (id))"
cursor.execute(create) 
print("Table has been create successfully ... ")
# db.commit()
db.close()


###  DISPLAY RECORD  ###   
select = "SELECT * FROM mty.sample_hk"
cursor.execute(select)
remaining_rows = cursor.fetchall() 
print("Total number of record: ", cursor.rowcount)  
print("Rent Information")
# print(remaining_rows)
for i in remaining_rows:
    id = i[0]
    title = i[1]
    rent_type = i[2]
    rent_location = i[3]
    rent_price = i[4]
    print(id, title, rent_type, rent_location, rent_price)
cursor.close()
db.close()
print("MySQL connection is closed")    


# ###  UPDATE RECORD  ###
update = "UPDATE mty.sample_hk SET id = 40 WHERE id = 39 " 
cursor.execute(update)
# db.commit()
print("Record updated successfully ...")
db.rollback()
db.close()