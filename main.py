import pandas as pd
import csv
import pymysql
dF=pd.read_csv("Sample.csv")
print(dF)


with open("Sample.csv",'r')  as file:
  reader=csv.reader(file)
  connection = pymysql.connect(host='localhost', user='root',  password='Year' ,db='nikhildb')
  cursor=connection.cursor()
  for row in reader:
           cursor.execute('INSERT INTO csv (`Region`, `Country`, `Item Type`, `Sales Channel`, `Order Priority`, `Order Date`, `Order ID`, `Ship Date`, `Units Sold`, `Unit Price`, `Unit Cost`, `Total Revenue`, `Total Cost`, `Total Profit`) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)',row)
           connection.commit()


cursor.close()
connection.close()
