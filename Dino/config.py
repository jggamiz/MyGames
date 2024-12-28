'''
Screen Settings:
Adjusts screen dimensions and background color
'''
SCREEN_WIDTH = 800         # Width of the game window
SCREEN_HEIGHT = 400        # Height of the game window
BACKGROUND_COLOR = (255, 255, 255)  # White background


'''
Dino Settings:
Defines the dinosaur's starting position and size
'''
DINO_START_X = 100
DINO_START_Y = SCREEN_HEIGHT-100
DINO_WIDTH = 60
DINO_HEIGHT = 60


'''
Gravity and Jump:
Controls the dinosaur's jump physics
'''
GRAVITY = 0.5              # Gravity applied each frame while in the air
JUMP_VELOCITY = -10        # Initial velocity for a jump


'''
Ground Level:
Used to determine where the dinosaur should land
'''
GROUND_Y = SCREEN_HEIGHT-50  # Y-coordinate for the ground level


'''
Obstacle Settings:
Basic obstacle dimensions and speed
'''
OBSTACLE_WIDTH = 40
OBSTACLE_HEIGHT = 60
INITIAL_SPEED = 10
MAX_SPEED = INITIAL_SPEED*2
SPEED_INC = 0.2


'''
Scoring and colors:
Settings for score and font size
'''
SCORE_INCREMENT = 1
FONT_SIZE = 36             
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
GREEN = (1,150,32)
SKY_COLOR = (135, 206, 235)
