from search.item import ItemSearch
import json


#BUSCA SEGA COM CUSTO UNIFORME
class BlindSearch:
    
    MATRIX_SIZE = 42

    def __init__(self):
        self.a = "a"
    
    def getCostByValue(self, value):

        if(value == 1):
            return 1
        elif(value == 2):
            return 5
        elif(value == 3):
            return 10
        elif(value == 4):
            return 15

        



    #def blindSearch(self, initialPosition, targetPosition, grid):






    def getChildrenItem(self, actualPosition, grid):
        
        ACTUAL_POSITION_X = actualPosition[0]
        ACTUAL_POSITION_Y = actualPosition[1]
        VALUE_POSITION = grid[ACTUAL_POSITION_X][ACTUAL_POSITION_Y]
        COST_POSITION = self.getCostByValue(VALUE_POSITION)

        childrenArray = []

        item = ItemSearch(actualPosition, COST_POSITION, None)

        #verifica numero a esquerda
        if(grid[ACTUAL_POSITION_X - 1][ACTUAL_POSITION_Y] != None):
            childrenArray[0].append(ACTUAL_POSITION_X - 1)
            childrenArray[0].append(ACTUAL_POSITION_Y)

        #verifica numero a direita
        if(grid[ACTUAL_POSITION_X + 1][ACTUAL_POSITION_Y] != None):
            childrenArray[1].append(ACTUAL_POSITION_X + 1)
            childrenArray[1].append(ACTUAL_POSITION_Y)

        #verifica numero acima
        if(grid[ACTUAL_POSITION_X][ACTUAL_POSITION_Y - 1] != None):
            childrenArray[2].append(ACTUAL_POSITION_X)
            childrenArray[2].append(ACTUAL_POSITION_Y - 1)

        #verifica numero abaixo
        if(grid[ACTUAL_POSITION_X][ACTUAL_POSITION_Y +1] != None):
            childrenArray[3].append(ACTUAL_POSITION_X)
            childrenArray[3].append(ACTUAL_POSITION_Y + 1)

        item.children = childrenArray

        print(item.children)
        




    



