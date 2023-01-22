# WAP to print the numbers from userdefined n to 0 using recursion

inp = int(input("Enter n: "))

# def rec(n):
#     j = n
#     arr = []
#     for i in range(0, j+1):
#         arr.append(i)
#     arr.reverse()
#     for i in arr:
#         print(i)

def rec(n):
    print(n)
    n-=1
    if(n==-1):
        return
    rec(n)

rec(inp)