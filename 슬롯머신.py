# 슬롯머신 게임

import pygame
import random
import time

# 초기화
pygame.init()

# 화면 설정
screen_width = 600
screen_height = 400
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("슬롯 머신 게임")

# 색깔
white = (255, 255, 255)
black = (0, 0, 0)

# 아이콘 설정
icon_width = 100
icon_height = 100
icon_x = [100, 250, 400]
icon_y = screen_height // 2 - icon_height // 2
icons = ["cherry.png", "lemon.png", "orange.png", "plum.png", "bell.png", "bar.png", "seven.png"]

# 게임 관련 변수
spin_duration = 3
spinning = False
result = [0, 0, 0]

# 이미지 로드
images = []
for icon in icons:
    image = pygame.image.load(icon)
    image = pygame.transform.scale(image, (icon_width, icon_height))
    images.append(image)

# 게임 루프
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    keys = pygame.key.get_pressed()
    if keys[pygame.K_SPACE] and not spinning:
        spinning = True
        result = [random.randint(0, len(icons) - 1) for _ in range(3)]
        spin_start_time = time.time()

    # 화면 업데이트
    screen.fill(white)

    if spinning and time.time() - spin_start_time < spin_duration:
        # 슬롯이 돌아가는 중
        for i in range(3):
            icon_index = (result[i] + int(time.time() * 10)) % len(icons)
            screen.blit(images[icon_index], (icon_x[i], icon_y))
    else:
        # 결과 표시
        for i in range(3):
            screen.blit(images[result[i]], (icon_x[i], icon_y))

        # 슬롯 머신 정지
        spinning = False

    pygame.display.flip()

# 게임 종료
pygame.quit()
