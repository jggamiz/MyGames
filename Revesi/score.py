from reversi import count_tokens

def score(board):
    '''
    Return the current score for both players
    '''
    return {
        'X':count_tokens(board,'X'),
        'O':count_tokens(board,'O')
    }