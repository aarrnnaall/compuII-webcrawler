import mysql.connector

db=mysql.connector.connect(host="localhost",user="root",password="",db="crawler")
c = db.cursor()
c.execute("SELECT * FROM auto")
result_set = c.fetchall()
for row in result_set:
    print(row[1])
