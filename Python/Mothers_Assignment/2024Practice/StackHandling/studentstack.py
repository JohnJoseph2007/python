# Given a Dictionary Stu_dict containing marks of students for three
# test-series in the form Stu_ID:(TS1, TS2, TS3) as key-value pairs.
# Write a Python program with the following user-defined functions to
# perform the specified operations on a stack named Stu_Stk

# (i) Push_elements(Stu_Stk, Stu_dict) : It allows pushing IDs of those 
# students, from the dictionary Stu_dict into the stack Stu_Stk, who 
# have scored more than or equal to 80 marks in the TS3 Test.
# (ii) Pop_elements(Stu_Stk): It removes all elements present inside the 
# stack in LIFO order and prints them. Also, the function displays 
# 'Stack Empty' when there are no elements in the stack.

# Call both functions to execute queries.

def checkEmpty():
    if stu_stk==[]:
        return True
    else:
        return False
    
def Push_elements(Stu_Stk, Stu_dict):
    for i in Stu_dict:
        if Stu_dict[i][2] >= 80:
            stu_stk.append(i)
    print(stu_stk)

def Pop_elements(Stu_Stk):
    for i in range(len(stu_stk)):
        if checkEmpty==True:
            print("Stack Empty")
        else:
            u = stu_stk.pop()
            print(u)


# MAIN #

Stu_dic = {5:(87,68,89), 10:(57,54,61), 12:(71,67,90), 14:(66,81,80), 18:(80,48,91)}
top = None
stu_stk = []


Push_elements(stu_stk, Stu_dic)
Pop_elements(stu_stk)


# Works √