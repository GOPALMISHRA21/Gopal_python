from turtle import *
t = Turtle()
t1=Turtle()
side=5
speed('fastest')
t.fillcolor('yellow')
t.begin_fill()

for i in range(side):
   
    t.pencolor('green')
    t.pensize(5)
    t.fd(-150)
    t.lt(360/5)

    t1.fd(-150)
    t1.lt(360/5)
    t1.pencolor('blue')
    t1.fillcolor('blue')
    t1.begin_fill()
    t1.circle(50)
    t1.end_fill()
t.end_fill()
mainloop()



