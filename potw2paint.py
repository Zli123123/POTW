import time
import random



num = int(input("number: "))
x = []
y = []
i = 0
while i < num:
        numx = int(input("number: "))
        x.append(numx)
        numy = int(input("number: "))
        y.append(numy)
        i += 1
    
x.sort(reverse = True) #lol, ima not waste  my time doing sort
print(x)
y.sort (reverse = True)
print(y)
downx = x[-1] 
downx -= 1
downy = y[-1]
downy -= 1
upx = x[0] 
upx += 1
upy = y[0] 
upy += 1    

if __name__ == "__main__" :
        import turtle
        screen = turtle.Screen()  
        screen.colormode(255)        
        t = turtle.Turtle()
        t.penup()
        t.goto(downx, downy)
        t.pendown()
        t.goto(downx, upy)
        t.goto(upx, upy)
        t.goto(upx, downy)
        t.goto(downx, downy)
        for i in range (0, len(x)):
                r = random.randint(0, 255)
                g = random.randint(0, 255)
                b = random.randint(0, 255)
                t.pencolor(r, g, b)
                t.penup()
                t.goto(x[i], y[i])
                t.pendown()
                t.circle(1)
                random.seed(time.time())
                if i == num:
                        time.sleep(10)
                        turtle.bye()        


