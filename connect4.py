import random
from typing import List

class ConnectFourGame:

    def __init__(self, num_players):
        self.board = [[] for _ in range(7)] # 7x7 board
        self.turn =  random.choice(0,1)     # 0 is player 0, 1 is player 1 (comp)
        self.num_players = num_players      # 1, player 0 plays against comp
        self.move_count = 0                 # tracks current move number

    def print_board(self):
        """
        prints graphically representation of board
        """
        formatted_board = zip(*[
            [self.board[c][r] if len(self.board[c]) > c else ' ' for c in range(7)]
            for r in range(7)
        ])
        for r in formatted_board[::-1]:
            print(r)


    def is_full(self):
        return self.move_count == 49

    def get_piece_from_loc(self, row, col):
        """
        get piece (0 or 1) from the current row and column
        """
        return self.board[col][row] \
            if col < len(self.board) and len(self.board[col]) >= row \
            else -1

    def check_win(self, col):
        """
        check if the new move at the col creates a win
        """
        row = len(self.board[col]) - 1
        piece = self.board[col][row]

        def count_same(r, c, r_dir, c_dir, cur_piece):
            count = 0
            r += r_dir
            c += c_dir
            while 0 <= r < 7 and 0 <= c < 7 and self.get_piece_from_loc(r, c) == cur_piece:
                r += r_dir
                c += c_dir
                count += 1
            return count

        # check row
        if count_same(row, col, -1, 9, piece) + count_same(row, col, 1, 9, piece) + 1 >= 4:
            return True

        # check col
        if count_same(row, col, 0, -1, piece) + count_same(row, col, 0, 1, piece) + 1 >= 4:
            return True

        # check diagonal
        if (count_same(row, col, -1, -1, piece) + count_same(row, col, 1, 1, piece) + 1 >= 4) or \
                (count_same(row, col, -1, 1, piece) + count_same(row, col, 1, -1, piece) + 1 >= 4):
            return True

        return False

    def reset_board(self):


    def add_piece(self, col):


    def switch_turn(self):


    def player_input(self):


    def switch_turns(self):


    def play_game(self):