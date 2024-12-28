'''
Screen Settings:
Adjusts screen dimensions and background color
'''
SCREEN_WIDTH = 800         # Width of the game window
SCREEN_HEIGHT = 400        # Height of the game window

'''
Dino Settings:
Defines the dinosaur's starting position and size
'''
DINO_START_X = 100
DINO_START_Y = SCREEN_HEIGHT-100
DINO_WIDTH = 60
DINO_HEIGHT = 80


'''
Gravity and Jump:
Controls the dinosaur's jump physics
'''
GRAVITY = 0.45             # Gravity applied each frame while in the air
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
OBSTACLE_HEIGHT = 80
INITIAL_SPEED = 10
MAX_SPEED = INITIAL_SPEED*2
SPEED_INC = 0.2


'''
Boss Settings:
'''
BOSS_WIDTH = 300
BOSS_HEIGHT = 300
BOSS_START_X = SCREEN_WIDTH
BOSS_START_Y = GROUND_Y - BOSS_HEIGHT
BOSS_HEALTH = 3


'''
Potion Settings:
'''
POTION_WIDTH = 37
POTION_HEIGHT = 37
POTIONS_NEEDED = 3
POTION_Y_RANGE = (GROUND_Y - POTION_HEIGHT, GROUND_Y - 2 * POTION_HEIGHT)  # Range for random placement
# Potion Count Display
POTION_DISPLAY_X = SCREEN_WIDTH - 150
POTION_DISPLAY_Y = 20


'''
Fireball Settings:
'''
FIREBALL_WIDTH = 35
FIREBALL_HEIGHT = 35
FIREBALL_SPEED = 10
FIRE_COOLDOWN = 0.5  # Time in seconds between consecutive fireballs


'''
Scoring and colors:
Settings for score and font size
'''
FONT_SIZE = 36             
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
GREEN = (1,150,32)
SKY_COLOR = (135, 206, 235)