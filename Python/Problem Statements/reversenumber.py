#WAP to reverse a given number, for example 123 = 321

a = 123
b = 0

while(a>0):
    r = a%10
    b+=r
    b*=10
    a = round(a/10)

b//=10

print(b)