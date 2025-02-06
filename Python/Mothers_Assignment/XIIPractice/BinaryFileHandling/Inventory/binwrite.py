import pickle

with open("Python/Mothers_Assignment/XIIPractice/BinaryFileHandling/inventory.dat", 'wb') as f:
    n = int(input("Enter no.: "))
    for i in range(n):
        ni = input("Enter pID, pName, qty, price").split()
        # (ProductID, ProductName, Quantity, Price)
        nx = (int(ni[0]), ni[1], int(ni[2]), int(ni[3]))
        pickle.dump(nx, f)