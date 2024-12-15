# WAP using a function to read from a binary file
# 'employee.dat' and print the avg salary of employee working in accounts
# The same program will create the binary file and store records=[enumber, name, salary, department]

import pickle

def avgsal():
    with open("Python/MPS_Practical/q5/employee.dat", 'rb') as f:
        c = 0
        s = 0
        try:
            while True: 
                x = pickle.load(f)
                if x[3].upper() == "ACCOUNTS":
                    s+=x[2]
                    c+=1
        except EOFError:
            if c==0:
                return "No employees in accounts dept."
            else:
                return s/c
        

n = int(input("Enter no. of employees: "))
w = open("Python/MPS_Practical/q5/employee.dat", 'wb')
for i in range(n):
    eno = int(input("Enter employee no.: "))
    nam = input("Enter employee name: ")
    sal = float(input("Enter salary: "))
    dep = input("Enter department: ")
    l = [eno, nam, sal, dep]
    pickle.dump(l, w)
w.close()

print("Average salary: " ,avgsal())

