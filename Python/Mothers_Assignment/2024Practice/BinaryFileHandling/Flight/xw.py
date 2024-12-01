# [Fno, FName, Fare, Source, Destination]

import pickle

with open("Python/Mothers_Assignment/2024Practice/BinaryFileHandling/Flight/flight.dat", 'wb') as f:
    n = int(input("no. "))
    for i in range(n):
        ni = input("no name fare src dest: ").split()
        nx = [int(ni[0]), ni[1], int(ni[2]), ni[3], ni[4]]
        pickle.dump(nx, f)
