import random

def initiation() :
    print("Which calculator are you using? \n 1. Arithmetic \n 2. Simple Interest \n 3. Percentage Calculator \n 4. Random Number Picker")
    calcpick = input("1/2/3/4 : ")

    if calcpick == "1" :
        arithmetic()
    elif calcpick == "2" :
        si()
    elif calcpick == "3" :
        percentage()
    elif calcpick == "4" :
        rng()
    else :
        print("Enter 1, 2, 3 or 4")
        initiation()

    res()


def arithmetic() :
    anum1 = int(input("Enter the first number : "))
    aop = input("Enter the operator : ")
    anum2 = int(input("Enter the second number : "))

    art = 0

    if aop == "+" :
        art = anum1 + anum2
    elif aop == "-" :
        art = anum1 - anum2
    elif aop == "*" :
        art = anum1 * anum2
    elif aop == "/" :
        art = anum1 / anum2
    elif aop == "%" :
        art = anum1 % anum2
    else :
        print("Enter either +, -, *, / or *")
        arithmetic()

    print(str(art))

    res()


def si() :
    p = int(input("Enter Principal : "))
    t = int(input("Enter Time (in years) : "))
    r = int(input("Enter Rate (without the % sign) : "))
    s = (p*t*r)/100
    a = p + s

    print("Simple Interest = " + str(s))
    print("Amount = " + str(a))

    res()


def percentage() :
    num = int(input("Enter the numerator : "))
    den = int(input("Enter the denominator : "))
    p = (num/den)*100

    print("Percentage = " + str(p) + "%")

    res()


def rng() :
    nums = []
    rnum = int(input("Enter number of numbers you want to randomize : "))
    for i in range (0, rnum) :
        inputs = int(input("Enter the numbers, pressing enter after each one : "))
        nums.append(inputs)

    outputs = random.choice(nums)
    print("Original list is : " + str(nums))
    print("Random number is : " + str(outputs))

    res()

def res() :
    
    restart = input("Hit 'r' to restart and 'e' to exit : ")

    if restart == "r" :
        initiation()
    elif restart == "e" :
        exit
    else :
        print("Enter either 'r' or 'e'")
        res()

initiation()
