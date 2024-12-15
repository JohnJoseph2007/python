cities = {}
stack = []

n = int(input("No. of cities: "))
for i in range(n):
    city = input("city name: ")
    pop = int(input("population: "))
    cities[city]=pop

def pushit():
    for i in cities:
        if cities[i]>=1000:
            stack.append(i)

def popit():
    global stack
    while len(stack)>0:
        print(stack[-1])
        stack = stack[:len(stack)-1]
    else:
        print("Underflow")

pushit()
popit()