import pygame as pg

vec = pg.math.Vector2
FPS = 60
FIELD_COLOR = (30, 30, 30)

MOVEMENT_DIRECTION = {'left' : vec(-1,0), 
                      'right': vec(1,0), 
                      'down' : vec(0,1)}
TILE_SIZE = 20
FIELD_SIZE = FIELD_W, FIELD_H = 15, 30
FIELD_RES = FIELD_W * TILE_SIZE, FIELD_H * TILE_SIZE
INIT_POS_OFFSET = vec(FIELD_W // 2 - 1, 0)
#dictionary for the shapes (tetriminos)
TETROMINOS = {
    # T shape
    "T" : [(0,0),(-1,0),(0,-1),(1,0)],
    # sqaure shape
    "O" : [(0,0), (0,-1), (1,0), (1,-1)],
    # J shape
    "J" : [(0,0), (-1,0), (0,-1), (0,-2)],
    # L shape
    "L" : [(0,0), (1,0), (0,-1), (0,-2)],
    # I shape
    "I" : [(0,0), (0,1), (0,-1), (0,-2)],
    # S shape
    "S" : [(0,0), (-1,0), (0,-1), (1,-1)],
    # Z shape
    "Z" : [(0,0), (1,0),(0,-1), (-1,-1)]
}