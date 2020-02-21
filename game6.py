from pico2d import *
import random

class Grass:
    def __init__(self):
        self.image = load_image('grass.png')
        self.x, self.y = 400, 30
    def draw(self):
        self.image.draw(self.x, self.y)

    def update(self):
        pass

class Boy:
    def __init__(self):
        self.x, self.y = 100, 90
        self.image = load_image('run_animation.png')
        self.frame = 0

    def draw(self):
        sx = self.frame * 100
        self.image.clip_draw(sx, 0, 100, 100, self.x, self.y)

    def update(self):
        self.frame = (self.frame + 1) % 8
        self.x += 1

def handle_events():
    global loop
    events = get_events()
    for e in events:
        if e.type == SDL_QUIT:
            loop = False # end the game loop 
        elif e.type == SDL_KEYDOWN:
            if e.key == SDLK_ESCAPE:
                loop = False

open_canvas()

g = Grass()
boys = [Boy() for i in range(11)]
x = 100
for b in boys:
    b.x = x
    x += 50

loop = True
while (loop):
    #b.update()
    for b in boys: 
        b.update()

    clear_canvas()

    g.draw()
    for b in boys:
        b.draw()

    update_canvas()
    handle_events()

    delay(0.03) 

close_canvas()







