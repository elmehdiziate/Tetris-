from setting import *
import math
import random


class Block(pg.sprite.Sprite):
    def __init__(self, tetromino, pos):
        self.tetromino = tetromino
        self.pos = pos + INIT_POS_OFFSET
        super().__init__(tetromino.tetris.sprite_group)
        self.image = pg.Surface([TILE_SIZE, TILE_SIZE])
        self.image.fill('purple')
        self.rect = self.image.get_rect()

    def set_pos(self):
        self.rect.topleft = self.pos * TILE_SIZE
    
    def update(self):
        self.set_pos()
    
    


class Tetromino:
    def __init__(self, tetris):
        self.tetris = tetris
        self.shape = random.choice(list(TETROMINOS.keys()))
        self.blocks = [Block(self, pos) for pos in TETROMINOS[self.shape]]

    def move(self,  direction):
        move_direction = MOVEMENT_DIRECTION[direction]
        for block in self.blocks:
            block.pos += move_direction

    def update(self):
        self.move('down')

    def draw(self):
        pass
