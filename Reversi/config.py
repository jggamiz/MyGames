# Game Board Configuration
SIZE = 8  # Board dimensions (8x8). Not modifiable as per Reversi rules

# Display Settings
CELL_SIZE = 60       # Size of each board cell in pixels
MARGIN = 10         # Space between cells in pixels
BOARD_SIZE = SIZE * CELL_SIZE + (SIZE + 1) * MARGIN  # Total board size including margins
WINDOW_SIZE = (BOARD_SIZE, BOARD_SIZE + 50)  # Window dimensions (width, height). Extra 50px for score

# Game Settings
AI_DELAY_MS = 1000  # Delay before AI moves (milliseconds)
VOLUME = 0.5        # Game sound effects volume (0.0 to 1.0)