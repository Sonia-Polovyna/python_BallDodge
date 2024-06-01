import sys
import pygame
from BallDodge_SettingsMenu import *


def empty ():
    return


def exit_game():
    pygame.quit()
    sys.exit()


pygame.init()
screen_size = (640, 480)
screen = pygame.display.set_mode(screen_size)

background_color=(0,0,0)


def game():
    running = True
    color = (255, 255, 255)
    paddle_width = 10
    paddle_height = 80
    padding = 50
    paddle_1x = padding
    paddle_1y = screen_size[1] / 2 - paddle_height / 2
    paddle_2x = screen_size[0] - padding
    paddle_2y = paddle_1y
    movement = 5

    ball_radius = 12
    ball_x = screen_size[0] / 2
    ball_y = screen_size[1] / 2
    ball_speed_x = 3
    ball_speed_y = 3
    score = [0, 0]
    score_font = pygame.font.SysFont("Arial", 20)

    clock = pygame.time.Clock()
    #music = pygame.mixer.Sound("Name of the song")
    #music.play(-1)
    while running:
        events = pygame.event.get()
        for event in events:
            if event.type == pygame.QUIT:
                running = False

        keys = pygame.key.get_pressed()
        if keys[pygame.K_w] and paddle_1y > 0:
            paddle_1y = paddle_1y - movement
        if keys[pygame.K_s] and paddle_1y < screen_size[1] - paddle_height:
            paddle_1y = paddle_1y + movement
        if keys[pygame.K_UP] and paddle_2y > 0:
            paddle_2y = paddle_2y - movement
        if keys[pygame.K_DOWN] and paddle_2y < screen_size[1] - paddle_height:
            paddle_2y = paddle_2y + movement
        ball_x = ball_x + ball_speed_x
        ball_y = ball_y + ball_speed_y
        if ball_y < 0 or ball_y > screen_size[1]:
            ball_speed_y = -ball_speed_y
        if ball_x < paddle_1x + paddle_width and ball_y < paddle_1y + paddle_height and paddle_1y < ball_y:
            ball_speed_x = - ball_speed_x
            ball_speed_x += 0.1
        if ball_x > paddle_2x and ball_y < paddle_2y + paddle_height and paddle_2y < ball_y:
            ball_speed_x = - ball_speed_x
            ball_speed_x += 0.1
        if ball_x < 0:
            score[0] +=1
            ball_x = screen_size[0] / 2
            ball_y = screen_size[1] / 2
            ball_speed_x = - ball_speed_x
            ball_speed_x = 3
        if ball_x > screen_size[0]:
            score[1] +=1
            ball_x = screen_size[0] / 2
            ball_y = screen_size[1] / 2
            ball_speed_x = - ball_speed_x
            ball_speed_x = 3

        screen.fill((0, 0, 0))

        pygame.draw.rect(screen, color, (paddle_1x, paddle_1y, paddle_width, paddle_height))
        pygame.draw.rect(screen, color, (paddle_2x, paddle_2y, paddle_width, paddle_height))

        pygame.draw.circle(screen, color, (ball_x, ball_y), ball_radius)

        render_text = score_font.render(f"Score {score[0]}:{score[1]}", True, color)
        screen.blit(render_text, [screen_size[0]/2 - render_text.get_size()[0]/2, screen_size[1]/2-220], )
        pygame.display.flip()
        clock.tick(60)
    pygame.quit()
    sys.exit()


menu_items = ["Start","Settings","Exit"]
menu_items_map = {
    "Start": game ,
    "Settings": settings,
    "Exit": exit_game
}
main_menu_font=pygame.font.Font(None, 36)
text_color = (255, 255, 255)
hover_color = (200, 200, 200)
centerx= 100
centery= 100

def draw_text(text, font, color, screen, centerx, centery):
    text_test = font.render(text, True, color)
    text_field = text_test.get_rect()
    text_field.centerx = centerx
    text_field.centery = centery
    screen.blit(text_test, text_field)
def main_menu():
    while True:
        mx, my = pygame.mouse.get_pos()
        for event in pygame.event.get():
            if event.type==pygame.QUIT:
                pygame.quit()
                sys.exit()
            elif event.type == pygame.MOUSEBUTTONDOWN:
                for i, button in enumerate(menu_items):
                    if screen_size[1] / 2 + 50 * i - 25 < my < screen_size[1] / 2 + 50 * i + 25:
                        menu_items_map[button]()
        screen.fill(background_color)
        for i, button in enumerate(menu_items):
            if screen_size[1]/2+50*i -25 < my < screen_size[1]/2+50*i +25:
                draw_text(button, main_menu_font, hover_color, screen, screen_size[0]/2, screen_size[1]/2+50*i)
            else:
                draw_text(button, main_menu_font, text_color, screen, screen_size[0]/2, screen_size[1]/2 + 50 * i)
        pygame.display.flip()


if __name__ == "__main__":
    main_menu()
