import mysql.connector as ms

con = ms.connect(host="localhost", user='root', passwd='password123', database='records')
cur = con.cursor()

cur.execute("create table Rec (name varchar(30) NOT NULL, age int(3) NOT NULL)")
con.commit()

for i in range(10):
    name = input("Enter name: ")
    age = int(input("Enter age: "))
    cur.execute("insert into Rec values({},{})".format(name, age))
    con.commit()

cur.execute("SELECT * from Rec ORDER BY age desc")
x = cur.fetchall()
for i in x:
    print(i)

con.close()