from pico2d import *

fonts = {}
def load(file, size):
    global fonts
    key = '%s_%d' % (file, size)
    if key in fonts:
        print("Found:", key)
        return fonts[key]

    print("Loading:", key)
    font = load_font(file, size)
    fonts[key] = font

    return font
