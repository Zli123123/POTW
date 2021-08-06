a = int(input("number: "))
b = int(input("number2: "))
count = 0
count1 = 0
import math
for i in range(a, b+1):
                for j in range (0, i + 1):
                                if int(j*j*j*j*j*j) == i:
                                                count1 += 1
                                                print(i)
                                                print(j)
                                                count += 1        

    
        
        

print("count: ", count)