# MEAN:
listinput = list(map(int, input().split()))
sum = 0
for i in listinput:
    sum+=i
mean = sum/len(listinput)
print(mean)

# MEDIAN:
listinput.sort()
n = len(listinput)
if n%2==0:
    m1 = listinput[n//2]
    # double forward slash (//) returns an integer (rounded off) number
    m2 = listinput[(n//2)-1]
    float(m1)
    float(m2)
    median = (m1+m2)/2
else:
    median = listinput[n//2]
print(median)