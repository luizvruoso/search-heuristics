import pygame


ACTUAL_POSITION = -1
TARGET_POSITION = -9999

class Map:
    def __init__(self):
        self.WINDOW_SIZE = [505, 505]
        self.GREEN = (151, 224, 103)
        self.BLUE = (84, 194, 234)
        self.RED = (201, 94, 82)
        self.BROWN = (119, 93, 68)   
        self.WHITE = (255, 250, 250) 
        self.BLACK = (0, 0, 0) 

    def screen(self, objectSource): 
       # print(len(grid))

        initialPosition = objectSource.startPosition
        finishPosition =  objectSource.finishPosition

        objectSource.sketchMatrix[initialPosition[0]][initialPosition[1]] = ACTUAL_POSITION
        objectSource.sketchMatrix[finishPosition[0]][finishPosition[1]] = TARGET_POSITION
        
        grid = objectSource.sketchMatrix

        pygame.init()
        # This sets the WIDTH and HEIGHT of each grid location
        WIDTH = 11
        HEIGHT = 11
        
        # This sets the margin between each cell
        MARGIN = 1
        screen = pygame.display.set_mode(self.WINDOW_SIZE)
        pygame.display.set_caption("D.A.T.A")
        done = False
        clock = pygame.time.Clock()

        while not done:
            for event in pygame.event.get():  # User did something
                if event.type == pygame.QUIT:  # If user clicked close
                    done = True  # Flag that we are done so we exit this loop

            for row in range(42):
                #print(grid[row])
                for column in range(42):
                    if grid[row][column] == ACTUAL_POSITION:
                        color = self.WHITE 
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
                    pygame.draw.rect(screen,color,
                        [(MARGIN + WIDTH) * column + MARGIN,
                        (MARGIN + HEIGHT) * row + MARGIN,
                        WIDTH,
                        HEIGHT])

            clock.tick(60)
            pygame.display.flip()
        
        pygame.quit()

