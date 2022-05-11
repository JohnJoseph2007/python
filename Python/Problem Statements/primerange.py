#Enter 2 numbers, then find prime numbers between that range.

numstart = int(input("Enter start number"))
numend = int(input("Enter end number"))
for i in range(numstart, numend+1):
    for j in range(2, i+1):
        if i%j==0:
            break
        else:
            print(i)
    