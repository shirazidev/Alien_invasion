import pygame

# screen settings
WIDTH, HEIGHT = 800, 600
FPS = 30

# stars settings
NUM_ROWS = 10
NUM_COLS = 10
STAR_SIZE = 2
STAR_COLOR = (255, 255, 255)
HORIZONTAL_SPACING = WIDTH // NUM_COLS
VERTICAL_SPACING = HEIGHT // NUM_ROWS

# pygame settings
pygame.init()
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("ستاره ها")
clock = pygame.time.Clock()

# main loop
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # black bg
    screen.fill((0, 0, 0))

    # draw stars
    for row in range(NUM_ROWS):
        for col in range(NUM_COLS):
            x = col * HORIZONTAL_SPACING + HORIZONTAL_SPACING // 2
            y = row * VERTICAL_SPACING + VERTICAL_SPACING // 2
            pygame.draw.circle(screen, STAR_COLOR, (x, y), STAR_SIZE)

    # refresh screen
    pygame.display.flip()
    clock.tick(FPS)

pygame.quit()
