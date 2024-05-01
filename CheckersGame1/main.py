import pygame
from checkers.constants import WIDTH, HEIGHT
from checkers.board import Board
FPS = 60
WIN = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Checkers")


def main():
    run = True
    clock = pygame.time.Clock()  # For setting Running Refresh Rate of the game
    board= Board()
    while run:
        clock.tick(FPS)  # Game Refreshrate->60

        for event in pygame.event.get():  # For checking any event is happening at current time
            if event.type == pygame.QUIT:
                run = False
            if event.type == pygame.MOUSEBUTTONDOWN:
                pass
        board.draw_squares(WIN)
        pygame.display.update()
    pygame.quit()

main()
