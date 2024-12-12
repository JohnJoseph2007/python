dict = {}
for i in range(6):
    name = input("Enter name: ")
    marks = int(input("Marks: "))
    dict[name] = marks

stack = []

def Push():
    for i in dict:
        if dict[i]>75:
            stack.append(i)

def Pop():
    global stack
    while len(stack)>0:
        print(stack[-1])
        stack = stack[:len(stack)-1]
    else:
        print("Underflow")

Push()
Pop()