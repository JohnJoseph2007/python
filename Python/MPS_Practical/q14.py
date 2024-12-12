stack = []

def pushit():
    n = int(input("Enter no. of entries: "))
    for i in range(n):
        city = input("Enter city name: ")
        pop = int(input("Enter population"))
        if pop>=1000:
            stack.append(city)

def popit():
    global stack
    while len(stack)>0:
        print(stack[-1])
        stack = stack[:len(stack)-1]
    else:
        print("Underflow")

pushit()
popit()