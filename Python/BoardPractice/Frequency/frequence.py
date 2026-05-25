# Take a txt file and find the most commonly occurring word, also list their frequencies.

f = open("new.txt", 'r')
dic = {}
x = f.read()
for i in x:
    if i in dic:
        dic[i] += 1
    elif i not in dic:
        dic[i] = 1
maxn = 0
maxw = ""
for k,v in dic.items():
    if v > maxn:
        maxn = v
        maxw = k

print(maxn, maxw)
print(dic)
