import pygame
from game_manager import GameManager
from config import SCREEN_WIDTH, SCREEN_HEIGHT

def main():
    # Initialize Pygame
    pygame.init()
    
    # Set up the display
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    pygame.display.set_caption("Mario Bros")

    # Create a GameManager instance to control the game
    game_manager = GameManager()

    # Main game loop
    clock = pygame.time.Clock()

    while True:
        # Handle events (user input, quit event, etc.)
        game_manager.handle_events()

        # Update the game state (dinosaur, obstacles, collisions)
        game_manager.update()

        # Draw the game components to the screen
        game_manager.draw(screen)

        # Update the screen with the latest drawing
        pygame.display.flip()

        # Cap the frame rate to 60 FPS
        clock.tick(60)

# Run the game
if __name__ == "__main__":
    main()
