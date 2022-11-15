import pgzrun
import random


WIDTH=1200
HEIGHT=500

p=Actor('ironman',(50,50))   #player speed
p.speed = 5
e1=Actor('enemy',(250,250))
rx = random.randint(50,WIDTH-50)
ry = random.randint(50,HEIGHT-50)
c=Actor('cookie_img',(rx,ry))   #cookie
score = 0

def draw():
    if score<=2:
        screen.clear()
        p.draw()
        c.draw()
        e1.draw()
        screen.draw.text(f'Score: {score}',(WIDTH-120,10),fontsize=30)
        screen.draw.text('Gopal Mishra',(WIDTH-250,50),fontsize=40)
    else:
        screen.fill('green')
        screen.draw.text('You win',(WIDTH/2-100,HEIGHT/2-50),fontsize=50)

    if  p.x == e1.x and p.y == e1.y:
        screen.fill('blue')
        screen.draw.text('You loose',(WIDTH/2-100,HEIGHT/2-50),fontsize=50)
        sounds.r1.play()

def player_control():
    if keyboard.W:
        p.y -= p.speed
    elif keyboard.S:
        p.y += p.speed
    elif keyboard.A:
        p.x -= p.speed
        p.angle = 10
    elif keyboard.D:
        p.x += p.speed
        p.angle = -10
    else:
        p.angle=0
    
    if p.x > e1.x:
        e1.x += 1
    if p.y > e1.y:
        e1.y += 1
    if p.x < e1.x:
        e1.x -= 1
    if p.y < e1.y:
        e1.y -= 1
    
    

    # BOUNDRY MANAGE
    if p.x < 0:
        p.x = WIDTH
    if p.x > WIDTH:
        p.x=0
    
def handle_score():
    global score
    if p.colliderect(c):
        rx = random.randint(50,WIDTH-50)
        ry = random.randint(50,HEIGHT-50)
        c.pos = (rx,ry)
        score += 1
def update():
    player_control()
    handle_score()

pgzrun.go()