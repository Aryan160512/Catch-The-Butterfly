import pgzrun
import random

WIDTH = 800
HEIGHT = 450
TITLE = 'Catch the Butterfly Game'

score = 0

butterfly = Actor('butterfly')
butterfly.pos = (400, 225)

def moveButterfly():
    butterfly.pos = (random.randint(50, 750), random.randint(50, 200))

def on_mouse_down(pos):
    global score
    if butterfly.collidepoint(pos):
        moveButterfly()
        score = score + 1

def draw():
    screen.clear()
    screen.blit('background', (0, 0))
    butterfly.draw()
    screen.draw.text('Score: ' + str(score), (50, 50))



pgzrun.go()