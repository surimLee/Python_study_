# import pico2d
import random
from pico2d import *
import game_framework

font = None
score = 0

sceneBgImage = None

class Block:
    bgImage = None
    def __init__(self, x, y, text):
        self.x, self.y = x, y
        self.text = text
        if Block.bgImage == None:
            Block.bgImage = load_image('block_bg.png')
    def draw(self):
        Block.bgImage.draw(self.x, self.y)
        font.draw(self.x, self.y, self.text, (0, 0, 127))
    def isEmpty(self):
        return self.text == ''
    def initialize(self):
        self.text = '2' if random.randint(0, 1) == 0 else '4'
    def getValue(self):
        return 0 if self.isEmpty() else int(self.text)
    def setValue(self, v):
        if v == 0:
            self.text = ''
        else:
            self.text = str(v)

class Board:
    def __init__(self):
        self.blocks = []
        for y in range(4):
            for x in range(4):
                # b = Block(100 * x + 100, 100 * y + 100, str(x)+','+str(y))
                b = Block(100 * x + 100, 100 * y + 100, '')
                self.blocks.append(b)
    def draw(self):
        for b in self.blocks:
            b.draw()
    def isFull(self):
        for b in self.blocks:
            if b.isEmpty():
                return False
        return True

    def createNew(self):
        if self.isFull():
            print('Already full')
            return False

        while True:
            index = random.randint(0, 15)
            print('index=', index)
            block = self.blocks[index]
            if block.isEmpty():
                break
        block.initialize()
        return True

    def translateLeft(self, x, y):
        return (x, y)
    def translateRight(self, x, y):
        return (3-x, y)
    def translateDown(self, x, y):
        return (y, x)
    def translateUp(self, x, y):
        return (3-y, 3-x)

    def push(self, translator):
        for y in range(4):
            for x in range(4):
                ox, oy = translator(x, y)
                v = self.getValue(ox, oy)
                # v = self.blocks[y * 4 + x].getValue()
                if v == 0:
                    for x2 in range(x + 1, 4):
                        ox2, oy2 = translator(x2, y)
                        v = self.getValue(ox2, oy2)
                        # v = self.blocks[y * 4 + x2].getValue()
                        if v > 0:
                            self.setValue(ox, oy, v)
                            self.setValue(ox2, oy2, 0)
                            break
                    if v == 0:
                        break
                for x2 in range(x + 1, 4):
                    ox2, oy2 = translator(x2, y)
                    v2 = self.getValue(ox2, oy2)
                    if v == v2:
                        global score
                        score += 2 * v
                        self.setValue(ox, oy, 2 * v)
                        self.setValue(ox2, oy2, 0)
                        break
                    if v2 > 0:
                        break
    def getValue(self, x, y):
        return self.blocks[y * 4 + x].getValue()
    def setValue(self, x, y, v):
        self.blocks[y * 4 + x].setValue(v)


def enter():
    global font, board
    font = load_font('ENCR10B.TTF', 50)
    board = Board()
    global sceneBgImage
    sceneBgImage = load_image('ingame_bg.png')

def exit():
    pass

def update():
    pass

def draw():
    global blocks

    clear_canvas()
    sceneBgImage.draw(400, 300)
    board.draw()
    font.draw(600, 400, str(score), (127, 0, 0))
    update_canvas()

def handle_events():
    events = get_events()
    for e in events:
        if e.type == SDL_QUIT:
            game_framework.quit()
        if e.type == SDL_KEYDOWN:
            if e.key == SDLK_ESCAPE:
                game_framework.pop_state()
            elif e.key == SDLK_SPACE:
                board.createNew()
            elif e.key == SDLK_LEFT:
                board.push(lambda x, y: (x, y))
            elif e.key == SDLK_RIGHT:
                board.push(lambda x, y: (3-x, y))
            elif e.key == SDLK_UP:
                board.push(lambda x, y: (3-y, 3-x))
            elif e.key == SDLK_DOWN:
                board.push(lambda x, y: (y, x))

if __name__ == '__main__':
    import sys
    current_module = sys.modules[__name__]
    open_canvas()
    game_framework.run(current_module)
    close_canvas()
