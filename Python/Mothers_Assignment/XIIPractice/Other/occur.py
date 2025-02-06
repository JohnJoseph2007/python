# Write a Python Program containing a function FindWord(STRING,
# SEARCH), that accepts two arguments : STRING and SEARCH, and
# prints the count of occurrence of SEARCH in STRING. Write
# appropriate statements to call the function.
# For example, if :
# STRING = "Learning history helps to know about history with interest in history"
# SEARCH = 'history'
# the function should display
# "The word history occurs 3 times."

def FindWord(STRING, SEARCH):
    l = STRING.split()
    c = 0
    for i in l:
        if i==SEARCH:
            c+=1
    print("The word {} appears {} times".format(SEARCH, c))

STRING = "Learning history helps to know about history with interest in history"
SEARCH = 'history'

FindWord(STRING, SEARCH)

# Works √