n = int(input("Enter length of dictionary: "))
d = {}
for i in range(n):
    key = eval(input("Enter key: "))
    value = eval(input("Enter value: "))
    d[key]=value

search = eval(input("Enter search term: "))

if search in d:
    del d[search]

print(d)
