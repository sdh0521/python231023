# 블럭깨기2.py
import pygame
import random

# 초기화
pygame.init()

# 화면 설정
screen_width = 800
screen_height = 600
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("블록 깨기 게임")

# 색깔
white = (255, 255, 255)
blue = (0, 0, 255)

# 패들 설정
paddle_width = 100
paddle_height = 10
paddle_x = (screen_width - paddle_width) // 2
paddle_y = screen_height - paddle_height - 20
paddle_speed = 10

# 공 설정
ball_radius = 10
ball_x = screen_width // 2
ball_y = screen_height // 2
ball_speed_x = 7 * random.choice((1, -1))
ball_speed_y = 7

# 블록 설정
block_width = 100
block_height = 30
block_rows = 5
block_cols = 8
blocks = []

for row in range(block_rows):
    for col in range(block_cols):
        block = pygame.Rect(col * block_width, row * block_height, block_width, block_height)
        blocks.append(block)

# 게임 오버 여부
game_over = False

# 게임 루프
while not game_over:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            game_over = True

    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT] and paddle_x > 0:
        paddle_x -= paddle_speed
    if keys[pygame.K_RIGHT] and paddle_x < screen_width - paddle_width:
        paddle_x += paddle_speed

    # 화면 업데이트
    screen.fill(white)

    # 공 이동
    ball_x += ball_speed_x
    ball_y += ball_speed_y

    # 공과 화면 경계 체크
    if ball_x <= ball_radius or ball_x >= screen_width - ball_radius:
        ball_speed_x = -ball_speed_x
    if ball_y <= ball_radius:
        ball_speed_y = -ball_speed_y

    # 패들과 공 충돌
    if (paddle_x < ball_x < paddle_x + paddle_width) and (paddle_y < ball_y + ball_radius):
        ball_speed_y = -ball_speed_y

    # 블록과 공 충돌
    for block in blocks[:]:
        if block.colliderect((ball_x - ball_radius, ball_y - ball_radius, 2 * ball_radius, 2 * ball_radius)):
            blocks.remove(block)
            ball_speed_y = -ball_speed_y

    # 게임 화면 그리기
    pygame.draw.rect(screen, blue, (paddle_x, paddle_y, paddle_width, paddle_height))
    pygame.draw.circle(screen, blue, (int(ball_x), int(ball_y)), ball_radius)
    for block in blocks:
        pygame.draw.rect(screen, blue, block)

    pygame.display.flip()

    # 블록을 모두 깼을 경우
    if not blocks:
        game_over = True

# 게임 종료
pygame.quit()
