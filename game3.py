from pico2d import *
import random

open_canvas()
ch = load_image('run_animation.png')
gr = load_image('grass.png')
# gr.draw_now(400, 30)

def handle_events():
    global loop
    events = get_events()
    for e in events:
        if e.type == SDL_QUIT:
            loop = False # end the game loop 
        if e.type == SDL_KEYDOWN and e.key == SDLK_ESCAPE:
            loop = False


x = 0
frame = 0
loop = True
while (loop):
    clear_canvas()
    gr.draw(400, 30)
    ch.clip_draw(frame * 100, 0, 100, 100, x, 90)
    update_canvas()
    x = x + 2
    if x >= 800:
        loop = False

    frame += 1
    if frame >= 8:
        frame = 0

    handle_events()

    delay(0.03) 

close_canvas()







