from pico2d import *
import random

open_canvas()
ch = load_image('character.png')
gr = load_image('grass.png')
gr.draw_now(400, 30)

x = 0
while (x < 800):
    clear_canvas()
    gr.draw(400, 30)
    ch.draw(x, 90)
    update_canvas()
    x = x + 2
    delay(0.1) 

clear_canvas_now()

delay(5)

close_canvas()







