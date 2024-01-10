s = input("Enter string: ").split()
n = ""
for i in s:
    newstring=""
    for j in range(len(i)):
        if j==1:
            newstring=newstring+chr(ord(i[j])-32)
        else:
            newstring=newstring+i[j]
    n=n+newstring+" "

print(n)

