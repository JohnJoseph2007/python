s = input("Enter string: ").split()
d = {}
for i in s:
    if i not in d:
        d[i] = s.count(i)

print(d)