# Write a function dispBook(BOOKS) in Python, that takes a dictionary
# BOOKS as an argument and displays the names in uppercase of those
# books whose name starts with a consonant.
# For example, Consider the following dictionary
# BOOKS = {1:"Python", 2:"Internet Fundamentals ", 3:"Networking ",
# 4:"Oracle sets", 5:"Understanding HTML"}
# 
# The output should be:
# PYTHON
# NETWORKING

def dispBook(BOOKS):
    for i in BOOKS:
        if BOOKS[i][0] not in "AEIOUaeiou":
            print(BOOKS[i].upper())

books = {1:"Python", 2:"Internet Fundamentals ", 3:"Networking ", 4:"Oracle sets", 5:"Understanding HTML"}
dispBook(books)

# Works √