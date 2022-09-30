from turtle import *
i = 1
speed('fastest')
pencolor('blue')
pensize(1)
bgcolor('black')
while True:
    fd(10 + i)
    for j in range(6):
        fd(20)
        lt(360/8)
    
    left(360//8)
    i += 5
    write(i)
    if i >500:
        break
mainloop()