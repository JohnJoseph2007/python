n = int(input("Enter length of list: "))
l = []
for i in range(n):
    l.append(eval(input("Enter item: ")))

for i in range(n):
    if i==0 or i==2 or i==3:
        l.pop(i)

print(l)
