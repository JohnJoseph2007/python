#Three steps to check if it is a leap year:
#   Step 1: If the year is perfectly divisible by 4 (no remainder)
#   Step 2: If the year is perfectly divisible by 4 but not by 100 it is a leap year
#   Step 3: If the year is divisible by 100 and by 400 it is a leap year

year = int(input("Enter year: "))

if year%4==0:
    if year%100==0:
        if year%400==0:
            print("It is a leap year")
        else:
            print("It is not a leap year")
    else:
        print("It is a leap year")
else:
    print("It is not a leap year")