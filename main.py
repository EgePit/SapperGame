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
    fields = {}
    fields['width'] = InputField(settings_screen, 'Field width', 'width', (100, 25))
    fields['height'] = InputField(settings_screen, 'Field height', 'height', (100, 80))
    fields['mines'] = InputField(settings_screen, 'Mines', 'mines', (100, 130))

    clock = pg.time.Clock()
    running = True
    while running:
        for event in pg.event.get():
            clock.tick(60)
            if event.type == pg.QUIT:
                running = False
            if event.type == pg.MOUSEBUTTONDOWN:
                for field in fields:
                    if fields[field].input_field.collidepoint(event.pos):
                        fields[field].set_active(True)
                    else:
                        fields[field].set_active(False)
            if event.type == pg.KEYDOWN:
                for field in fields:
                    if fields[field].get_status():
                        fields[field].type(event)
        for field in fields:
            fields[field].draw()
        pg.display.flip()

    return (1, 2, 3)
    # return (width, height, mines)


if __name__ == '__main__':
    pg.init()
    init_game()
    # pg.quit()
