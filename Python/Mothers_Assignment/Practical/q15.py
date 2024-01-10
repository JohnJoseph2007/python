n = int(input("Enter number of employees: "))
d = {}
for i in range(n):
    eid = int(input("Enter employee id: "))
    en = input("Enter employee name: ")
    es = float(input("Enter employee salary: "))
    d[eid]={"empname":en, "empsalary":es}

for i in d:
    print("Employee ID: ", i, "\nEmployee Name: ", d[i]["empname"], "\nEmployee Salary: ", d[i]['empsalary'])
