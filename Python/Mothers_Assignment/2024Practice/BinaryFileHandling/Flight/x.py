# Consider a file FLIGHT.DAT containing multiple records. The
# structure of each record is as shown below:
# [Fno, FName, Fare, Source, Destination]
# Write a function COPY_REC() in Python that copies all those
# records from FLIGHT.DAT where the source is DELHI and the
# destination is MUMBAI, into a new file RECORD.DAT

import pickle

x= []
with open("Python/Mothers_Assignment/2024Practice/BinaryFileHandling/Flight/flight.dat", "rb") as fr:
    try:
        while True:
            x.append(pickle.load(fr))
    except EOFError:
        writer = open("Python/Mothers_Assignment/2024Practice/BinaryFileHandling/Flight/record.dat", 'wb')
        for i in x:
            if i[3]=="BBI" and i[4]=="QAT":
                pickle.dump(i, writer)
        writer.close()
