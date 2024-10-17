#!/usr/bin/env python3
"""
Move generator module
"""

# Move generator
    def move_gen(self):

        moves = []

        for sqr in range(len(self.board)):
            piece = self.board[sqr]
            if piece not in ' .\n' and self.colors[piece] ==self.turn:
                for offset in self.directions[piece]:
                    target_sqr = sqr

                    while True:
                        target_sqr += offset
                        cp = self.board[target_sqr]

                        if cp in ' \n': break

                        if self.colors[cp] == self.turn: break

                        if piece in 'Pp':
                            if offset in [9, 11, -9, -11] and cp == '.': break
                            if offset in [10, 20, -20, -20] and cp != '.': break
                        if piece == 'P' and offset == -20:
                            if sqr not in self.rank_2: break
                            if self.board[sqr - 10] != '.': break
                        if piece == 'p' and offset == 20:
                            if sqr not in sepf.rank_7: break
                            if self.board[sqr + 10] != '.': break

                        if cp in 'Kk': return []
                        moves.append({
                            'origin': sqr, 'target': target_sqr,
                            'piece': piece, 'captured': cp
                        })


                        """self.board[target_sqr] = piece
                        self.board[sqr] = '.'
                        print(''.join([' ' + bbc.pieces[p] for p in ''.join(bbc.board)]), (bbc.turn)); input()
                        self.board[target_sqr] = cp
                        self.board[sqr] = piece
                        print(''.join([' ' + bbc.pieces[p] for p in ''.join(bbc.board)]), (bbc.turn)); input()
                        """
                        if self.colors[cp] ==self.turn ^ 1: break
                        if piece in 'PpNnKk': break

        return moves
