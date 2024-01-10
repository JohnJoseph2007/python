n = int(input("Enter length of list: "))
l = []
for i in range(n):
    l.append(int(input("Enter number: ")))

pc = 0
nc = 0
zc = 0

for i in l:
    if i>0:
        pc+=1
    elif i<0:
        nc+=1
    elif i==0:
        zc+=1

print("Zero Count:", zc, "\nPositive Count:", pc, "\nNegative Count:", nc)