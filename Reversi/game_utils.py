from config import SIZE, CORNERS

def valid_pos(x,y):
    '''
    Check if a position is within the board boundaries
    '''
    return 0<=x<SIZE and 0<=y<SIZE

def empty_pos(board,x,y):
    '''
    Check if the position is empty (contains a space)
    '''
    return board[x][y]==' '

def is_a_corner(x,y):
    '''
    Check if the given coordinates represent a corner
    '''
    return (x,y) in CORNERS

def count_tokens(board, token):
    '''
    Count the total number of occurrences of a specific token on the board
    '''
    return sum(row.count(token) for row in board)

def score(board):
    '''
    Return the current score for both players
    '''
    return {
        'X':count_tokens(board,'X'),
        'O':count_tokens(board,'O')
    }

def count_corners(board, token):
    '''
    Count the number of corners containing a specific token on the board
    '''    
    return sum(1 for (row,col) in CORNERS if board[row][col] == token)