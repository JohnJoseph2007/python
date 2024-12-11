# WAP that creates a text file flower.txt and write some lines to it.
# Read the contents of the file and count the lines
# having more than 3 words "lily" in each line

# File Creation:
w = open("Python/MPS_Practical/q6/flowers.txt",'w')
n = int(input("Enter no of lines: "))
x = ''
for i in range(n):
    inp = input("Enter line: ")
    x = x + inp + '\n'
w.write(x)
w.close()

# File Reading:
f = open("Python/MPS_Practical/q6/flowers.txt", 'r')
r = f.readlines()
count = 0
for i in r:
    c = 0
    for j in i.split():
        if j=="lily":
            c+=1
    if c>=3:
        count+=1

print("No of lines:", count)
