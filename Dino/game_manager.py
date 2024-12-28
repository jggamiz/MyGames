import pygame, time, random
from dino import Dino
from obstacle import Obstacle
from config import SCREEN_WIDTH, SCREEN_HEIGHT, WHITE, BLACK, GREEN, SKY_COLOR, FONT_SIZE, SCORE_INCREMENT, INITIAL_SPEED, SPEED_INC, MAX_SPEED, GROUND_Y


class GameManager:

    '''
    Manages the overall game flow, including updates, rendering, and resetting.
    '''

    def __init__(self):
        '''
        Initializes the GameManager, setting up the Dino, obstacles, score, and game state.
        '''
        self.dino = Dino()
        self.obstacle = Obstacle()
        self.score = 0
        self.game_active = True
        self.speed = INITIAL_SPEED

        # Now let's set some customized font style and size
        pygame.font.init()
        self.score_font = pygame.font.Font(None, FONT_SIZE)
        self.game_over_font = pygame.font.Font(None, FONT_SIZE*2-8) 


    def run_game_loop(self):
        '''
        Starts the main game loop, handling events, updates, and rendering
        '''
        while True:
            self.handle_events()
            if self.game_active:
                self.update()
                self.draw()
            pygame.display.flip()


    def update(self):
        '''
        Updates the game state, including the Dino, obstacles, and score.
        Checks for collisions and adjusts the game speed dynamically.
        '''
        if self.game_active:
            self.dino.update()
            self.obstacle.update(self.speed)

            if self.dino.rect.colliderect(self.obstacle.rect):
                self.game_active = False
            
            if self.obstacle.rect.right + self.obstacle.rect.width < 0:
                self.obstacle.reset()  # Reset the obstacle's position
                self.speed += SPEED_INC  # Increase speed
                self.score += SCORE_INCREMENT  # Increment score

            # Limit max speed to avoid it becoming unmanageable
            self.speed = min(self.speed, MAX_SPEED)


    def draw(self, screen):
        '''
        Renders the game screen, including the Dino, obstacles, and UI.
        '''
        # First Background
        screen.fill(WHITE) # White background
        pygame.draw.line(screen, (BLACK), (0, GROUND_Y), (SCREEN_WIDTH, GROUND_Y), 5)

        #screen.fill(SKY_COLOR, (0, 0, SCREEN_WIDTH, GROUND_Y))
        #screen.fill(GREEN, (0, GROUND_Y, SCREEN_WIDTH, SCREEN_HEIGHT - GROUND_Y))

        # Draw the dinosaur and obstacles
        self.dino.draw(screen)
        self.obstacle.draw(screen)

        if self.game_active: self.show_score(screen)
        else: self.show_game_over(screen)

        pygame.display.flip()


    def handle_events(self):
        '''
        Handles user inputs, including jumping, ducking, and resetting the game.
        '''
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                exit()

            if self.game_active:
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_SPACE or event.key == pygame.K_UP:
                        self.dino.jump()
                    elif event.key == pygame.K_DOWN:
                        self.dino.duck()
                elif event.type == pygame.KEYUP:
                    if event.key == pygame.K_DOWN:
                        self.dino.stand_up()
            else:
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_r:
                        # If "R" is pressed, reset the game
                        self.reset()
                    elif event.key == pygame.K_ESCAPE:
                        # Exit the game if ESC is pressed
                        pygame.quit()
                        exit()


    def reset(self):
        '''
        Resets the game to its initial state.
        '''
        self.dino.reset()
        self.obstacle.reset()
        
        self.score = 0
        self.game_active = True
        self.speed = INITIAL_SPEED

    
    def show_score(self, screen):
        '''
        Displays the current score on the game screen.
        @param screen The Pygame screen where the score is rendered.
        '''
        score_txt = self.score_font.render(f"Score: {self.score}", True, BLACK)
        screen.blit(score_txt, (10,10))


    def show_game_over(self, screen):
        '''
        Displays the game-over screen with the final score and instructions.
        @param screen The Pygame screen where the game-over message is rendered.
        '''
        # Display "Game Over" text
        game_over_txt = self.game_over_font.render("Game Over", True, (200, 0, 0))
        screen.blit(game_over_txt, (SCREEN_WIDTH // 2 - game_over_txt.get_width() // 2, SCREEN_HEIGHT // 3))
        
        # Display the obtained score
        score_txt = self.score_font.render(f"Score: {self.score}", True, BLACK)
        screen.blit(score_txt, (SCREEN_WIDTH // 2 - score_txt.get_width() // 2, SCREEN_HEIGHT // 3 + 65))
        
        # Display the instruction to restart
        instruction_text = self.score_font.render("Press R to Restart", True, (100, 100, 100))
        screen.blit(instruction_text, (SCREEN_WIDTH // 2 - instruction_text.get_width() // 2, SCREEN_HEIGHT // 3 + 100))
