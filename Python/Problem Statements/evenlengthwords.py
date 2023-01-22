#WAP to print all the even length words in a sentence

inp = input("Enter sentence: ").strip().split()

even = []
for i in inp:
    if(len(i)%2==0):
        even.append(i)

print(even)
