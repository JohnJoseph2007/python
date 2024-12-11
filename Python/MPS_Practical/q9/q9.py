import pickle

w = open("Python/MPS_Practical/q9/cinema.dat", 'wb')
n = int(input("Enter no. of records to enter: "))
for i in range(n):
    dor = input("Enter date of release: ")
    name = input("Enter movie name: ")
    typ = input("Enter movie type: ")
    pickle.dump([dor, name, typ], w)
w.close()

f = open("Python/MPS_Practical/q9/cinema.dat", 'rb')
try:
    while True:
        x=pickle.load(f)
        if x[2].lower() == "comedy":
            print(x)
except EOFError:
    f.close()
