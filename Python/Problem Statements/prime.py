count = 0
num = int(input("Enter a number"))
for i in range(1, num+1):
    count = count+1 if num%i==0 else count+0
print("Is prime" if count==2 else "Is not prime")