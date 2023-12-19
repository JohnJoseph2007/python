st = {}
n = int(input("Enter no. of students: "))
for i in range(n):
    roll = int(input("Enter roll no.: "))
    name = input("Enter name: ")
    mark = []
    for i in range(5):
        mark.append(float(input("Enter mark in subject", i)))
    st[i] = {'roll':roll, 'name':name, 'mark':mark}

fail = []

for i in st:
    c = 0
    for j in st[i]['mark']:
        if j<40:
            c+=1
    if c>2:
        fail.append(st[i]['name'])

print("Failed students: ", fail)