import pickle
import os

w = open("Python/MPS_Practical/q8/bank.dat", 'wb')
for i in range(10):
    accno = int(input("Account no.: "))
    cname = input("Customer name: ")
    balance = float(input("Balance: "))
    pickle.dump([accno, cname, balance], w)
w.close()

# Deletion:

search = int(input("Enter account name to search: "))
f = open("Python/MPS_Practical/q8/bank.dat", 'rb')
fw = open("Python/MPS_Practical/q8/bank2.dat", 'wb')
try:
    while True:
        x=pickle.load(f)
        if x[0]!=search:
            pickle.dump(x, fw)
except EOFError:
    os.remove("Python/MPS_Practical/q8/bank.dat")
    os.rename("Python/MPS_Practical/q8/bank2.dat", "Python/MPS_Practical/q8/bank.dat")
f.close()
fw.close()
        