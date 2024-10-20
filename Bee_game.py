import pgzrun
import random
WIDTH = 800
HEIGHT = 600
score = 0

gameover = False


bee = Actor("bee image")
bee.pos = (400,300)
flower = Actor("flower")
flower.pos = (200,100)



def draw():
    
    if gameover == False:
        screen.blit("grass image",( 0,0))
        bee.draw()
        flower.draw()
        screen.draw.text(str(score),(65,50),color='dark blue')
    else:
        screen.fill("red")
        screen.draw.text("GAMEOVER",(400,300),color='dark blue')

def update(): 
    
    if keyboard.left:
        bee.x = bee.x - 5
    if keyboard.right:
        bee.x = bee.x + 5
    if keyboard.up:
        bee.y = bee.y - 5
    if keyboard.down:
        bee.y = bee.y + 5

    if bee.colliderect(flower):
        flower.pos = (random.randint(50,750),random.randint(50,550))
        global score
        score = score+10

def end():
    global gameover
    gameover = True

clock.schedule(end,20)

pgzrun.go()

