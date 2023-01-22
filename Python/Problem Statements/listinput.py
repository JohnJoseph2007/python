inputtaken = list(map(int, input("enter :)").strip().split(",")))

inputtaken.sort(reverse=True)


print(inputtaken[1])