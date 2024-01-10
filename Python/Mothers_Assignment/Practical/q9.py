n = int(input("Enter length of tuple: "))
l = []
for i in range(n):
    l.append(eval(input("Enter item: ")))

t = tuple(l)
p = 1

for i in t:
    if type(i)==int:
        p*=i

print(p)