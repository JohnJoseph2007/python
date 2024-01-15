n = int(input("Enter number of employees: "))
d = {}
for i in range(n):
    eid = int(input("Enter employee id: "))
    en = input("Enter employee name: ")
    es = float(input("Enter employee salary: "))
    d[eid]= (en, es)

for i in d:
    print("\nEmployee ID: ", i, "\nEmployee Name: ", d[i][0], "\nEmployee Salary: ", d[i][1],"\n")
