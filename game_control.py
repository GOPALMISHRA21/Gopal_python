import pgzrun

HEIGHT =500
WIDTH=800

p = Actor('ironman', (100,100))
e1=Actor('character_zombie_hurt',(200,200))
e2=Actor('chr1',(150,350))
e3=Actor('hr3',(500,400))

def draw():
    screen.fill('black')
    p.draw()
    e1.draw()
    e2.draw()
    e3.draw()

def update():
    print(p.pos,e1.pos)
    if keyboard.left:
        p.x -=5
        p.angle = 10
        sounds.back_001.play()
    elif keyboard.right:
        p.x +=5
        p.angle = -10
    elif keyboard.up:
        p.y-= 5
    elif keyboard.down:
        p.y +=5
    elif keyboard.SPACE:
        p.angle = 100
    else:
        p.angle = 0
    

# enemy control
    if p.x > e1.x:
        e1.x += 1
    if p.y > e1.y:
        e1.y += 1
    if p.x < e1.x:
        e1.x -= 1
    if p.y < e1.y:
        e1.y -= 1


    if p.x > e2.x:
        e2.x += 1
    if p.y > e2.y:
        e2.y += 1
    if p.x < e2.x:
        e2.x -= 1
    if p.y < e2.y:
        e2.y -= 1

    if p.x > e3.x:
        e3.x += 1
    if p.y > e3.y:
        e3.y += 1
    if p.x < e3.x:
        e3.x -= 1
    if p.y < e3.y:
        e3.y -= 1

    

pgzrun.go()