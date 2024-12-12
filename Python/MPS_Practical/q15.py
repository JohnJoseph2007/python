import mysql.connector as ms

con = ms.connect(host="localhost", user='root', passwd='password123', database='office')
cur = con.cursor()

cur.execute("SELECT * from employee")
x = cur.fetchall()
for i in x:
    print(i)

con.close()