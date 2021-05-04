import time
import json

import pygame
import copy

ACTUAL_POSITION = 999999
TARGET_POSITION = -9999


class Map:
    def __init__(self):
        self.WINDOW_SIZE = [505, 550]
        self.GREEN = (151, 224, 103)
        self.BLUE = (84, 194, 234)
        self.RED = (201, 94, 82)
        self.BROWN = (119, 93, 68)
        self.WHITE = (255, 250, 250)
        self.BLACK = (0, 0, 0)
        self.DARK_GREY = (56, 56, 56)
        self.PINK = (255, 112, 252)
        self.WIDTH = 11
        self.HEIGHT = 11
        self.MARGIN = 1

    def screen(self, matrix, searchParams, arrayColorActualPosition, arrayColorFinalResult, arrayColorFrontier):
        with open('./properties/configs.json') as json_file:
            data = json.load(json_file)
            self.WINDOW_SIZE = data['general']['pygame']['WINDOW_SIZE']
            self.WIDTH = data['general']['pygame']['WIDTH']
            self.HEIGHT = data['general']['pygame']['HEIGHT']
            self.MARGIN = data['general']['pygame']['MARGIN']

        initialPosition = searchParams.getInitialPosition()
        finishPosition = searchParams.getTargetPosition()

        arrayColorFinalResult.append(initialPosition.getActualPosition())

        # OPCAO PARA HEURISTICA DE RALO
        #matrix.sketchMatrix[finishPosition.getX()][finishPosition.getY()] = TARGET_POSITION

        grid = copy.deepcopy(matrix.sketchMatrix)
        grid[initialPosition.actualPosition[0]][initialPosition.actualPosition[1]] = TARGET_POSITION
        pygame.init()

        #WIDTH = 11
        #HEIGHT = 11

        #MARGIN = 1



        screen = pygame.display.set_mode(self.WINDOW_SIZE)
        screen.fill(self.DARK_GREY)
        pygame.display.set_caption("D.A.T.A")
        done = False

        pygame.font.init()
        font = pygame.font.SysFont('Arial MT Light', 18)

        x = font.render("Número de pops: ", True, self.WHITE)
        y = font.render("Custo total: ", True, self.WHITE)
        z = font.render("Tempo total: ", True, self.WHITE)

        screen.blit(x, (20, 520))
        screen.blit(y, (180, 520))
        screen.blit(z, (310, 520))

        clock = pygame.time.Clock()

        while not done:
            pygame.draw.rect(screen, self.DARK_GREY, [125, 520, 50, 20], 0)
            pygame.draw.rect(screen, self.DARK_GREY, [255, 520, 50, 20], 0)
            pygame.draw.rect(screen, self.DARK_GREY, [390, 520, 100, 20], 0)

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    done = True


            for row in range(matrix.getSizeY()):
                for column in range(matrix.getSizeX()):
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
                                     [(self.MARGIN + self.WIDTH) * column + self.MARGIN,
                                      (self.MARGIN + self.HEIGHT) * row + self.MARGIN,
                                      self.WIDTH,
                                      self.HEIGHT])

            for row in arrayColorFinalResult:
                color = self.WHITE
                pygame.draw.rect(screen, color,
                                 [(self.MARGIN + self.WIDTH) * row[1] + self.MARGIN,
                                  (self.MARGIN + self.HEIGHT) * row[0] + self.MARGIN,
                                  self.WIDTH,
                                  self.HEIGHT])

            for row in arrayColorFrontier:
                color = self.DARK_GREY
                pygame.draw.rect(screen, color,
                                 [(self.MARGIN + self.WIDTH) * row[1] + self.MARGIN,
                                  (self.MARGIN + self.HEIGHT) * row[0] + self.MARGIN,
                                  self.WIDTH,
                                  self.HEIGHT])

            for row in arrayColorActualPosition:
                color = self.PINK
                pygame.draw.rect(screen, color,
                                 [(self.MARGIN + self.WIDTH) * row[1] + self.MARGIN,
                                  (self.MARGIN + self.HEIGHT) * row[0] + self.MARGIN,
                                  self.WIDTH,
                                  self.HEIGHT])

            font = pygame.font.SysFont("Arial MT Light", 20)

            x1 = font.render(str(searchParams.getNumberOfPops()), True, self.WHITE)
            x2 = font.render(str(searchParams.getTotalCost()), True, self.WHITE)
            x3 = font.render(str(searchParams.getTotalTime()), True, self.WHITE)
            #print(searchParams.getNumberOfPops())
            #print(searchParams.getTotalCost())
            screen.blit(x1, (125, 520))
            screen.blit(x2, (255, 520))
            screen.blit(x3, (390, 520))



            pygame.display.update()


            clock.tick(15)
            pygame.display.flip()




        pygame.quit()
