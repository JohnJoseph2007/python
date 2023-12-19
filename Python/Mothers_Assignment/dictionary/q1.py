st = {}
n = int(input("Enter number of students: "))
for i in range(n):
    name = input("Enter name: ")
    roll = int(input("Enter roll no.: "))
    avg = float(input("Enter average: "))
    st[str(i+1)]={'name':name, 'roll':roll, 'avg':avg}

for i in st:
    if st[i]['avg'] > 90:
        print("Name - ", st[i]['name'])
        print("Roll no. - ", st[i]['roll'])
        print("Average - ", st[i]['avg'])
    else:
        continue