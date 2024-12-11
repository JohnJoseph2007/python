# WAP to generate random values from 1 to 10 and add
# to the list and then remove all the odd nos. from it.

import random

ls = []
n = int(input("Enter no. of items: "))
for i in range(n):
    ls.append(random.randint(1, 10))

lscopy = ls[:]

for i in ls:
    if i%2==1:
        lscopy.remove(i)

print("Original list:", ls)
print("Updated list:", lscopy)