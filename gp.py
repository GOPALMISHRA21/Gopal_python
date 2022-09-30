from turtle import *
speed('fastest')
pencolor('red')
bgcolor('black')
x=0
for i in range(50):
        fillcolor("yellow")
        begin_fill()
        pencolor("green")
        circle(5*i)
        circle(-5*i)
        lt(i)


mainloop()

