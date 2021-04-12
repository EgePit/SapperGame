class PlayField:
    width = 10
    height = 10
    mines = 10


    def __init__(self, screen, width, height, mines):
        """
        :param width: field width in cells
        :param height: field height in cells
        :param mines: mines amount on field
        """
        self.width = width
        self.height = height
        self.mines = mines

