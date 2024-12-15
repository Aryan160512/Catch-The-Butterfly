import pgzrun

WIDTH = 800
HEIGHT = 500
TITLE = 'Alien Shooter Game'

alien = Actor('alien')
alien.pos = (250, 250)

def draw():
    screen.clear()
    screen.blit('space', (0, 0))
    alien.draw()

pgzrun.go()