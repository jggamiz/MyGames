import pygame, random
from config import SCREEN_WIDTH, GROUND_Y

BRICKS_WIDTH = 80
BRICKS_HEIGHT = 30
BULLET_WIDTH = 45
BULLET_HEIGHT = 30
PLANT_WIDTH = 50
PLANT_HEIGHT = 90
GOOMBA_WIDTH = 60
GOOMBA_HEIGHT = 70

class Obstacle:

    '''
    Represents an obstacle in the game that moves across the screen.
    '''

    def __init__(self, type="land"):
        '''
        Initializes the obstacle with a random position and type.
        '''
        #Initialize the obstacle with its type (e.g., 'cactus' or 'bird').
        self.type = type

        # Load and scale images for all obstacles
        self.plant_image = pygame.image.load("assets/Piranha_Plant_-_Artwork.webp")
        self.plant_image = pygame.transform.scale(self.plant_image, (PLANT_WIDTH, PLANT_HEIGHT))

        self.goomba_image = pygame.image.load("assets/goomba.png")
        self.goomba_image = pygame.transform.scale(self.goomba_image, (GOOMBA_WIDTH, GOOMBA_HEIGHT))

        self.bullet_image = pygame.image.load("assets/bullet.jpg")
        self.bullet_image = pygame.transform.scale(self.bullet_image, (BULLET_WIDTH, BULLET_HEIGHT))

        self.bricks_image = pygame.image.load("assets/bricks.jpg")
        self.bricks_image = pygame.transform.scale(self.bricks_image, (BRICKS_WIDTH, BRICKS_HEIGHT))

        # Assign the current valid image and position
        if self.type=="land":
            self.image = random.choice([self.goomba_image, self.plant_image])
        else: # air
            self.image = random.choice([self.bricks_image, self.bullet_image])

        if self.image==self.goomba_image: 
            self.y = GROUND_Y - 70
        elif self.image==self.plant_image: 
            self.y = GROUND_Y - PLANT_HEIGHT
        elif self.image==self.bricks_image: 
            self.y = GROUND_Y - PLANT_HEIGHT - random.randint(-5, 25)
        elif self.image==self.bullet_image: 
            self.y = GROUND_Y - PLANT_HEIGHT - random.randint(-5, 25)

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
    

    def reset(self):
        '''
        Resets the obstacle to a new random position off-screen.
        '''
        self.x = SCREEN_WIDTH + random.randint(0,150)
        self.type = "air" if random.choice([True,False]) else "land"

        if self.type=="land":
            self.image = random.choice([self.goomba_image, self.plant_image])
        else: # air
            self.image = random.choice([self.bricks_image, self.bullet_image])
 
        if self.image==self.goomba_image: self.y = GROUND_Y - GOOMBA_HEIGHT
        elif self.image==self.plant_image: self.y = GROUND_Y - PLANT_HEIGHT
        elif self.image==self.bricks_image: self.y = GROUND_Y - random.randint(85, 110)
        elif self.image==self.bullet_image: self.y = GROUND_Y - random.randint(85, 110)
        
        self.rect = self.image.get_rect(topleft=(self.x, self.y))
        

    def draw(self, screen):
        '''
        Draws the obstacle on the game screen.
        @param screen The Pygame screen where the obstacle is rendered.
        '''
        screen.blit(self.image, (self.x, self.y))