lib = {}
n = int(input("Enter no. of books: "))
for i in range(n):
    bno = int(input("Enter book no.: "))
    title = input("Enter title: ")
    price = float(input("Enter price: "))
    pub = input("Enter publisher: ")
    lib[bno] = {'title':title, 'price':price, 'publisher':pub}

pubsearch = input("Enter publisher you want to search for: ")

for i in lib:
    if lib[i]['publisher'] == pubsearch:
        print(lib[i]['title'])
        continue
    else:
        continue