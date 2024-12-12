import mysql.connector as ms

con = ms.connect(host="localhost", user='root', passwd='password123', database='office')
cur = con.cursor()

def delete(eno):
    cur.execute("DELETE from employee where eno={}".format(eno))
    con.commit()

e = int(input("Enter employee id to delete: "))
delete(e)

con.close()