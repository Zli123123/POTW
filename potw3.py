#potw3 grind - hopefully it's not that bad\
import random #yes, but how to make each number unique
import time
random.seed(time.time())
yesorno = 1
yaxis = int(input("number: "))
xaxis = int(input("number: "))
maze = []
listwhole = []
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
    print("The factors of",x,"are:")
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
kkk = 1
if yesorno == 2:
    for i in range (yaxis):
        maze.append([])
        for k in range (xaxis):
            integer = colors[kkk]
            kkk+=1
            print(integer, end = " ")
            listwhole.append(integer)
        print ("\r")
    print (listwhole)
if yesorno == 1:
    for i in range (yaxis):
        maze.append([])
        for k in range (xaxis):
            integer = random.randint(1, 20)
            print(integer, end = " ")
            listwhole.append(integer)
        print ("\r")
    print (listwhole)    
#l is the point where we are at (so at the start l would be the integer at 1,1)

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
print(lastpoint, "\\**")
pointrn = listwhole[0]
print (pointrn, "\\**")
print_factors(pointrn)


finalcount = 0
for somethingthatsnoti in (0, len(listwhole)):
    lastpoint = (yaxis * xaxis)
    for i in range (0, len(listwhole)):
        if listwhole[i] == lastpoint:
            lastpoint = listx[i] * listy[i]
            print("newlastpoint:", lastpoint, "//", listx[i], ",", listy[i], "//", listwhole[i])
            if listx[i] * listy[i] == pointrn:
                finalcount += 1

if finalcount >= 1:
    print("maze is solvable/escapable: damn this took a long time")
else:
    print("no, impossible to escape")