# WAF to take input a string and check whether
# the string is a palindrome or not.

def pal(string):
    string = string.lower()
    if string==string[::-1]:
        return True
    else:
        return False