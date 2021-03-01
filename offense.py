#!/usr/bin/env python3
import random
from utils import write
from block_at_three import *

def offense_next_to(x, y, map, check) :
    pos_x = x - 1
    while pos_x < x + 2:
        pos_y = y - 1
        while pos_y < y + 2 :
            if pos_x == x and pos_y == y or pos_x > 19 or pos_y > 19 or pos_x < 0 or pos_y < 0:
                pass
            elif map[pos_x][pos_y] == '1' :
                if pos_x > x :
                    map, check = check_right(pos_x, pos_y, map, check, y)
                elif pos_x < x :
                    map,check = check_left(pos_x, pos_y, map, check, y)
                elif pos_x == x :
                    map, check = check_vertical(pos_x, pos_y, map, check, y)
            pos_y += 1
        pos_x += 1
    return map, check

def check_offense(map) :
    check = False
    for x in range(20) :
        for y in range(20) :
            if map[x][y] == '1' :
                map, check = offense_next_to(x, y, map, check)
    if check != True :
        map = random_ia(map)
    return map

def random_ia(map) :
    x = random.randint(0,19)
    y = random.randint(0,19)
    if map[x][y] == '0' :
        map[x][y] = '1'
        write("{},{}".format(x, y))
    else :
        random_ia(map)
    return map