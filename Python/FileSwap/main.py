def swap():
    inp1 = input("Source filename: ")
    inp2 = input("Destination filename: ")

    with open(inp1, "r") as a:
        a_data = a.read()
    
    with open(inp2, "r") as b:
        b_data = b.read()

    with open(inp2, "w") as w:
        w.write(a_data)

    with open(inp1, "w") as w:
        w.write(b_data)

swap()