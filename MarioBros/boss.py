import pygame
from config import BOSS_HEALTH, BOSS_HEIGHT, BOSS_START_X, BOSS_START_Y, BOSS_WIDTH

class Boss:
    '''
    Represents the Boss that appears at specific intervals.
    '''

    def __init__(self):
        self.x = BOSS_START_X
        self.y = BOSS_START_Y+20
        self.width = BOSS_WIDTH
        self.height = BOSS_HEIGHT
        self.health = BOSS_HEALTH
        self.defeated = False

        # Load and scale boss image
        self.image = pygame.image.load("assets/boss.png")
        self.image = pygame.transform.scale(self.image, (self.width, self.height))

        # Create a collision rectangle
        self.rect = self.image.get_rect(topleft=(self.x, self.y))


    def is_off_screen(self):
        '''
        Checks if the boss has moved off the screen.
        '''
        return self.x + self.rect.width < 0
    

    def update(self, speed):
        '''
        Moves the boss across the screen unless defeated.
        @param speed: The current game speed.
        '''
        if not self.defeated:
            self.x -= speed
            self.rect.x = self.x  # Update collision rectangle position


    def take_damage(self):
        '''
        Marks the boss as defeated.
        '''
        self.defeated = True


    def draw(self, screen):
        '''
        Renders the Boss on the game screen.
        @param screen The Pygame screen where the Boss is rendered.
        '''
        screen.blit(self.image, (self.x, self.y))