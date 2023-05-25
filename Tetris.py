from setting import *
import math
from Tetromino import Tetromino
import pygame.freetype as ft

class Content:
    def __init__(self, app) :
        self.app = app
        self.font = ft.Font(FONT_PATH)
    def draw(self):
        self.font.render_to(self.app.screen, (WIN_W*0.6 , WIN_H*0.02), 
                            text="TETRIS-", fgcolor='white', size = TILE_SIZE *1.75, 
                            bgcolor='black')
class Tetris:
    def __init__(self, app):
        self.app = app
        self.sprite_group = pg.sprite.Group()
        self.field_array = self.get_array()
        self.tetromino = Tetromino(self)
        self.speed_up = False
        self.next_tetromino = Tetromino(self, current = False)
    def game_over(self):
        if self.tetromino.blocks[0].pos.y == INIT_POS_OFFSET[1]:
            pg.time.wait(300)
            return True
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
            if self.game_over():
                self.app.__init__()
            else:
                self.speed_up = False
                self.put_blocks_in_array()
                self.next_tetromino.current = True
                self.tetromino = self.next_tetromino
                self.next_tetromino = Tetromino(self, current=False)
    
    def control(self, pressed_key):
        if pressed_key == pg.K_LEFT:
            self.tetromino.move(direction='left')
        elif pressed_key == pg.K_RIGHT:
            self.tetromino.move(direction='right')
        elif pressed_key == pg.K_UP:
            self.tetromino.rotate_right()
        elif pressed_key == pg.K_z:
            self.tetromino.rotate_left()
        elif pressed_key == pg.K_DOWN:
            self.speed_up = True
    
    def draw_grid(self):
        for x in range(FIELD_W):
            for y in range(FIELD_H):
                pg.draw.rect(self.app.screen, "black",
                             (x* TILE_SIZE, y * TILE_SIZE, TILE_SIZE, TILE_SIZE), 1)
    def update(self):
        trigger = [self.app.anime_trigger, self.app.fast_trigger][self.speed_up]
        if trigger == True:
            self.check_lines()
            self.tetromino.update()
            self.check_landing()
        self.sprite_group.update()

    def draw(self):
        self.draw_grid()
        self.sprite_group.draw(self.app.screen)