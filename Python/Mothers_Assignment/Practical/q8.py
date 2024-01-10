n = int(input("Enter length of list: "))
l = []
for i in range(n):
    l.append(eval(input("Enter item: ")))

searchterm = eval(input("Enter term to be searched: "))
for i in range(n):
    if searchterm==l[i]:
        print(i)
        break
else:
    print("Not Available")