n = int(input("Enter length of tuple: "))
l = []
for i in range(n):
    l.append(eval(input("Enter item: ")))
t=tuple(l)
u=()
for i in t:
    if type(i)==list:
        if len(i)>=3:
            u=u+(100,)
        else:
            u=u+(i,)
    else:
        u=u+(i,)

print(u)