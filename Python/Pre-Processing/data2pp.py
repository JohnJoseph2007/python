import csv

data = []

with open("D:\VSC\Python\python\Python\Pre-Processing\data2.csv") as f:
    read = csv.reader(f)
    for i in read:
        data.append(i)

headers = data[0]
planetData = data[1:]

for i in planetData:
    i[2] = i[2].lower()

planetData.sort(key=lambda planetData:planetData[2])

with open("sortedData2.csv", "w", newline="") as g:
    write = csv.writer(g)
    write.writerow(headers)
    write.writerows(planetData)

    