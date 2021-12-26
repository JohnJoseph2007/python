import time, os, shutil

path = input("Enter Path: ")
days = float(input("Enter the number of days before which the files will be deleted: "))
seconds = int(days*24*60*60)
listelem = []
listtime = []
dest="D:\CutItems"

if os.path.exists(path):
    contents = os.listdir(path)
    for i in contents:
        sinelem = os.path.join(path, i)
        listelem.append(sinelem)
        sorted(listelem)
    for i in listelem:
        ctime = int(os.stat(i).st_ctime)
        listtime.append(ctime)
    print(listelem)
    print(listtime)
    print(seconds)
    # for i in range(len(listtime)-1):
    #     if listtime[i] < seconds:
    #         shutil.move(listelem[i], dest)
    #         print("File moved")
    #     else:
    #         print("File not moved")
    
else:
    print("Path does not exist")