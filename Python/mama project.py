import random

def lottery() :
    num = int(input("Enter the number of total patients in the list : "))
    pat_list = []
    r = int(input("Enter the number of patients you want to randomly pick : "))
    for i in range(0, num) :
        patients = input("Enter the serial numbers of the patients : ")
        pat_list.append(patients)

    pick = random.sample(pat_list, r)
    picked_list = [pick]
    print("Random patients are : ")
    for x in range(len(picked_list)) :
        print (picked_list[x])

lottery()
