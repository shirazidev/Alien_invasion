import pygame
import sys

# code by shirazidev.ir

def run_game():
    # Initialize Pygame
    pygame.init()

    # Set up the screen
    screen = pygame.display.set_mode((800, 600))
    pygame.display.set_caption("Key Events")

# code by shirazidev.ir

    # Main loop
    while True:
        # Handle events
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
            elif event.type == pygame.KEYDOWN:
                # Print the key code when a key is pressed
                print("code dokme feshari:", event.key)

        # Update the display
        pygame.display.flip()

if __name__ == '__main__':
    run_game()
