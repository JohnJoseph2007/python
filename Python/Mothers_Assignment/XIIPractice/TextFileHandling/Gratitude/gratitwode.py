# Write a function Start_with_I() in Python, which should read a
# text file 'Gratitude.txt' and then display lines starting with 'I'.

def Start_with_I():
    with open("Python/Mothers_Assignment/XIIPractice/TextFileHandling/gratitude.txt") as f:
        x = f.readlines()
        for i in x:
            if i[0] == "I":
                print(i)

Start_with_I()

# Works √