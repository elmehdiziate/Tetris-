from setting import *
import math
from Tetromino import Tetromino
class Tetris:
    def __init__(self, app):
        self.app = app
        self.sprite_group = pg.sprite.Group()
        self.field_array = self.get_array()
        self.tetromino = Tetromino(self)
    def check_lines(self):
        row = FIELD_H - 1
        for y in range(FIELD_H - 1, -1, -1):
            for x in range(FIELD_W):
                self.field_array[row][x] = self.field_array[y][x]
                if self.field_array[y][x]:
                    self.field_array[row][x].pos = vec(x,y)
            if sum(map(bool, self.field_array[y])) < FIELD_W:
                row -= 1
            else: 
                for x in range(FIELD_W):
                    self.field_array[row][x].alive = False
                    self.field_array[row][x] = 0
    def put_blocks_in_array(self):
        for block in self.tetromino.blocks:
            x,y = int(block.pos.x), int(block.pos.y)
            self.field_array[y][x] = block 
        
    def get_array(self):
        return [[0 for x in range(FIELD_W)] for y in range(FIELD_H)]
    
    def check_landing(self):
        if self.tetromino.landing:
            self.put_blocks_in_array()
            self.tetromino = Tetromino(self)
    
    def control(self, pressed_key):
        if pressed_key == pg.K_LEFT:
            self.tetromino.move(direction='left')
        elif pressed_key == pg.K_RIGHT:
            self.tetromino.move(direction='right')
        elif pressed_key == pg.K_UP:
            self.tetromino.rotate_right()
        elif pressed_key == pg.K_z:
            self.tetromino.rotate_left()
    
    def draw_grid(self):
        for x in range(FIELD_W):
            for y in range(FIELD_H):
                pg.draw.rect(self.app.screen, "white",
                             (x* TILE_SIZE, y * TILE_SIZE, TILE_SIZE, TILE_SIZE), 1)
    def update(self):
        if self.app.anime_trigger == True:
            self.check_lines()
            self.tetromino.update()
            self.check_landing()
        self.sprite_group.update()

    def draw(self):
        self.draw_grid()
        self.sprite_group.draw(self.app.screen)