import pgzrun

WIDTH = 800
HEIGHT = 800
TTTLE = 'Catch the Butterfly'

butterfly = Actor('butterfly')
butterfly.pos = (150, 150)

def draw():
    screen.clear()
    screen.blit('background', (0, 0))
    butterfly.draw()



pgzrun.go()