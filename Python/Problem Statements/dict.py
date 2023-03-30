# WAP to iterate a given list and count the occurence of each item. Create a dictionary to
# show the occurence of each element

# sample input = [11, 45, 8, 23, 45, 23, 53]
# sample output = {11:1, 45:2, 23:2, 53:1, 8:1}

sample = [11, 45, 8, 23, 45, 23, 53]
dict = {}

for i in sample:
    if i in dict:
        dict[i]+=1
    else:
        dict[i]=1
    
print(dict)
