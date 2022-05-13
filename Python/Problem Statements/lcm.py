# Find LCM of two numbers with the help of a function

def lcm(a, b):
    lower, higher = 0, 0
    if a>b:
        lower = b
        higher = a
    else:
        lower = a
        higher = b
    upperlimit = lower*higher
    for i in range(higher, upperlimit+1):
        if i%higher == 0 and i%lower == 0:
            lcm = i
    return lcm

in1 = int(input("Enter first number: "))
in2 = int(input("Enter second number: "))

lcm(in1, in2)