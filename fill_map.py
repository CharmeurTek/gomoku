#!/usr/bin/env python3

def init_map(map) :
    i = 0
    j = 0
    map = [['0' for i in range(20)] for j in range(20)]

    return map

def fill_map_opp(x, y, map) :
    map[int(x)][int(y)] = '2'
    return map