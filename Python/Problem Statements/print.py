# Take an int input from the user, and print the number till that much (in a single line).

a = int(input("E: "))
s = ""
arr = []

for i in range(1, a+1):
    h = str(i)
    arr.append(h)

s = "".join(arr)

print(s)



# SECOND WAY:

# for i in range(1, a+1):
#     print(i, end="")