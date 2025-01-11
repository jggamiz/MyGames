# Game Board Configuration
'''
To modify this value of SIZE, select the count_values_2
function in ai_player.py
'''
SIZE = 8  # Board dimensions (SIZExSIZE)

CORNERS = [
    (0, 0),
    (0, SIZE-1),
    (SIZE-1, 0),
    (SIZE-1, SIZE-1)
]

# Display Settings
CELL_SIZE = 60      # Size of each board cell in pixels
MARGIN = 10         # Space between cells in pixels
BOARD_SIZE = SIZE * CELL_SIZE + (SIZE + 1) * MARGIN  # Total board size including margins
WINDOW_SIZE = (BOARD_SIZE, BOARD_SIZE + 50)  # Window dimensions (width, height). Extra 50px for score

# Game Settings
AI_DELAY_MS = 1000  # Delay before AI moves (milliseconds)
VOLUME = 0.5        # Game sound effects volume (0.0 to 1.0)