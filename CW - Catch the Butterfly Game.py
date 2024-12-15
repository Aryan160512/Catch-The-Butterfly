import pgzrun

WIDTH = 800
HEIGHT = 450
TITLE = 'Catch the Butterfly Game'

butterfly = Actor('butterfly')
butterfly.pos = (400, 225)

def draw():
    screen.clear()
    screen.blit('background', (0, 0))
    butterfly.draw()



pgzrun.go()