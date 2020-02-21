from pico2d import *
import random

open_canvas()
ch = load_image('run_animation.png')
gr = load_image('grass.png')
# gr.draw_now(400, 30)

def handle_events():
    global loop
    global x, y, dx, dy, tx, ty
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
        # elif e.type == SDL_MOUSEMOTION:
        #     x = e.x
        #     y = get_canvas_height() - e.y
        elif e.type == SDL_MOUSEBUTTONDOWN:
            tx = e.x
            ty = get_canvas_height() - e.y
            dx = (tx - x) / 10
            dy = (ty - y) / 10
        # elif e.type == SDL_MOUSEBUTTONUP:
        #     dx, dy = 0, 0


x = 400
y = 300
tx, ty = x, y
dx = 0
dy = 0
frame = 0
loop = True
while (loop):
    clear_canvas()
    gr.draw(400, 30)
    ch.clip_draw(frame * 100, 0, 100, 100, x, y)
    update_canvas()

    if dx > 0:
        if x + dx > tx:
            x = tx
            dx = 0
        else:
            x += dx
    else:
        if x + dx < tx:
            x = tx
            dx = 0
        else:
            x += dx
    if dy > 0:
        if y + dy > ty:
            y = ty
            dy = 0
        else:
            y += dy
    else:
        if y + dy < ty:
            y = ty
            dy = 0
        else:
            y += dy

    # x = x + 2
    # if x >= 800:
    #     loop = False

    frame += 1
    if frame >= 8:
        frame = 0

    handle_events()

    delay(0.03) 

close_canvas()







