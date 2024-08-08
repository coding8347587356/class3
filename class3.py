import pgzrun
from random import randint

WIDTH = 300
HEIGHT = 300

def draw():

    width = WIDTH
    height = HEIGHT-200

    for i in range(20):
        r = randint(0,255)
        g = randint(0,255)
        b = randint(0,255)
        
        rect = Rect((0,0), (width,height))
        screen.draw.rect(rect, (r,g,b))
   
        width -= 10
        height += 10

        


pgzrun.go()