import pygame, random
from config import SCREEN_WIDTH, GROUND_Y, OBSTACLE_WIDTH, OBSTACLE_HEIGHT


class Obstacle:

    '''
    Represents an obstacle in the game that moves across the screen.
    '''

    def __init__(self, type="cactus"):
        '''
        Initializes the obstacle with a random position and type.
        '''
        #Initialize the obstacle with its type (e.g., 'cactus' or 'bird').
        self.type = type

        # Load and scale images for both cactus and bird
        self.cactus_image = pygame.image.load("assets/cactus.png")
        self.bird_image = pygame.image.load("assets/bird.png")
        self.cactus_image = pygame.transform.scale(self.cactus_image, (OBSTACLE_WIDTH, OBSTACLE_HEIGHT))
        self.bird_image = pygame.transform.scale(self.bird_image, (OBSTACLE_WIDTH, OBSTACLE_HEIGHT // 2))

        # Assign the current valid image and position
        self.image = self.cactus_image if self.type=="cactus" else self.bird_image
        self.y = GROUND_Y - OBSTACLE_HEIGHT if self.type=="cactus" else GROUND_Y - 1.45*OBSTACLE_HEIGHT


        # Start the obstacle off-screen to the right
        self.x = SCREEN_WIDTH
        
        # Create a collision rectangle based on the image position
        self.rect = self.image.get_rect(topleft=(self.x, self.y))

    
    def update(self, speed):
        '''
        Moves the obstacle across the screen.
        @param speed The current game speed.
        '''
        # Move the obstacle leftwards
        self.x -= speed
        self.rect.x = self.x # sync the image and the rectangle

        # Reset if off-screen
        #if self.x + self.rect.width < 0:
        #    self.reset()
    

    def reset(self):
        '''
        Resets the obstacle to a new random position off-screen.
        '''
        self.x = SCREEN_WIDTH + random.randint(0,150)
        self.type = "bird" if random.choice([True,False]) else "cactus"
        self.image = self.bird_image if self.type=="bird" else self.cactus_image
        self.y = GROUND_Y - OBSTACLE_HEIGHT if self.type == "cactus" else GROUND_Y - 1.45*OBSTACLE_HEIGHT
        self.rect = self.image.get_rect(topleft=(self.x, self.y))
        

    def draw(self, screen):
        '''Draws the obstacle on the game screen.
        @param screen The Pygame screen where the obstacle is rendered.
        '''
        screen.blit(self.image, (self.x, self.y))