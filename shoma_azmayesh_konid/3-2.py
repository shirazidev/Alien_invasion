import pygame
import sys

# Initialize Pygame
pygame.init()

# Screen dimensions
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption('Space Shooter Shirazidev')

# Colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)

# Player properties
player_width = 50
player_height = 30
player_x = 50
player_y = SCREEN_HEIGHT // 2
player_speed = 5

# Bullet properties
bullet_width = 10
bullet_height = 5
bullet_speed = 7

# Target properties
target_width = 30
target_height = 60
target_x = SCREEN_WIDTH - target_width - 10
target_y = 0
target_speed = 5

# Game variables
bullets = []
misses = 0
game_active = False

# Font
font = pygame.font.Font(None, 36)

def draw_text(text, font, color, surface, x, y):
    text_obj = font.render(text, True, color)
    text_rect = text_obj.get_rect()
    text_rect.center = (x, y)
    surface.blit(text_obj, text_rect)

def reset_game():
    global bullets, misses, player_y, target_y, game_active
    bullets = []
    misses = 0
    player_y = SCREEN_HEIGHT // 2
    target_y = 0
    game_active = True

# Main game loop
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE and game_active:
                bullet_x = player_x + player_width
                bullet_y = player_y + player_height // 2
                bullets.append(pygame.Rect(bullet_x, bullet_y, bullet_width, bullet_height))
        elif event.type == pygame.MOUSEBUTTONDOWN:
            mouse_x, mouse_y = event.pos
            if not game_active and play_button.collidepoint((mouse_x, mouse_y)):
                reset_game()

    keys = pygame.key.get_pressed()
    if keys[pygame.K_UP] and player_y - player_speed > 0:
        player_y -= player_speed
    if keys[pygame.K_DOWN] and player_y + player_height + player_speed < SCREEN_HEIGHT:
        player_y += player_speed

    if game_active:
        # Move target
        target_y += target_speed
        if target_y <= 0 or target_y + target_height >= SCREEN_HEIGHT:
            target_speed = -target_speed

        # Move bullets
        for bullet in bullets:
            bullet.x += bullet_speed
            if bullet.x > SCREEN_WIDTH:
                bullets.remove(bullet)
                misses += 1
                if misses >= 3:
                    game_active = False

        # Check for bullet collisions with target
        for bullet in bullets:
            if bullet.colliderect((target_x, target_y, target_width, target_height)):
                bullets.remove(bullet)
                # Do something if hit, e.g., increase score (not implemented here)

    # Draw everything
    screen.fill(BLACK)
    pygame.draw.rect(screen, WHITE, (player_x, player_y, player_width, player_height))
    pygame.draw.rect(screen, RED, (target_x, target_y, target_width, target_height))
    for bullet in bullets:
        pygame.draw.rect(screen, WHITE, bullet)

    if not game_active:
        play_button = pygame.Rect(SCREEN_WIDTH // 2 - 50, SCREEN_HEIGHT // 2 - 25, 100, 50)
        pygame.draw.rect(screen, WHITE, play_button)
        draw_text('Play', font, BLACK, screen, SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2)

    pygame.display.flip()
    pygame.time.Clock().tick(60)
