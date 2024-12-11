import mysql.connector as ms

def search(rno):
    cur.execute("SELECT * from student WHERE rollno={}".format(rno))
    x = cur.fetchall()
    if len(x)==0:
        print("Record does not exist")
    else:
        print("Record exists.")

con = ms.connect(host="localhost", user='root', passwd='password123', database='school')
cur = con.cursor()

rin = int(input("enter roll no.: "))
search(rin)
