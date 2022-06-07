board = [' ' for x in range(10)]

def print_board(board):
    print(board[1] + board[2] + board[3] + '\n'
        + board[4] + board[5] + board[6] + '\n'
        + board[7] + board[8] + board[9])

def insertBoard(letter, pos):
    pass

def insertLetter(letter, pos):
    board[pos] = letter    

def spaceIsFree(pos):
    return board[pos] == ''

def isWinner(bo, le):
    return ((bo[7] == le and bo[8] == le and bo[9] == le) or
    (bo[4] == le and bo[5] == le and bo[6] == le) or 
    (bo[1] == le and bo[2] == le and bo[3] == le) or 
    (bo[7] == le and bo[4] == le and bo[1] == le) or 
    (bo[8] == le and bo[5] == le and bo[2] == le) or 
    (bo[9] == le and bo[6] == le and bo[3] == le) or 
    (bo[7] == le and bo[5] == le and bo[3] == le) or 
    (bo[9] == le and bo[5] == le and bo[1] == le))

def playerMove():
    pass

def selectRandom():
    pass

def compMove():
    pass

def isBoardFull(board):
    pass

def main():
    pass







