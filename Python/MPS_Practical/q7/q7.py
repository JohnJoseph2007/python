def newfile():
    n = int(input("Enter no. of lines: "))
    w = open("Python/MPS_Practical/q7/online.txt", 'w')
    ws = ''
    for i in range(n):
        inp = input("Enter line: ")
        ws = ws + inp + '\n'
    w.write(ws)
    w.close()

def count_t_word():
    f = open("Python/MPS_Practical/q7/online.txt", 'r')
    x = f.readlines()
    c = 0
    for i in x:
        for j in i.split():
            if j[0].lower()=='t' and len(j)==5:
                c+=1
    print("No. of eligible words:", c)