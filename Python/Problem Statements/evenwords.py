sentence = input("Enter a sentence: ")

def wordsplit(s):
    a = s.split(" ")
    for i in a:
        if len(i)%2==0:
            print(f"{i} has even number of letters")
        else:
            print(f"{i} has odd number of letters")

wordsplit(sentence)