from pico2d import *
import random

open_canvas()
ch = load_image('run_animation.png')
gr = load_image('grass.png')
# gr.draw_now(400, 30)

x = 0
frame = 0
while (x < 800):
    clear_canvas()
    gr.draw(400, 30)
    ch.clip_draw(frame * 100, 0, 100, 100, x, 90)
    update_canvas()
    x = x + 2
    frame += 1
    if frame >= 8:
        frame = 0
    delay(0.03) 

clear_canvas_now()

delay(5)

close_canvas()







