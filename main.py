#!/usr/bin/env python3

from utils import *
from defense import check_defense
from fill_map import *
from offense import random_ia

if __name__ == '__main__':
    map = []
    map = init_map(map)
    tab = []
    pos_opp = []
    check = False

    while True:
        line = read()
        tab = line.split(' ')
        if tab[0].find("START") != -1 and check == False:
            if tab[1] == "20\n":
                write("OK")
            else :
                write("ERROR bad START parameter")
        elif line.find("BEGIN") is not -1 and check == False :
            check_defense(map, pos_opp)
        elif tab[0].find("TURN") is not -1 and check == False:
            pos_opp = tab[1].split(',')
            map = fill_map_opp(int(pos_opp[0]), int(pos_opp[1]), map)
            check_defense(map, pos_opp)
        elif tab[0].find("BOARD") is not -1 or check == True:
            check = True
            if tab[0].find("DONE") is not -1 :
                check = False
                random_ia(map)
            elif tab[0].find("BOARD") is -1 :
                board_pos = line.split(',')
                x = int(board_pos[0])
                y = int(board_pos[1])
                z = board_pos[2].rsplit('\n')
                map[x][y] = z[0]
        elif tab[0].find("END") is not -1 and check == False:
            exit(0)