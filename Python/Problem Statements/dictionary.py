#WAP to print a dictionary where keys are numbers between 1 to 15 and values are the square of the keys
keys = []
values = []

for i in range(1, 16):
    keys.append(i)
    values.append(i*i)

a = dict(zip(keys, values))

print(a)
