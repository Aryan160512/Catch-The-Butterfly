import pgzrun

WIDTH = 900
HEIGHT = 800

def createRect(x, y, w, h, c):
    rect = Rect((x, y), (w, h))
    screen.draw.rect(rect, c)

def createCircle(x, y, r, c):
    screen.draw.circle((x, y), r, c)

def draw():
    screen.clear()
    
    createRect(100, 100, 150, 75, "blue")
    createCircle(250, 137, 37, "red")  
    createRect(287, 200, 150, 75, "green")
    createCircle(437, 237, 37, "yellow") 
    createRect(474, 300, 150, 75, "purple")
    createCircle(624, 337, 37, "orange")  
    createRect(661, 400, 150, 75, "cyan")
    createCircle(811, 437, 37, "lime") 

    createRect(50, 200, 150, 75, "blue")
    createCircle(200, 237, 37, "red")  
    createRect(237, 300, 150, 75, "green")
    createCircle(387, 337, 37, "yellow") 
    createRect(424, 400, 150, 75, "purple")
    createCircle(574, 437, 37, "orange")  
    createRect(611, 500, 150, 75, "cyan")
    createCircle(761, 537, 37, "lime") 


pgzrun.go()
