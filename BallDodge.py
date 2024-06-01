import sys
import pygame

pygame.init()
screen_size = (640, 480)
screen = pygame.display.set_mode(screen_size)

pygame.display.set_caption("New game")

running = True
color = (255, 255, 255)
paddle_width = 10
paddle_height = 80
padding = 50
paddle_1x = padding
paddle_1y = screen_size[1]/2 - paddle_height/2
paddle_2x = screen_size[0] - padding
paddle_2y = paddle_1y
movement = 5

ball_radius = 12
ball_x = screen_size[0]/2
ball_y = screen_size[1]/2
ball_speed_x = 5
ball_speed_y = 5

clock = pygame.time.Clock()
while running:
    events = pygame.event.get()
    for event in events:
        if event.type == pygame.QUIT:
            running = False

    keys = pygame.key.get_pressed()
    if keys[pygame.K_w] and paddle_1y>0:
        paddle_1y = paddle_1y - movement
    if keys[pygame.K_s] and paddle_1y<screen_size[1]-paddle_height:
        paddle_1y = paddle_1y + movement
    if keys[pygame.K_UP] and paddle_2y>0:
        paddle_2y = paddle_2y - movement
    if keys[pygame.K_DOWN] and paddle_2y<screen_size[1]-paddle_height:
        paddle_2y = paddle_2y + movement
    ball_x = ball_x + ball_speed_x
    ball_y = ball_y + ball_speed_y
    if ball_y < 0 or ball_y > screen_size[1]:
        ball_speed_y = -ball_speed_y
    if ball_x < paddle_1x + paddle_width and ball_y < paddle_1y + paddle_height and paddle_1y < ball_y:
        ball_speed_x = - ball_speed_x
    if ball_x > paddle_2x and ball_y < paddle_2y + paddle_height and paddle_2y < ball_y:
        ball_speed_x = - ball_speed_x
    screen.fill((0, 0, 0))

    pygame.draw.rect(screen, color, (paddle_1x, paddle_1y, paddle_width, paddle_height))
    pygame.draw.rect(screen, color, (paddle_2x, paddle_2y, paddle_width, paddle_height))

    pygame.draw.circle(screen, color, (ball_x, ball_y), ball_radius)

    pygame.display.flip()
    clock.tick(60)
pygame.quit()
sys.exit()