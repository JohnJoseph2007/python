# Create a function maxsalary() in Python to read all the records
# from an already existing file record.csv which stores the records
# of various employees working in a department

import csv

def maxsalary():
    with open("Python/Mothers_Assignment/XIIPractice/TextFileHandling/SalaryMax/record.csv", "r", newline='') as f:
        x=csv.reader(f)
        next(x)
        max = 0
        mx = []
        for i in x:
            if int(i[3])>=max:
                max=int(i[3])
                mx = i
        print(mx)

maxsalary()

# Works √