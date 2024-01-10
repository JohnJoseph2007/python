n = int(input("Enter length of dictionary: "))
d = {}
for i in range(n):
    key = eval(input("Enter key: "))
    value = eval(input("Enter value: "))
    d[key]=value

kv = list(d.items())
dl=[]
for i in kv:
    if i[1] in dl:
        d.pop(i[0])
    else:
        dl.append(i[1])

print(d)
