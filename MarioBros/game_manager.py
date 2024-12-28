import pygame, random
from pygame import mixer
from dino import Dino
from obstacle import Obstacle
from boss import Boss
from potion import Potion
from config import SCREEN_WIDTH, SCREEN_HEIGHT, BLACK, GREEN, FONT_SIZE, INITIAL_SPEED, GROUND_Y, POTION_DISPLAY_X, POTION_DISPLAY_Y


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
        self.speed = INITIAL_SPEED
        self.boss = None
        self.fireballs = []
        self.potions = []
        self.game_active = True

        # Set customized font style and size
        pygame.font.init()
        self.score_font = pygame.font.Font(None, FONT_SIZE)
        self.game_over_font = pygame.font.Font(None, FONT_SIZE * 2 - 8)

        self.spawn_potions()

        # Load background image
        self.background_image = pygame.image.load("assets/background.jpg")
        self.background_image = pygame.transform.scale(self.background_image, (SCREEN_WIDTH, SCREEN_HEIGHT))

        # Initialize the mixer for sounds
        mixer.init()

        # Load all sounds
        self.sounds = {
            "dino_death": mixer.Sound("assets/mario_dies.wav"),
            "jump": mixer.Sound("assets/jump.wav"),
            "fireball": mixer.Sound("assets/fireball.wav"),
            "boss_defeated": mixer.Sound("assets/bowser_dies.wav"),
            "potion": mixer.Sound("assets/good_potion.wav"),
            "poison": mixer.Sound("assets/bad_potion.wav"),
            "mamma_mia": mixer.Sound("assets/mamma_mia.mp3")
        }

        # Set initial volumes
        self.set_global_volume(0.5)


    def spawn_potions(self):
        '''
        Dynamically spawns potions or poisons during a 10-point interval, ensuring no more than two appear.
        '''
        # Check if fewer than 1 potions/poisons are active
        if len(self.potions) < 1:
            # Randomize potion/poison spawning based on score
            if random.randint(0, 100) < 10:  # 10% chance to spawn per frame
                obstacles = [self.obstacle] if self.obstacle else []
                potion = Potion(obstacles)
                self.potions.append(potion)

    def run_game_loop(self):
        '''
        Starts the main game loop, handling events, updates, and rendering.
        '''
        while True:
            self.handle_events()
            if self.game_active:
                self.update()
                self.draw()
            pygame.display.flip()


    def update(self):
        if self.game_active:  # Only update game logic if the game is active
            # Check if it's a boss level
            if not self.boss and self.score > 0 and self.score % 10 == 0:
                self.boss = Boss()  # Initialize the boss
                self.obstacle = None  # Temporarily disable regular obstacles
            
            # Handle boss level
            if self.boss:
                self.boss.update(self.speed)
                
                # If the boss is defeated and moves off-screen, remove it
                if self.boss.defeated:
                    self.boss = None  # Remove the boss
                    self.sounds["boss_defeated"].play()
                    self.score += 1
                    self.obstacle = Obstacle()  # Resume obstacles
                    return
                
                # If the dino collides with the boss, game over
                if not self.boss.defeated and self.dino.rect.colliderect(self.boss.rect):
                    self.sounds["dino_death"].play()
                    self.game_active = False  # End the game
                    return
            
            # Handle fireballs
            for fireball in self.fireballs[:]:
                fireball.update()
                if fireball.is_off_screen():
                    self.fireballs.remove(fireball)
                elif self.boss and fireball.rect.colliderect(self.boss.rect):
                    self.boss.defeated = True
                    self.fireballs.remove(fireball)
            
            # Update regular gameplay elements if no boss exists
            if not self.boss:
                self.dino.update()
                self.obstacle.update(self.speed)

                # Check collision with obstacle
                if self.obstacle and self.dino.rect.colliderect(self.obstacle.rect):
                    self.sounds["dino_death"].play()
                    self.game_active = False  # End the game
                    return

                # Increment score and reset obstacle if it goes off-screen
                if self.obstacle and self.obstacle.x + self.obstacle.rect.width < 0:
                    self.score += 1
                    self.obstacle.reset()
            
            self.spawn_potions()  # Dynamically spawn potions or poisons
            for potion in self.potions[:]:
                potion.update(self.speed)
                if potion.is_off_screen():
                    self.potions.remove(potion)
                elif self.dino.rect.colliderect(potion.rect):
                    if potion.is_potion: 
                        self.dino.potions += 1
                        self.sounds["potion"].play()
                    else: 
                        self.dino.potions = max(0, self.dino.potions - 2)
                        self.sounds["poison"].play()
                    self.potions.remove(potion)


    def draw(self, screen):
        '''
        Renders the game screen, including the Dino, obstacles, and UI.
        @param screen The Pygame screen where the elements are rendered.
        '''

        # Background rendering
        #screen.fill(SKY_COLOR)
        screen.blit(self.background_image, (0, 0))
        pygame.draw.rect(screen, GREEN, (0, GROUND_Y, SCREEN_WIDTH, SCREEN_HEIGHT - GROUND_Y))


        # Draw Dino, obstacle, boss, and potions
        self.dino.draw(screen)
        if self.obstacle:
            self.obstacle.draw(screen)
        if self.boss:
            self.boss.draw(screen)
        for potion in self.potions:
            potion.draw(screen)
        for fireball in self.fireballs:
            fireball.draw(screen)

        # Display score and potion count
        self.show_score(screen)
        self.show_potion_count(screen)

        if not self.game_active:
            self.show_game_over(screen)

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
                        self.sounds["jump"].play()
                    elif event.key == pygame.K_DOWN:
                        self.dino.duck()
                    elif event.key == pygame.K_f:
                        self.dino.spit_fire(self.fireballs)
                        self.sounds["fireball"].play()
                    elif event.key == pygame.K_m:
                        self.sounds["mamma_mia"].play()
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
        self.obstacle = Obstacle()  # Reset obstacle
        self.boss = None  # Reset the boss
        self.score = 0
        self.speed = INITIAL_SPEED
        self.game_active = True
        self.potions = []  # Clear existing potions
        self.spawn_potions()

    def show_score(self, screen):
        '''
        Displays the current score on the game screen.
        @param screen The Pygame screen where the score is rendered.
        '''
        score_txt = self.score_font.render(f"Score: {self.score}", True, BLACK)
        screen.blit(score_txt, (10, 10))


    def show_game_over(self, screen):
        '''
        Displays the game-over screen with the final score and instructions.
        @param screen The Pygame screen where the game-over message is rendered.
        '''
        game_over_txt = self.game_over_font.render("Game Over", True, (200, 0, 0))
        screen.blit(game_over_txt, (SCREEN_WIDTH // 2 - game_over_txt.get_width() // 2, SCREEN_HEIGHT // 3))

        score_txt = self.score_font.render(f"Score: {self.score}", True, BLACK)
        screen.blit(score_txt, (SCREEN_WIDTH // 2 - score_txt.get_width() // 2, SCREEN_HEIGHT // 3 + 65))

        instruction_text = self.score_font.render("Press R to Restart", True, (100, 100, 100))
        screen.blit(instruction_text, (SCREEN_WIDTH // 2 - instruction_text.get_width() // 2, SCREEN_HEIGHT // 3 + 100))


    def show_potion_count(self, screen):
        '''
        Displays the number of potions available for the player.
        @param screen The Pygame screen where the potion count is rendered.
        '''
        potion_text = self.score_font.render(f"Potions: {self.dino.potions}", True, BLACK)
        screen.blit(potion_text, (POTION_DISPLAY_X, POTION_DISPLAY_Y))


    def set_global_volume(self, volume):
        '''
        Sets the volume for all game sounds.
        @param volume The volume level (0.0 to 1.0).
        '''
        for sound in self.sounds.values():
            sound.set_volume(volume)