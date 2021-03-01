#!/usr/bin/env python3

from fill_map import *
from offense import random_ia
from utils import write
from block_at_three import *
from offense import check_offense

def check_next_if_3_pawns(prev_x, prev_y, x, y, map, check) :
    pos_x = x - 1
    while pos_x < x + 2:
        pos_y = y - 1
        while pos_y < y + 2 :
            if prev_x == pos_x and prev_y == pos_y or pos_x > 19 or pos_y > 19 or pos_x < 0 or pos_y < 0:
                pass
            elif pos_x == x and pos_y == y :
                pass
            elif map[pos_x][pos_y] == '2' and check == False:
                if pos_x > x :
                    map, check = check_right(pos_x, pos_y, map, check, y)
                elif pos_x < x :
                    map,check = check_left(pos_x, pos_y, map, check, y)
                elif pos_x == x :
                    map, check = check_vertical(pos_x, pos_y, map, check, y)
            pos_y += 1
        pos_x += 1
    return map, check

def check_next_to_pawn(x, y, map, check) :
    pos_x = x - 1
    while pos_x < x + 2:
        pos_y = y - 1
        while pos_y < y + 2 :
            if pos_x == x and pos_y == y or pos_x > 19 or pos_y > 19 or pos_x < 0 or pos_y < 0:
                pass
            elif map[pos_x][pos_y] == '2' :
                map, check = check_next_if_3_pawns(x, y, pos_x, pos_y, map, check)
            pos_y += 1
        pos_x += 1
    return map, check

def check_defense(map, pos_opp) :
    check = False
    for x in range(20) :
        for y in range(20) :
            if map[x][y] == '2' :
                map, check = check_next_to_pawn(x, y, map, check)
    if check != True :
        map = check_offense(map)
    return map