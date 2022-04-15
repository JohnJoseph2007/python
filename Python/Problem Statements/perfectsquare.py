import math

def perfect(num):
    if num>0:
        a = int(math.sqrt(num))
        return(a*a==num)
    return False
        # if num == a*a:
        #     return True
        # else:
        #     return False

input = int(input("Enter a number: "))

if perfect(input):
    print("Perfect :)")
else:
    print("Not perfect :(")
