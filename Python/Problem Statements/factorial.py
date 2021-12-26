n = int(input("Enter the number to check factorial for: "))
result = 1
if n>0:
    for i in range(1, n+1):
        result=result*i
    print(result)
elif n==0:
    print("Factorial for 0 is 1")
else:
    print("YOU ENTERED A NEGATIVE NUMBER STUPID")