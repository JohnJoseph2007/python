import pickle
import os

w = open("Python/MPS_Practical/q12/student.dat", 'wb')
n = int(input("Enter no. of records to input: "))
for i in range(n):
    id = int(input("Student ID: "))
    sname = input("Student name: ")
    marks = float(input("Marks: "))
    pickle.dump({"sid":id, "name":sname, "marks":marks}, w)
w.close()

def update():
    search = int(input("Enter student id to search: "))
    f = open("Python/MPS_Practical/q12/student.dat", 'rb')
    fw = open("Python/MPS_Practical/q12/student2.dat", 'wb')
    found = False
    try:
        while True:
            x=pickle.load(f)
            if x['sid']==search:
                minp = float(input("Enter updated marks: "))
                x['marks'] = minp
                pickle.dump(x, fw)
                found = True
    except EOFError:
        if found:
            print("Record found and updated")
        else:
            print("Record does not exist")

        os.remove("Python/MPS_Practical/q12/student.dat")
        os.rename("Python/MPS_Practical/q12/student2.dat", "Python/MPS_Practical/q12/student.dat")
    f.close()
    fw.close()

update()