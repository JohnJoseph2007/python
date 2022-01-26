import string


def count_set_bits(arr, n):
    #Write your code here..
    binary = 0
    stringbinary=""
    onecount = 0
    hey = 0
    for i in arr:
        binary = bin(i)[2:]
        stringbinary = str(binary)
        for j in stringbinary:
            if j=="1":
                onecount+=1
            else:
                hey+=1
    return onecount

t=int(input())
for _ in range(t):
    n=int(input())
    arr=[int(x) for x in input().strip().split()]
    print(count_set_bits(arr,n))