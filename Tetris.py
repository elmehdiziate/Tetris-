from setting import *
import math
from Tetrimino import Tetrimino
class Tetris:
    def __init__(self, app):
        self.app = app
        self.tetrimino = Tetrimino(self)
    def draw_grid(self):
        for x in range(FIELD_W):
            for y in range(FIELD_H):
                pg.draw.rect(self.app.screen, "white",
                             (x* TILE_SIZE, y * TILE_SIZE, TILE_SIZE, TILE_SIZE), 1)
    def update(self):
        self.tetrimino.update()
    def draw(self):
        self.draw_grid()