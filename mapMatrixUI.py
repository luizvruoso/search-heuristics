import time

import pygame
import copy

ACTUAL_POSITION = 999999
TARGET_POSITION = -9999


class Map:
    def __init__(self):
        self.WINDOW_SIZE = [505, 530]
        self.GREEN = (151, 224, 103)
        self.BLUE = (84, 194, 234)
        self.RED = (201, 94, 82)
        self.BROWN = (119, 93, 68)
        self.WHITE = (255, 250, 250)
        self.BLACK = (0, 0, 0)
        self.DARK_GREY = (56, 56, 56)
        self.PINK = (255, 112, 252)

    def screen(self, matrix, searchParams, arrayColorActualPosition, arrayColorFinalResult, arrayColorFrontier):

        initialPosition = searchParams.getInitialPosition()
        finishPosition = searchParams.getTargetPosition()

        arrayColorFinalResult.append(initialPosition.getActualPosition())

        # OPCAO PARA HEURISTICA DE RALO
        # matrix.sketchMatrix[finishPosition.getX()][finishPosition.getY()] = TARGET_POSITION

        grid = copy.deepcopy(matrix.sketchMatrix)
        pygame.init()

        WIDTH = 11
        HEIGHT = 11

        MARGIN = 1

        screen = pygame.display.set_mode(self.WINDOW_SIZE)
        pygame.display.set_caption("D.A.T.A")
        done = False

        pygame.font.init()
        font = pygame.font.SysFont('Arial MT Light', 23)

        x = font.render("Número de pops: ", True, self.WHITE)
        y = font.render("Custo total: ", True, self.WHITE)
        z = font.render("Tempo total: ", True, self.WHITE)

        screen.blit(x, (5, 510))
        screen.blit(y, (200, 510))
        screen.blit(z, (350, 510))

        clock = pygame.time.Clock()

        while not done:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    done = True

            for row in range(matrix.getSizeX()):
                for column in range(matrix.getSizeY()):
                    if grid[row][column] == TARGET_POSITION:
                        color = self.BLACK
                    if grid[row][column] == 1:
                        color = self.GREEN
                    elif grid[row][column] == 2:
                        color = self.BROWN
                    elif grid[row][column] == 3:
                        color = self.BLUE
                    elif grid[row][column] == 4:
                        color = self.RED

                    pygame.draw.rect(screen, color,
                                     [(MARGIN + WIDTH) * column + MARGIN,
                                      (MARGIN + HEIGHT) * row + MARGIN,
                                      WIDTH,
                                      HEIGHT])

            for row in arrayColorFinalResult:
                color = self.WHITE
                pygame.draw.rect(screen, color,
                                 [(MARGIN + WIDTH) * row[1] + MARGIN,
                                  (MARGIN + HEIGHT) * row[0] + MARGIN,
                                  WIDTH,
                                  HEIGHT])

            for row in arrayColorFrontier:
                color = self.DARK_GREY
                pygame.draw.rect(screen, color,
                                 [(MARGIN + WIDTH) * row[1] + MARGIN,
                                  (MARGIN + HEIGHT) * row[0] + MARGIN,
                                  WIDTH,
                                  HEIGHT])

            for row in arrayColorActualPosition:
                color = self.PINK
                pygame.draw.rect(screen, color,
                                 [(MARGIN + WIDTH) * row[1] + MARGIN,
                                  (MARGIN + HEIGHT) * row[0] + MARGIN,
                                  WIDTH,
                                  HEIGHT])

            font = pygame.font.SysFont("Comic Sans MS", 15)

            x1 = font.render(str(searchParams.getNumberOfPops()), True, self.WHITE)
            x2 = font.render(str(searchParams.getTotalCost()), True, self.WHITE)
            x3 = font.render(str(searchParams.getTotalTime()), True, self.WHITE)
            print(searchParams.getNumberOfPops())
            print(searchParams.getTotalCost())
            screen.blit(x1, (140, 510))
            screen.blit(x2, (300, 510))
            screen.blit(x3, (450, 510))
            pygame.display.update()

            clock.tick(10)
            pygame.display.flip()

        pygame.quit()
