import sys

def sort(array):
    sortedarray = sorted(array)
    print("Sorted array : ")
    print(sortedarray)
    branch(sortedarray)

def arrayinput():
    arraylength=int(input("Enter number of items in the list of numbers: "))
    arrayofnumbers=[]
    while len(arrayofnumbers)<arraylength:
        num=int(input("Enter the numbers: "))
        arrayofnumbers.append(num)
    sort(arrayofnumbers)

def branch(array):
    pref=input("To add the list, press +; To subtract the list, press -; To multiply the list, press *; To divide the list, press /")
    if pref=="+":
        add(array)
    elif pref=="-":
        sub(array)
    elif pref=="*":
        multiply(array)
    elif pref=="/":
        divide(array)
    else:
        print("Enter either '+', '-', '*' or '/'")

def add(array):
    starter = 0
    for x in array:
        starter = starter + x
    print("Added the array: "+str(starter))
    end()

def sub(array):
    starter = 0
    for x in array:
        starter = starter - x
    print("Subtracted from 0, result is: "+str(starter))
    end()

def multiply(array):
    starter = 1
    for x in array:
        starter = starter * x
    print("Multiplied the array: "+str(starter))
    end()

def divide(array):
    starter=1
    for x in array:
        starter = starter/x
    print("Starting with 1, division result is: "+str(starter))
    end()

def end():
    print("Run again or End?")
    a = input("Run again [Y] \nEnd [N]")
    if a=="Y" or a=="y":
        arrayinput()
    elif a=="N" or a=="n":
        sys.exit()

arrayinput()