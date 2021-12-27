#"Spiderman No Way Home is so good"
sentence = input("Enter a sentence: \n")
increment=0
spacing=1
for letter in sentence:
    increment+=1
    if letter == " ":
        spacing+=1
print("Number of letters is {}" .format(increment))
print("Number of words is {}" .format(spacing))

# words = sentence.split(" ")
# print("Words are: {}" .format(words))
# print("Number of words is {}" .format(len(words)))