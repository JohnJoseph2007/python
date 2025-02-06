#Write a program with two user defined functions considering them to act as PUSH and POP
# operations of the data structure stack.
# I. Addnew(Book) - To add a new book to a list of Books
# II. Remove(Book) – To remove a book from a list of Books.

stack = ["AM", "GOT"]

def addnew(book):
    stack.append(book)
    print("Book added successfully")
    print(stack)

def remove(book):
    if book in stack:
        stack.remove(book)
        print("Book removed successfully")
        print(stack)
    else:
        print("Book not found")

addnew(input())
remove(input())