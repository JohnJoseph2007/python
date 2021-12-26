def swapFileData():
    source=input("Enter Source Filename with proper paths: ")
    dest=input("Enter Destination Filename with proper paths: ")

    with open(source, 'r') as a:
        a_data = a.read()
    
    with open(dest, 'r') as b:
        b_data = b.read()
    
    with open(source, 'w') as wa:
        wa.write(b_data)
    
    with open(dest, 'w') as wb:
        wb.write(a_data)

swapFileData()