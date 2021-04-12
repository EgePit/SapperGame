import pygame as pg


class InputField:
    inactive_color = (190, 190, 192, 255)
    active_color = (255, 255, 255, 255)
    text_color = (0, 0, 0, 0)
    is_active = False
    value = ''

    def __init__(self, screen, label, name, coordinates=(100, 100), width=200, height=32):
        """
        :param screen: window where to draw 
        :param name: field name
        :param coordinates: (x,y) field coordinates
        :param width: field width
        :param height: field height
        """
        self.screen = screen
        self.label = label
        self.name = name
        self.width = width
        self.height = height
        self.main_font = pg.font.Font(None, 32)
        self.label_font = pg.font.Font(None, 25)
        self.input_field = pg.Rect(coordinates, (self.width, self.height))

    def draw(self):
        """
        Field Drawing
        :return: Null
        """
        label_surface = self.label_font.render(self.label, True, self.text_color)
        self.screen.blit(label_surface, (self.input_field.x, self.input_field.y - self.label_font.get_linesize()))

        color = self.active_color if self.is_active else self.inactive_color
        text_surface = self.main_font.render(self.value, True, self.text_color)
        self.width = max(self.width, text_surface.get_width() + 10)
        pg.draw.rect(self.screen, color, self.input_field)
        self.screen.blit(text_surface, (self.input_field.x + 5, self.input_field.y + 5))

    def set_active(self, status):
        """
        :param status: bool set field status
        :return: Null
        """
        self.is_active = status

    def get_status(self):
        return self.is_active

    def type(self, event):
        """
        Changing field text
        :param event: pygame keydown event
        :return: Null
        """
        if event.key == pg.K_BACKSPACE:
            self.value = self.value[:-1]
        else:
            self.value += event.unicode

