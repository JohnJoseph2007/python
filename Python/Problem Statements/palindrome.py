inputstring = input("Enter a word: ")
def palindrome(parameter):
    if parameter == parameter[::-1]:
        print("It is a palindrome")
    else:
        print("It isn't a palindrome")

palindrome(inputstring)