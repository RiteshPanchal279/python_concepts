import mysql.connector

db = mysql.connector.connect(
   host="localhost",
   user="root",
   passwd="root"
)

c=db.cursor()
c.execute('CREATE DATABASE mystudentdb')
c.execute('SHOW DATABASES')
for i in c:
   print(i)

c=db.cursor()
c.close()
db.close()