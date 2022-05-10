#Enter 2 numbers, then find prime numbers between that range.

array = []
numstart = int(input("Enter start number"))
numend = int(input("Enter end number"))
for i in range(numstart, numend+1):
    for j in range(1, i+1):
        count = 0
        count = count+1 if j%i==0 else count+0
        print(f"{j} is prime" if count==2 else "Is not prime")
