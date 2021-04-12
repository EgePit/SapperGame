import pygame as pg
from PlayField import *
from InputField import *


def init_game():
    print(1)
    width, height, mines = ask_settings()
    print(width, height, mines)
    # play_field = PlayField(width, height, mines)


def ask_settings():
    settings_screen = pg.display.set_mode((400, 200))
    settings_screen.fill((180, 180, 180))
    # width_input = pg.Rect(100, 100, 140, 32)
    # inactive_color = pg.Color('gray')
    # active_color = pg.Color('white')
    # font = pg.font.Font(None, 32)
    # width_value = ''

    width_input = InputField(settings_screen, 'Field width', 'width', (100, 25))
    height_input = InputField(settings_screen, 'Field height', 'height', (100, 80))
    mines_input = InputField(settings_screen, 'Mines', 'mines', (100, 130))

    clock = pg.time.Clock()
    running = True
    active = False
    while running:
        for event in pg.event.get():
            # clock.tick(30)
            if event.type == pg.QUIT:
                running = False
                if event.type == pg.MOUSEBUTTONDOWN:
                    if width_input.input_field.collidepoint(event.pos):
                        width_input.set_active(True)
                    else:
                        width_input.set_active(False)

                    if height_input.input_field.collidepoint(event.pos):
                        height_input.set_active(True)
                    else:
                        height_input.set_active(False)

                    if mines_input.input_field.collidepoint(event.pos):
                        mines_input.set_active(True)
                    else:
                        mines_input.set_active(False)
            # if event.type == pg.KEYDOWN:
            #     if active:
            #         if event.key == pg.K_BACKSPACE:
            #             width_value = width_value[:-1]
            #         else:
            #             print(type(event.unicode))
            #             width_value += event.unicode

        # color = active_color if active else inactive_color
        # width_surface = font.render(width_value, True, pg.Color('black'))
        # width = max(200, width_surface.get_width()+10)
        # width_input.w = width
        # pg.draw.rect(settings_screen, color, width_input)
        # settings_screen.blit(width_surface, (width_input.x + 5, width_input.y + 5))
        width_input.draw()
        height_input.draw()
        mines_input.draw()
        pg.display.flip()

    return (1, 2, 3)
    # return (width, height, mines)


if __name__ == '__main__':
    pg.init()
    init_game()
    # pg.quit()
