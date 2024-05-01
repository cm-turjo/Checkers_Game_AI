import pygame.draw

from .constants import RED, WHITE, SQUARE_SIZE,GREY


class Piece:
    PADDING = 10
    OUTLINE = 2

    def __init__(self, row, col, color):
        self.row = row
        self.col = col
        self.color = color
        self.king = False

        if self.color == RED:
            self.direction = 1
        else:
            self.direction = 1
        self.x = 0
        self.y = 0
        self.calc_pos()

    def calc_pos(self):  # Calculate x and y position based on the column that we are in
        self.x = SQUARE_SIZE * self.col + SQUARE_SIZE // 2  # for X co-ordinate
        self.y = SQUARE_SIZE * self.row + SQUARE_SIZE // 2

    def make_king(self):
        self.king = True

    def draw(self, win):
        radius = SQUARE_SIZE // 2 - self.PADDING
        # drawing outline
        pygame.draw.circle(win, GREY, (self.x, self.y), radius + self.OUTLINE)
        pygame.draw.circle(win, self.color, (self.x, self.y), radius)

    def __repr__(self):#internal representation of the object
        return str(self.color)



