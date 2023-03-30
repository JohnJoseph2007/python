# Create a new list from the available 2 lists. Pick all odd index items from the first list 
# and even indexed items from the second list
# Sample input : 
# l1 = [3,6,9,12,15,18,21]
# l2 = [4,8,12,16,20,24,28]
# Sample output:
# l3 = [6,12,18,4,12,20,28]

l1 = [3,6,9,12,15,18,21]
l2 = [4,8,12,16,20,24,28]
l3=[]

# for i in range(len(l1)):
#     if i%2==1:
#         l3.append(l1[i])

# for i in range(len(l2)):
#     if i%2==0:
#         l3.append(l2[i])
        
# print(l3)

odd = l1[1::2]
even = l2[0::2]

print(odd, even)