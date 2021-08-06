
import random 
import time
random.seed(time.time())
yaxis = 3
xaxis = 4
#yaxis = int(input(""))
#xaxis = int(input(""))
print("3")
print("4")
print("12 10 8 14")
print("1 11 12 12")
print("6 2 3 9")
maze = []
listwhole = [12, 10, 8, 14, 1, 11, 12, 12, 6, 2, 3, 9]
listx = []
listy = []

l = xaxis * yaxis
colors = []

for i in range (l+1) :
    
    uniqueFlag = False
    while not uniqueFlag :
        
        uniqueFlag = True
        x = random.randint(1, l+1)
        
        for j in range(i) :
            if colors[j] == x :
                uniqueFlag = False
                break
            
        if uniqueFlag :      
            colors.append(x)

def print_factors(x):
    factors = []
    factors1 = []
    tick = 0
    tick1 = 0
    for i in range(1, x + 1):
        if x % i == 0:
            tick += 1
    for i in range(1, x + 1):
        if x % i == 0:   
            tick1 += 1
            if i * i == x:
                factors.append(i)
                factors1.append(i)
            elif tick1 <= tick/2 and i*i != x:
                factors.append(i)
            else:
                factors1.append(i)
    factors.sort(reverse = True) 
    print(factors)
    print(factors1)


d = 0
count = 0
count1 = 1
while d < (yaxis * xaxis):
    d += 1
    if count == xaxis:
        count = 0
        count1 += 1
    count += 1
    listy.append(count1)
    listx.append(count)
print(listx)
print(listy)

lastpoint = (yaxis * xaxis)
pointrn = listwhole[0]
print_factors(pointrn)

finalcount = 0
for somethingthatsnoti in range(100):
    lastpoint = (yaxis * xaxis)
    print(lastpoint)
    for i in range (0, len(listwhole)):
        if listwhole[i] == lastpoint:
            lastpoint = listx[i] * listy[i]
            print("newlastpoint:", lastpoint, "//", listx[i], ",", listy[i], "//", listwhole[i])
            if listx[i] * listy[i] == pointrn:
                finalcount += 1



if finalcount >= 1:
    print("yes")
else:
    print("no")