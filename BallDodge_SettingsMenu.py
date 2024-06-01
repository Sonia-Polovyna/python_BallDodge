import sys
import pygame
from BallDodge_menu import main_menu, exit_game, game, empty

pygame.init()
screen_size = (640, 480)
screen = pygame.display.set_mode(screen_size)

background_color=(0,0,0)
settings_items = ["Continue","Restart","Sound","Language","Change player name","Change player color","Write a feedback","Return to menu","Quit"]
main_menu_font=pygame.font.Font(None, 36)
text_color = (255, 255, 255)
centerx= 100
centery= 100
hover_color = (200, 200, 200)
mx, my = pygame.mouse.get_pos()


def draw_text(text, font, color, screen, centerx, centery):
    text_test = font.render(text, True, color)
    text_field = text_test.get_rect()
    text_field.centerx = centerx
    text_field.centery = centery
    screen.blit(text_test, text_field)


def settings():
    while True:
        for event in pygame.event.get():
            if event.type==pygame.QUIT:
                pygame.quit()
                sys.exit()
        screen.fill(background_color)
        for i, button in enumerate(settings_items):
           draw_text(button, main_menu_font, text_color, screen, screen_size[0]/2, 35 + 50*i)
        pygame.display.flip()
        #     if screen_size[1]/2+50*i-25 < my < screen_size[1]/2+50*i+25:
        #         draw_text(button, main_menu_font, hover_color, screen, screen_size[0]/2, 35 + 50*i)
        #     else:
        #         draw_text(button, main_menu_font, text_color, screen, screen_size[0]/2, 35 + 50*i)
        # pygame.display.flip()


menu_items_map = {
    "Continue": game,
    "Restart": empty,
    "Sound": empty,
    "Language": empty,
    "Change player name": empty,
    "Change player color": empty,
    "Write a feedback": empty,
    "Return to menu": main_menu,
    "Quit": exit_game
}


if __name__ == "__main__":
    settings()
