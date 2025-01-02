import random
from reversi import *
from config import SIZE

MAX_DEPTH = 4
positive_infinity = float('inf')
negative_infinity = float('-inf')

# Heuristic weights
PIECE_RATIO_WEIGHT = 20
CORNER_CONTROL_WEIGHT = 500
POSITION_VALUE_WEIGHT = 75

def count_corners(board, token):
    '''
    Count the number of corners containing a specific token on the board
    '''
    corners = [
        (0, 0),
        (0, SIZE-1),
        (SIZE-1, 0),
        (SIZE-1, SIZE-1)
    ]
    
    return sum(1 for row, col in corners if board[row][col] == token)


def count_values(board, token):
    '''
    Calculate the weighted score for a given token based on position values
     - Corners (25): Highly valuable as they are stable and cannot be flipped once captured.
     - Edges (10, 15): Moderately valuable because they are less vulnerable than interior squares.
     - Near-Corners (-5, -10): Risky positions that can lead to losing corners if the opponent takes advantage of them.
     - Center (0, 2, 3, 4): Less critical but can still contribute to controlling the board.
    '''
    values = [
        [25, -5, 15, 10, 10, 15, -5, 25],
        [-5, -10, -4, 2, 2, -4, -10, -5],
        [15, -4, 3, 4, 4, 3, -4, 15],
        [10, 2, 4, 0, 0, 4, 2, 10],
        [10, 2, 4, 0, 0, 4, 2, 10],
        [15, -4, 3, 4, 4, 3, -4, 15],
        [-5, -10, -4, 2, 2, -4, -10, -5],
        [25, -5, 15, 10, 10, 15, -5, 25]
    ]
    
    count = 0
    for i in range(SIZE):
        for j in range(SIZE):
            if board[i][j] == token:
                count+=values[i][j]
    
    return count
    '''
    return sum(
        values[i][j] 
        for i, row in enumerate(board)
        for j, cell in enumerate(row)
        if cell == token
    )
    '''


def heuristic(board, token):
    '''
    Evaluates the state of the game board and assigns a score to it. 
    A higher score indicates a better position for the AI (maximizing).
    Uses weighted factors: piece count, corner control, and position values.
    '''
    rival_token='O' if token=='X' else 'X'
    num_tokens = count_tokens(board, token)
    num_rival_tokens = count_tokens(board, rival_token)
    total_tokens = num_tokens+num_rival_tokens

    # Handle terminal states
    if num_rival_tokens==0: 
        return positive_infinity-1
    if num_tokens==0:
        return negative_infinity+1
    if is_game_over(board):
        return (positive_infinity-1) if num_tokens > num_rival_tokens else (negative_infinity+1)
    
    value=0

    # Piece ratio evaluation (weight: PIECE_RATIO_WEIGHT)
    if total_tokens > 0:
        value += PIECE_RATIO_WEIGHT * max(num_tokens, num_rival_tokens) / total_tokens * (1 if num_tokens > num_rival_tokens else -1)

    # Corner control evaluation (weight: CORNER_CONTROL_WEIGHT)
    corners_diff = count_corners(board, token) - count_corners(board, rival_token)
    value += CORNER_CONTROL_WEIGHT * corners_diff    

    # Position value evaluation (weight: POSITION_VALUE_WEIGHT)
    value_pos_player = count_values(board, token)
    value_pos_rival = count_values(board, rival_token)
    total_value = value_pos_player + value_pos_rival
    
    if total_value>0:
        position_ratio = max(value_pos_player,value_pos_rival) / total_value
        value += POSITION_VALUE_WEIGHT * position_ratio * (1 if value_pos_player > value_pos_rival else -1)

    return value 


def minimax(board, depth, alpha, beta, maximizing_player, token):
    '''
    Implements the Minimax algorithm with alpha-beta pruning for decision-making in Reversi.

    Args:
        board (list): A 2D list representing the current game board.
        depth (int): The maximum depth of recursive search. Represents how many moves ahead the algorithm will consider.
        alpha (float): The best score that the maximizing player can guarantee (initially -∞).
        beta (float): The best score that the minimizing player can guarantee (initially +∞).
        maximizing_player (bool): True if the current turn is for the AI (maximizing player); False otherwise.
        token (str): The AI's token, either 'X' or 'O'.

    Returns:
        tuple:
            - x_move, y_move: Best move coordinates (valid at root only)
            - value (float): The evaluation score of the best move. Positive values favor the AI; negative values favor the opponent.
    '''

    # Base case: return heuristic if depth is 0 or game is over
    if depth==0 or is_game_over(board):
        return -1, -1, heuristic(board, token)
    
    rival_token = 'O' if token=='X' else 'X'
    xmove, ymove = -1,-1

    if maximizing_player: # AI's Turn
        max_eval=negative_infinity
        valid_plays = get_valid_plays(board, token)
        for x,y in valid_plays:
            copy = copy_board(board) # Copy board for simulation
            make_a_play(copy, token, x, y)  # Simulate move
            _,_,value = minimax(copy, depth-1, alpha, beta, False, token) # recurse
            #max_eval = max(max_eval, value)
            if value>max_eval:
                max_eval=value
                if depth==MAX_DEPTH:
                    xmove,ymove = x,y

            alpha = max(alpha,value)
            if beta<=alpha:
                break
        
        return xmove, ymove, max_eval
    
    else: # Opponent's Turn
        min_eval=positive_infinity
        valid_plays = get_valid_plays(board, rival_token)
        for x,y in valid_plays:
            copy = copy_board(board) # Copy board for simulation
            make_a_play(copy, rival_token, x, y) # Simulate move
            _,_,value = minimax(copy, depth-1, alpha, beta, True, token) # recurse
            min_eval = min(min_eval, value)
            beta = min(beta, value)
            if beta<=alpha:
                break
        
        return -1, -1, min_eval
    

def random_play(board, token):
    valid_plays = get_valid_plays(board, token)
    random.shuffle(valid_plays)
    return valid_plays[0]


def intelligent_play(board, token):
    x,y,_ = minimax(board, MAX_DEPTH, negative_infinity, positive_infinity, True, token)
    return [x,y]