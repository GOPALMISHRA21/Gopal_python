from turtle import *


#pentagon
side = 5
for i in range(side):
    pencolor('red')
    pensize(1)
    fd(-100)
    lt(360/5)
    fillcolor('yellow')
    begin_fill()
    dot(side*3)
    pensize(2)
    pencolor('blue')
    circle(side*8)
    end_fill()
mainloop()