import random

def __init__(self):
    self.board = []

def create_board(self):
    for a in range(3): 
        row = []
        for j in range(3):
            row.append('-')
        self.board.append(row)

def get_random_frist_palyer(self):
    return random.randint(0, 1)

def fix_spot(self, row, col, player):
    self.board[row][col] = player

def is_player_win(self, player):
    win = None

    n = len(self.board)

    for i in range(n):
        win = True
        for j in range(n):
            if self.board[i][j] != player:
                win = False
                break
        if win:
            return win


    win = True
    for i in range(n):
        if self.board[i][j] != player:
            win = False
            break
    if win:
        return win

    win = True
    for i in range(n):
        if self.board[i][n - 1 - i] != player:
            win = False
            break
    if win:
        return win
    return False

def is_board_filled(self):
    for row in self.board:
        for item in row:
            if item == '':
                return False
    
    return True

def swap_player_turn(self, player):
    return 'x' if player == 'o' else 'o'

def show_board(self):
    for row in self.board:
        for item in row:
            print(item, end=' ')
        print()

def start(self):
    self.create_board()








