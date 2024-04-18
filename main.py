import pandas as pd
import csv
import pymysql
dF=pd.read_csv("Sample.csv")
print(dF)


with open("Sample.csv",'r')  as file:
  reader=csv.reader(file)
  next(reader)
  connection = pymysql.connect(host="localhost", user="root",  password="" ,db="nikhildb")
  cursor=connection.cursor()
  for row in reader:
           cursor.execute("INSERT INTO csv  VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)",row)
           connection.commit()


cursor.close()
connection.close()
