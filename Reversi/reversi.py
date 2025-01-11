from board import *
from game_utils import *
from config import SIZE

def check_direction(board, token, start_x, start_y, dir_x, dir_y):
    '''
    Check one direction for valid moves and return tokens to flip
    '''
    tokens_to_flip = []
    x, y = start_x + dir_x, start_y + dir_y
    rival_token = 'O' if token == 'X' else 'X'

    # Ensure the immediate next position has a rival token
    if not valid_pos(x, y) or board[x][y] != rival_token:
        return []

    # Traverse in the direction while encountering rival tokens
    while valid_pos(x, y) and board[x][y] == rival_token:
        tokens_to_flip.append([x, y])
        x += dir_x
        y += dir_y

    # If we end up at a valid position with the current token, return the tokens to flip
    if valid_pos(x, y) and board[x][y] == token:
        return tokens_to_flip

    # Otherwise, return an empty list
    return []

def valid_play(board, token, start_x, start_y):
    '''
    Check if a move is valid and return the tokens to flip
    '''
    # Validate the initial position
    if not valid_pos(start_x, start_y) or not empty_pos(board, start_x, start_y):
        return False
 
    # Eight possible directions: up, down, left, right and four diagonals
    directions = [[0,1], [1,1], [1,0], [1,-1], [0,-1], [-1,-1], [-1,0], [-1,1]]
    tokens_to_flip = []

    # Check all directions for tokens to flip
    for dir_x, dir_y in directions:
        tokens_to_flip.extend(check_direction(board, token, start_x, start_y, dir_x, dir_y))

    # Return the flipped tokens if any, otherwise False
    return tokens_to_flip if tokens_to_flip else False

def get_valid_plays(board, token):
    '''
    Get all valid play positions for the given token
    '''
    return [(row,col) 
            for row in range(SIZE) 
            for col in range(SIZE) 
            if valid_play(board,token,row,col)]

def make_a_play(board, token, x, y):
    '''
    Make a play on the board if valid and flip appropriate tokens
    '''
    tokens_to_flip  = valid_play(board, token, x, y)
    if not tokens_to_flip: 
        return False

    board[x][y] = token
    for row,col in tokens_to_flip:
        board[row][col] = token
    
    return True

def is_game_over(board):
    '''
    Check if the game is over (board full or no valid moves)
    '''  
    filled_spaces  = sum(1 for row in board for cell in row if cell!=' ')
    return (filled_spaces==SIZE**2 or (not get_valid_plays(board, 'X') and not get_valid_plays(board, 'O')))