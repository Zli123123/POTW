import random
import time
random.seed(time.time())
yesorno = 1
yaxis = int(input("number: "))
xaxis = int(input("number: "))
listwhole = []
maze = []
if yesorno == 1:
    for i in range (yaxis):
        maze.append([])
        for k in range (xaxis):
            integer = random.randint(1, 30)
            print(integer, end = " ")
            listwhole.append(integer)
        print ("\r")
    print (listwhole)  

pointrn = listwhole[0]
print(pointrn)