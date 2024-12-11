import pickle

w = open("Python/MPS_Practical/q10/directory.dat", 'wb')
n = int(input("Enter no. of records to enter: "))
for i in range(n):
    name = input("Enter customer name: ")
    add = input("Enter address: ")
    mobno = input("Enter mobile number: ")
    pickle.dump({"customername":name, "address":add, "mobno":mobno}, w)
w.close()

f = open("Python/MPS_Practical/q10/directory.dat", 'rb')
try:
    while True:
        telephone=pickle.load(f)
        if telephone['mobno'][0]=='8':
            print(telephone)
except EOFError:
    f.close()