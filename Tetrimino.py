from setting import *
import math


class Block(pg.sprite.Sprite):
    def __init__(self, tetrimino, pos) :
        self.tetrimino = tetrimino
        super().__init__(tetrimino.tetris.sprite_group)
        self.image = pg.Surface([TILE_SIZE, TILE_SIZE])
        self.image.fill('red')
        self.rect = self.image.get_rect()
        self.rect.topleft = pos[0] * TILE_SIZE , pos[1] * TILE_SIZE
        
class Tetrimino:
    def __init__(self, tetris):
        self.tetris = tetris
        Block(self, (4,7))
    def update(self):
        pass
    def draw(self):
        pass
    