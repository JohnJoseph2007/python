inp = input("Enter string")
stack = []

def Push(st):
    for i in st:
        if i.isupper():
            stack.append(i)

def Pop():
    global stack
    while len(stack)>0:
        print(stack[-1])
        stack = stack[:len(stack)-1]
    else:
        print("Underflow")

Push(inp)
Pop()