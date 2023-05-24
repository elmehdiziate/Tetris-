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
    def collide(self, pos):
        x , y = int(pos.x), int(pos.y)
        if 0<x< FIELD_W and y< FIELD_H:
            return False
        return True
    
    


class Tetromino:
    def __init__(self, tetris):
        self.tetris = tetris
        self.shape = random.choice(list(TETROMINOS.keys()))
        self.blocks = [Block(self, pos) for pos in TETROMINOS[self.shape]]
    
    def collide(self, blocks_position):
        return any(map(Block.collide, self.blocks, blocks_position))

    def move(self,  direction):
        move_direction = MOVEMENT_DIRECTION[direction]
        new_positions = [block.pos + move_direction for block in self.blocks]
        is_collide = self.collide(new_positions)
        
        if not is_collide:             
            for block in self.blocks:
                block.pos += move_direction

    def update(self):
        self.move(direction = 'down')
