#!/usr/bin/env python3
"""
This is the main module, responsible for running the game
"""
import json
from moves import move_gen

# the main class (loading game config)
class Game:

    # This function initializes the game
    def __init__(self, file):
        with open(file) as input_file:
            self.__dict__ = json.loads(input_file.read())

            # The game board
            self.board = list('        \n' * 2 + ' ' + ''.join([
                '.' * int(chr) if chr.isdigit() else chr
                for chr in
                self.fen_string.split()[0].replace('/', '\n ')
            ]) + '\n' + '        \n' * 2)
            self.turn = 0 if self.fen_string.split()[1] == 'w' else 1

# Game config/settings
GAME_SETTINGS = '../resourses/config.json'

bbc = Game(GAME_SETTINGS)
bbc.move_gen()
# print(''.join([' ' + bbc.pieces[p] for p in ''.join(bbc.board)]), (bbc.turn))
