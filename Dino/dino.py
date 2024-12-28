import pygame
from config import DINO_START_X, DINO_START_Y, DINO_WIDTH, DINO_HEIGHT, GRAVITY, JUMP_VELOCITY, GROUND_Y


class Dino:

    '''
    Represents the player-controlled dinosaur in the game, including 
    movement, jumping, ducking, and collision handling.
    '''

    def __init__(self): 
        '''
        Initializes the Dino object, setting up its position, size, image,
        movement attributes, and collision rectangle.
        '''
        # Initial position and size setup for the dinosaur
        self.x = DINO_START_X
        self.y = GROUND_Y - DINO_HEIGHT
        self.width = DINO_WIDTH
        self.height = DINO_HEIGHT

        # Movements attributes
        self.velocity_y = 0
        self.jumping = False
        self.ducking = False

        # Load and scale the dinosaur image
        self.image_running = pygame.image.load("assets/dino.png")
        self.image_ducking = pygame.image.load("assets/dino_ducking.png")
        self.image_running = pygame.transform.scale(self.image_running, (DINO_WIDTH, DINO_HEIGHT))
        self.image_ducking = pygame.transform.scale(self.image_ducking, (DINO_WIDTH, DINO_HEIGHT // 2))

        # Create a collision rectangle based on the image position
        self.rect = self.image_running.get_rect(topleft=(self.x, self.y))



    def jump(self):
        '''
        Initiates a jump action for the Dino if it is not currently jumping.
        '''
        if not self.jumping:
            self.velocity_y = JUMP_VELOCITY
            self.jumping = True
    

    def duck(self):
        '''
        Sets the Dino to duck mode, reducing its height.
        '''
        self.ducking = True
        self.height = DINO_HEIGHT // 2
        self.rect.height = self.height
        self.rect.y = GROUND_Y - self.height
    

    def stand_up(self):
        '''
        Resets the Dino from ducking mode to its standard height.
        '''
        if self.ducking:
            self.ducking = False
            self.height = DINO_HEIGHT
            self.rect.height = self.height
            self.rect.y = GROUND_Y - self.height


    def update(self):
        '''
        Updates the Dino's position and movement attributes each frame.
        '''
        if self.jumping:
            self.velocity_y += GRAVITY
            self.y += self.velocity_y

            self.rect.y = self.y

            # Reset if on ground
            if self.y >= GROUND_Y-self.rect.height:
                self.y = GROUND_Y-self.rect.height
                self.jumping = False
                self.velocity_y = 0


    def draw(self, screen):
        '''
        Draws the Dino on the game screen.
        @param screen The Pygame screen where the Dino's image is rendered.
        '''
        if self.ducking: screen.blit(self.image_ducking, (self.x, self.y + (DINO_HEIGHT // 2)))
        else : screen.blit(self.image_running, (self.x, self.y))
  

    def reset(self):
        '''
        Resets the Dino's position, velocity, and jumping state to initial values.

        Places the Dino at its starting position on the ground and ensures
        that all movement attributes are reset for a new game session.
        '''
        self.x = DINO_START_X
        self.y = GROUND_Y - DINO_HEIGHT
        self.velocity_y = 0
        self.jumping = False
        self.ducking = False
        self.height = DINO_HEIGHT
        self.rect.topleft = (self.x, self.y)
