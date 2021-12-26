import random

randomNumber = random.randint(1, 9)
lives = 5
answer = "wrong"

while lives>0 and answer=="wrong":
    guess = int(input("Enter your guess between 1 and 9 here: "))
    if guess == randomNumber:
        print("You guessed correctly! Good job.")
        print("------------------------------")
        answer="right"
    elif guess > randomNumber:
        print("You guessed too high. Try a lower number")
        lives=lives-1
        print("Lives left: {}".format(lives))
        print("------------------------------")
    elif guess < randomNumber:
        print("You guessed too low. Try higher")
        lives=lives-1
        print("Lives left: {}".format(lives))
        print("------------------------------")

print("Thank you for playing, hope you enjoyed.")
print("Goodbye")
print("------------------------------")