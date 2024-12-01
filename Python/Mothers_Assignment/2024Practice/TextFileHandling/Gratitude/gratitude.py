# Write a function COUNT() in Python to read from a text file
# 'Gratitude.txt' and display the count of the letter 'e' in each
# line

def COUNT():
    with open('Python/Mothers_Assignment/2024Practice/TextFileHandling/gratitude.txt', 'r') as f:
        x = f.readlines()
        ln = 0
        for i in x:
            ln +=1
            c=0
            for j in i:
                if j=='e' or j=='E':
                    c+=1
            print("Line {}: {}".format(ln, c))

COUNT()