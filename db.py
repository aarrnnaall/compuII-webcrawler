import mysql.connector

con = mysql.connector.connect(user="root",password="",host="127.0.0.1",database="crawler")

cursor=con.cursor()
cursor.execute("CREATE TABLE auto (id INT, url VARCHAR(100), title VARCHAR(100), description VARCHAR(200));")

con.close()






        
