import pygame, random
from config import POTION_HEIGHT, POTION_WIDTH, SCREEN_WIDTH, OBSTACLE_HEIGHT, GROUND_Y

class Potion:
    
    '''
    Represents a collectible potion in the game.
    '''

    def __init__(self, obstacle):
        '''
        Initializes the potion at a random reachable position, avoiding overlap with obstacles.
        @param obstacles The list of obstacles to avoid overlap.
        '''
        self.width = POTION_WIDTH
        self.height = POTION_HEIGHT
    
        # Load and scale the images
        self.mushroom_image = pygame.image.load("assets/potion.png")
        self.mushroom_image = pygame.transform.scale(self.mushroom_image, (self.width, self.height))

        self.poison_image = pygame.image.load("assets/poison.png")
        self.poison_image = pygame.transform.scale(self.poison_image, (self.width, self.height))

        # Default
        self.is_potion = True
        self.image = self.mushroom_image

        # Set a valid position
        self.reset(obstacle)


    def reset(self, obstacles):
        '''
        Places the potion at a random reachable position, avoiding overlap with obstacles.
        @param obstacles The list of obstacles to avoid overlap.
        '''
        valid_position = False
        while not valid_position:
            self.x = random.randint(SCREEN_WIDTH, SCREEN_WIDTH + 300)  # Off-screen to the right
            self.y = GROUND_Y - random.randint(self.height, 2 * OBSTACLE_HEIGHT)

            # Create a rect for collision purposes
            self.rect = pygame.Rect(self.x, self.y, self.width, self.height)

            # Check for overlap with obstacles
            valid_position = all(not self.rect.colliderect(obstacle.rect) for obstacle in obstacles)

        # Randomize whether this is a potion or poison
        self.is_potion = random.choices([True, False], weights=[80, 20], k=1)[0]
        self.image = self.mushroom_image if self.is_potion else self.poison_image


    def is_off_screen(self):
        '''
        Checks if the potion has moved off-screen.
        @return True if the potion is off-screen, False otherwise.
        '''
        return self.x + self.width < 0


    def update(self, speed):
        '''
        Moves the potion across the screen at the current game speed.
        @param speed The current game speed.
        '''
        self.x -= speed
        self.rect.x = self.x  # Sync rect position with the image


    def draw(self, screen):
        '''
        Renders the potion on the game screen.
        @param screen The Pygame screen where the potion is rendered.
        '''
        screen.blit(self.image, (self.x, self.y))