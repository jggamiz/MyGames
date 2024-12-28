import pygame
from config import FIREBALL_HEIGHT, FIREBALL_SPEED, FIREBALL_WIDTH, SCREEN_WIDTH

class Fireball:
    '''
    Represents a fireball projectile.
    '''
    def __init__(self, x, y):
        '''
        Initializes the fireball's position and movement.
        '''
        self.x = x
        self.y = y
        self.speed = FIREBALL_SPEED
        self.image = pygame.image.load("assets/fireball.png")
        self.image = pygame.transform.scale(self.image, (FIREBALL_WIDTH, FIREBALL_HEIGHT))
        self.rect = self.image.get_rect(topleft=(self.x, self.y))

    def update(self):
        '''
        Moves the fireball to the right.
        '''
        self.x += self.speed
        self.rect.x = self.x

    def is_off_screen(self):
        '''
        Checks if the fireball has moved off-screen.
        '''
        return self.x > SCREEN_WIDTH

    def draw(self, screen):
        '''
        Draws the fireball on the screen.
        @param screen: The Pygame screen where the fireball is rendered.
        '''
        screen.blit(self.image, (self.x, self.y))
