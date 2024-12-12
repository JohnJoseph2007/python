import csv

w = open("Python/MPS_Practical/q13/employee.csv", 'w', newline='')
writer = csv.writer(w)
init = ['Enumber', 'Ename', 'Basic', 'DA', 'HRA', 'SALARY']
writer.writerow(init)

def inp():
    eno = int(input("Enter employee number: "))
    enam = input("Enter name: ")
    basic = int(input("Enter basic salary"))
    da = int(input("Enter DA salary"))
    hra = int(input("Enter HRA salary"))
    total = basic + da + hra
    x = [eno, enam, basic, da, hra, total]
    writer.writerow(x)

n = int(input("Enter no. of entries: "))
for i in range(n):
    inp()
