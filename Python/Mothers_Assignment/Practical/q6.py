n = int(input("Enter length of list: "))
l = []
for i in range(n):
    l.append(eval(input("Enter item: ")))

u = []
for i in l:
    if i not in u:
        u.append(i)
    else:
        continue

print(u)
