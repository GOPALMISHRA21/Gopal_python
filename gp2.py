from turtle import *
bgcolor('black')
colors=['red','blue', 'pink','yellow','purple']
speed('fastest')
x=0
for x in range(360):
    pencolor(colors[x % 5])
    width(x/100 + 1)
    forward(x)
    left(59)
mainloop()
