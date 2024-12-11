# WAF to reverse a list of integers.
# Don't use reverse function

def revlist(list):
    rev = []
    for i in range(len(list)-1, -1, -1):
        rev.append(list[i])
    print(rev)