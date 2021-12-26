input1 = input("Enter the first number : ")
input2 = input("Enter the second number : ")
inline3 = input("Enter the operator : ")

inline1 = int(input1)
inline2 = int(input2)

if inline3 == "+" :
    print(inline1 + inline2)
elif inline3 == "-" :
    print(inline1 - inline2)
elif inline3 == "*" :
    print(inline1 * inline2)
elif inline3 == "/" :
    print(inline1 / inline2)
elif inline3 == "%" :
    print(inline1 % inline2)
else :
    print("Enter either +, -, *, / or *")