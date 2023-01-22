nocom = int(input("Number of Commands = "))

list = []

for i in range(nocom):
    inp = input("Command = ").split()
    if inp[0]=="print":
        print(list)
    if inp[0]=="insert":
        list.insert(int(inp[1]), int(inp[2]))
    if inp[0]=="remove":
        list.remove(int(inp[1]))
    if inp[0]=="append":
        list.append(int(inp[1]))
    if inp[0]=="sort":
        list.sort()
    if inp[0]=="pop":
        list.pop()
    if inp[0]=="reverse":
        list.reverse()
    
