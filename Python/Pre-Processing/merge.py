import csv

row1 = []
row2 = []
header1 = []
header2 = []
pd1 = []
pd2 = []

with open("D:\VSC\Python\python\Python\Pre-Processing\data1.csv") as f:
    read = csv.reader(f)
    for i in read:
        row1.append(i)
    
with open("D:\VSC\Python\python\Python\Pre-Processing\data2.csv") as g:
    read = csv.reader(g)
    for i in read:
        row2.append(i)

header1 = row1[0]
pd1 = row1[1:]

header2 = row2[0]
pd2 = row2[1:]

header = header1 + header2
pd = []
for i in range(len(pd1)):
    pd.append(pd1[i]+pd2[i])

with open("final.csv", "w", newline="") as jake:
    write = csv.writer(jake)
    write.writerow(header)
    write.writerows(pd)