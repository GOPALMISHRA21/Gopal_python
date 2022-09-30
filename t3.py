from turtle import *

outside = 6
inside = 6
for i in range (outside):
    fd(100)
    for j in range(inside):
        fd(50)
        lt(360/outside)
    lt(360/outside)
mainloop()