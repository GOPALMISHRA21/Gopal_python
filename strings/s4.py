a = "gopal is a very good boy"
print(len(a))
for i,v in enumerate(a):
    print(f'{i}-------->>{v}')


from turtle import *

pensize(1)
bgcolor('black')
fillcolor("yellow")
speed('fastest')
begin_fill()
for i in range(100):
    pencolor('blue')
    lt(100)
    fd((360/5))
    for j in range(i):
        circle(50)
        pencolor("red")
    end_fill()
pencolor("red")
mainloop()
    