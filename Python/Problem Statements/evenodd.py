list = [62, 7, 35, 1, 1000, 99]
odd = []
even = []
for i in list:
    if i%2==0:
        even.append(i)
    else:
        odd.append(i)

print(odd)
print(even)