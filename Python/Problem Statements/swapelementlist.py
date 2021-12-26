christmas = ["Secret Semta", "Lights", "Tree", "Food", "Props", "Stars"]

def swap(list):
    n = len(list)-1
    el1 = list[0]
    list[0] = list[n]
    list[n] = el1
    

swap(christmas)

print(christmas)
