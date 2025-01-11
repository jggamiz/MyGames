from config import SIZE

def new_board():
    '''
    Create a new empty game board
    '''
    return [[' '  for _ in range(SIZE)] for _ in range(SIZE)]

def restart_board(board):
    '''
    Reset the board to the initial Reversi starting position
    '''
    # Clear the board using list comprehension
    for _, row in enumerate(board):
        row[:] = [' ' for _ in range(SIZE)]
    
    center = SIZE // 2
    board[center-1][center-1] = 'X'
    board[center-1][center] = 'O'
    board[center][center-1] = 'O'
    board[center][center] = 'X'

def copy_board(board):
    '''
    Create a deep copy of the game board
    '''
    return [row[:] for row in board]