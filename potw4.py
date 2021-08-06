#potw4
#N = restaurants, M = Pho Restaurants, N-1 roads
N = 7
M = 5
import random    
import time
random.seed(time.time())
resnums = []
for i in range (0, M):
    integer = random.randint(1, N)
    resnums.append(integer)

print(resnums)
list1 = []
list2 = []
if N % 2 == 0:
    print ("even")
else:
    print("odd")
    split = (N - 1) / 2
    mid = N - split
    for i in range(1, split+1):
        list1.append(i)
    for i in range(mid+1, (mid+split+1)):
        list2.append(i)
    print(list1, list2)
        
for i in range(1, N):
    point = i
    road[i] = i 