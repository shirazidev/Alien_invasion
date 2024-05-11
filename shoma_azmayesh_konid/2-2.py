import pygame
import random

# set screen
WIDTH, HEIGHT = 800, 600
FPS = 30

# stars setting
NUM_STARS = 100
STAR_SIZE = 2
STAR_COLOR = (255, 255, 255)

# pygsmr setting
pygame.init()
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("stars")
clock = pygame.time.Clock()


# a func for randomize star positions
def create_stars():
    stars = []
    for _ in range(NUM_STARS):
        x = random.randint(0, WIDTH)
        y = random.randint(0, HEIGHT)
        stars.append((x, y))
    return stars


# make list of stars in random positions
stars = create_stars()

# game main loop
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # black bg
    screen.fill((0, 0, 0))

    # draw stars
    for star in stars:
        pygame.draw.circle(screen, STAR_COLOR, star, STAR_SIZE)

    # refresh screen
    pygame.display.flip()
    clock.tick(FPS)

pygame.quit()
