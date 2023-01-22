# WAP to replace the last element in the list with another list
# a= [1, 2, 3, 4, 5]; b=[2, 3, 5, 4, 3]
# c= [1, 2, 3, 4, 2, 3, 5, 4, 3]

a = [1, 2, 3, 4, 5]
b = [2, 3, 5, 4 ,3]

a.pop()
# for i in b:
#     a.append(i)
c = a+b

print(c)
