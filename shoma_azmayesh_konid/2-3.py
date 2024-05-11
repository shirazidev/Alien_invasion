import pygame
import random

# تنظیمات پنجره
WIDTH, HEIGHT = 800, 600
FPS = 30

# تنظیمات قطرات باران
NUM_RAIN_DROPS = 50
RAIN_DROP_SIZE = 3
RAIN_DROP_COLOR = (150, 150, 255)
MAX_SPEED = 5

# تنظیمات Pygame
pygame.init()
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("باران")
clock = pygame.time.Clock()

# ایجاد قطرات باران
rain_drops = []
for _ in range(NUM_RAIN_DROPS):
    x = random.randint(0, WIDTH)
    y = random.randint(-50, 0)  # شروع از بالای صفحه
    speed = random.randint(1, MAX_SPEED)
    rain_drops.append([x, y, speed])

# حلقه اصلی برنامه
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # پس زمینه را پاک می‌کنیم
    screen.fill((0, 0, 0))

    # رسم قطرات باران
    all_drops_at_bottom = True  # شرطی برای بررسی اینکه آیا همه قطرات باران به پایین صفحه رسیده‌اند یا خیر
    for i in range(len(rain_drops)):
        pygame.draw.circle(screen, RAIN_DROP_COLOR, (rain_drops[i][0], rain_drops[i][1]), RAIN_DROP_SIZE)
        rain_drops[i][1] += rain_drops[i][2]  # افزایش موقعیت عمودی قطره باران با سرعت
        if rain_drops[i][1] <= HEIGHT:  # اگر حداقل یک قطره باران هنوز به پایین صفحه نرسیده باشد
            all_drops_at_bottom = False  # تغییر متغیر شرطی
    if all_drops_at_bottom:  # اگر همه قطرات باران به پایین صفحه رسیده باشند
        running = False  # برنامه را قطع می‌کنیم

    # بروزرسانی صفحه
    pygame.display.flip()
    clock.tick(FPS)

pygame.quit()
