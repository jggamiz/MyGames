from board import *
from config import SIZE

def valid_pos(x,y):
    '''
    Check if a position is within the board boundaries
    '''
    return 0<=x<SIZE and 0<=y<SIZE


def empty_pos(board,x,y):
    return board[x][y]==' '


def is_a_corner(x,y):
    '''
    Check if the given coordinates represent a corner
    '''
    return (x==0 and y==0) or (x==SIZE-1 and y==0) or (x==0 and y==SIZE-1) or (x==SIZE-1 and y==SIZE-1)


def valid_play(board, token, initx, inity):
    if not empty_pos(board, initx, inity) or not valid_pos(initx,inity):
        return False
    
    board[initx][inity] = token
    rival_token = 'O' if token=='X' else 'X'
    changing_tokens=[]

    # To change the necessary tokens, we'll have to move in all eight possible directions (up, down, left, right and four diagonals)
    for directionx, directiony in [[0,1],[1,1],[1,0],[1,-1],[0,-1],[-1,-1],[-1,0],[-1,1]]:
        x,y = initx,inity
        x += directionx # first step in the direction
        y += directiony # first step in the direction

        if valid_pos(x,y) and board[x][y]==rival_token:
            x+=directionx
            y+=directiony

            if not valid_pos(x,y): continue

            while board[x][y] == rival_token:
                x+=directionx
                y+=directiony
                
                if not valid_pos(x,y): break

            if not valid_pos(x,y): continue

            if board[x][y] == token: # We have to convert all the tokens we've been passing
                while True:
                    x-=directionx
                    y-=directiony

                    if x==initx and y==inity: break

                    changing_tokens.append([x,y])
    
    board[initx][inity] = ' '
    
    if len(changing_tokens) == 0: 
        return False
    return changing_tokens


def get_valid_plays(board, token):
    '''
    Get all valid play positions for the given token
    '''
    return [(i,j) 
            for i in range(SIZE) 
            for j in range(SIZE) 
            if valid_play(board,token,i,j)]


def make_a_play(board, token, x, y):
    '''
    Make a play on the board if valid and flip appropriate tokens
    '''
    tokens_to_flip  = valid_play(board, token, x, y)
    if not tokens_to_flip: 
        return False

    board[x][y] = token
    for row,col in tokens_to_flip :
        board[row][col] = token
    
    return True


def is_game_over(board):
    '''
    Check if the game is over (board full or no valid moves)
    '''  
    filled_spaces  = sum(1 for row in board for cell in row if cell != ' ')
    return (filled_spaces==SIZE**2 or (not get_valid_plays(board, 'X') and not get_valid_plays(board, 'O')))


def count_tokens(board, token):
    '''
    Count the total number of occurrences of a specific token on the board
    '''
    return sum(row.count(token) for row in board)