import mysql.connector as ms

con = ms.connect(host="localhost", user='root', passwd='password123', database='office')
cur = con.cursor()

def update(eno):
    name = input("Enter new name: ")
    salary = int(input("Enter new salary: "))
    cur.execute("UPDATE employee SET (name = {}, sal = {}) where eno = {}".format(name, salary, eno))
    con.commit()

e = int(input("Enter employee id to update: "))
update(e)

con.close()