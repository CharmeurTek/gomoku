#!/usr/bin/env python3

from utils import write

def fill_map_ia(x, y, map, check) :
    if x < 0 or x > 19 or y < 0 or y > 19 :
        return map, check
    if map[x][y] == '0' :
        map[int(x)][int(y)] = '1'
        check = True
        write("{},{}".format(x, y))
    return map, check

def check_right(pos_x, pos_y, map, check, y):
    if pos_y > y :
        map, check = fill_map_ia(pos_x + 1, pos_y + 1, map, check)
    elif pos_y < y :
        map, check = fill_map_ia(pos_x + 1, pos_y - 1, map, check)
    elif pos_y == y :
        map, check = fill_map_ia(pos_x + 1, pos_y, map, check)
    return map, check

def check_left(pos_x, pos_y, map, check, y) :
    if pos_y > y :
        map, check = fill_map_ia(pos_x - 1, pos_y + 1, map, check)
    elif pos_y < y :
        map, check = fill_map_ia(pos_x - 1, pos_y - 1, map, check)
    elif pos_y == y :
        map, check = fill_map_ia(pos_x - 1, pos_y, map, check)
    return map, check

def check_vertical(pos_x, pos_y, map, check, y) :
    if pos_y > y :
        map, check = fill_map_ia(pos_x, pos_y + 1, map, check)
    elif pos_y < y :
        map, check = fill_map_ia(pos_x, pos_y - 1, map, check)
    elif pos_y == y :
        map, check = fill_map_ia(pos_x, pos_y, map, check)
    return map, check