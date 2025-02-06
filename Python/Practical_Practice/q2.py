# Write a program with separate user defined functions to perform the following operations on a
# list containing 10 integers.
# i. A user defined function to traverse the content of the list and push the even numbers into a stack.
# ii. Pop and display the content of the stack.

x = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
stack = []

def pusheven(list):
    for i in list:
        if i % 2 == 0:
            stack.append(i)

def pop():
    global stack
    while len(stack)>0:
        print(stack[-1])
        stack = stack[:len(stack)-1]
    else:
        print("Underflow")

pusheven(x)
pop()