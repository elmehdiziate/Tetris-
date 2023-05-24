from setting import *
import math
import random


class Block(pg.sprite.Sprite):
    def __init__(self, tetromino, pos):
        self.tetromino = tetromino
        self.pos = pos + INIT_POS_OFFSET
        super().__init__(tetromino.tetris.sprite_group)
        self.image = pg.Surface([TILE_SIZE, TILE_SIZE])
        pg.draw.rect(self.image, 'purple', (1,1,TILE_SIZE - 2, TILE_SIZE - 2), border_radius=5)
        self.rect = self.image.get_rect()
        
    def rotate_right(self, pivot):
        translated = self.pos - pivot
        rotated = translated.rotate(90)
        return rotated + pivot
    
    def rotate_left(self, pivot):
        translated = self.pos - pivot
        rotated = translated.rotate(-90)
        return rotated + pivot

    def set_pos(self):
        self.rect.topleft = self.pos * TILE_SIZE
    
    def update(self):
        self.set_pos()
    def collide(self, pos):
        x , y = int(pos.x), int(pos.y)
        if 0 <= x <FIELD_W and y < FIELD_H and (
            y<0 or not self.tetromino.tetris.field_array[y][x]
        ):
            return False
        return True
    
    


class Tetromino:
    def __init__(self, tetris):
        self.tetris = tetris
        self.shape = random.choice(list(TETROMINOS.keys()))
        self.blocks = [Block(self, pos) for pos in TETROMINOS[self.shape]]
        self.landing = False
    
    def collide(self, blocks_position):
        return any(map(Block.collide, self.blocks, blocks_position))

    def move(self,  direction):
        move_direction = MOVEMENT_DIRECTION[direction]
        new_positions = [block.pos + move_direction for block in self.blocks]
        is_collide = self.collide(new_positions)
        
        if not is_collide:             
            for block in self.blocks:
                block.pos += move_direction
        elif direction == 'down':
            self.landing = True
    
    def rotate_right(self):
        pivot_pos = self.blocks[0].pos
        new_block_positions = [block.rotate_right(pivot_pos) for block in self.blocks]
        
        if(not self.collide(new_block_positions)):
            for i, block in enumerate(self.blocks):
                block.pos = new_block_positions[i]
    def rotate_left(self):
        pivot_pos = self.blocks[0].pos
        new_block_positions = [block.rotate_left(pivot_pos) for block in self.blocks]
        
        if(not self.collide(new_block_positions)):
            for i, block in enumerate(self.blocks):
                block.pos = new_block_positions[i]
                

    def update(self):
        self.move(direction = 'down')
