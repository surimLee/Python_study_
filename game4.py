from pico2d import *
import random

open_canvas()
ch = load_image('run_animation.png')
gr = load_image('grass.png')
# gr.draw_now(400, 30)

def handle_events():
    global loop
    global x, y, dx
    events = get_events()
    for e in events:
        if e.type == SDL_QUIT:
            loop = False # end the game loop 
        elif e.type == SDL_KEYDOWN:
            if e.key == SDLK_ESCAPE:
                loop = False
            elif e.key == SDLK_LEFT:
                dx -= 1
            elif e.key == SDLK_RIGHT:
                dx += 1
        elif e.type == SDL_KEYUP:
            if e.key == SDLK_LEFT:
                dx += 1
            elif e.key == SDLK_RIGHT:
                dx -= 1
        elif e.type == SDL_MOUSEMOTION:
            x = e.x
            y = get_canvas_height() - e.y


x = 400
y = 300
dx = 0
frame = 0
loop = True
while (loop):
    clear_canvas()
    gr.draw(400, 30)
    ch.clip_draw(frame * 100, 0, 100, 100, x, y)
    update_canvas()

    x += dx
    # x = x + 2
    # if x >= 800:
    #     loop = False

    frame += 1
    if frame >= 8:
        frame = 0

    handle_events()

    delay(0.03) 

close_canvas()







