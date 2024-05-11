import pygame
import random

# screen settings
WIDTH, HEIGHT = 800, 600
FPS = 30

# rain drrop settings
NUM_RAIN_DROPS = 100
RAIN_DROP_SIZE = 3
RAIN_DROP_COLOR = (150, 150, 255)
MAX_SPEED = 5

# settings of  Pygame
pygame.init()
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("rain")
clock = pygame.time.Clock()

# create rain drop
rain_drops = []
for _ in range(NUM_RAIN_DROPS):
    x = random.randint(0, WIDTH)
    y = random.randint(0, HEIGHT)
    speed = random.randint(1, MAX_SPEED)
    rain_drops.append([x, y, speed])

# main loop
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # bg black
    screen.fill((0, 0, 0))

    # rain drops draw
    for i in range(len(rain_drops)):
        pygame.draw.circle(screen, RAIN_DROP_COLOR, (rain_drops[i][0], rain_drops[i][1]), RAIN_DROP_SIZE)
        rain_drops[i][1] += rain_drops[i][2]  # افزایش موقعیت عمودی قطره باران با سرعت
        if rain_drops[i][1] > HEIGHT:  # اگر قطره باران پایین تر از پنجره باشد
            rain_drops[i][1] = random.randint(-50, 0)  # موقعیت قطره را به بالا بازنشانی می‌کنیم
            rain_drops[i][0] = random.randint(0, WIDTH)  # موقعیت افقی را تصادفی انتخاب می‌کنیم

    # screen refresh
    pygame.display.flip()
    clock.tick(FPS)

pygame.quit()
