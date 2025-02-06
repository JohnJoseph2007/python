# Consider a binary file 'INVENTORY.DAT' that stores information
# about products using tuple with the structure (ProductID,
# ProductName, Quantity, Price). Write a Python function
# expensiveProducts() to read the contents of
# 'INVENTORY.DAT' and display details of products with a price
# higher than Rs. 1000. Additionally, calculate and display the total
# count of such expensive products.

import pickle

with open("Python/Mothers_Assignment/XIIPractice/BinaryFileHandling/inventory.dat", 'rb') as f:
    try:
        c = 0
        while True:
            x = pickle.load(f)
            if x[3]>1000:
                print(x)
                c+=1
    except EOFError:
        pass
    finally:
        print("Count:", c)

# Works √