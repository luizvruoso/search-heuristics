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

        



    def blindSearch(self, initialPosition, targetPosition, grid):
        LIST_FRONTIER = []
        LIST_FRONTIER.append([])
        #PRIMEIRA PASSO
        LIST_FRONTIER[0].append(self.makeItem(initialPosition, grid))
        print(LIST_FRONTIER)

        

        



    def makeItem(self, actualPosition, grid):
        
        ACTUAL_POSITION_X = actualPosition[0]
        ACTUAL_POSITION_Y = actualPosition[1]
        VALUE_POSITION = grid[ACTUAL_POSITION_X][ACTUAL_POSITION_Y]
        COST_POSITION = self.getCostByValue(VALUE_POSITION)
        
        childrenArray = []

        item = ItemSearch(actualPosition, COST_POSITION, None)
        
        i = 0
        #verifica numero a esquerda
        if( (ACTUAL_POSITION_X - 1) >= 0 ):
            childrenArray.append([])
            childrenArray[i].append(ACTUAL_POSITION_X - 1)
            childrenArray[i].append(ACTUAL_POSITION_Y)
            i+=1

        #verifica numero a direita
        if(ACTUAL_POSITION_X + 1 <= 41):
            childrenArray.append([])
            childrenArray[i].append(ACTUAL_POSITION_X + 1)
            childrenArray[i].append(ACTUAL_POSITION_Y)
            i+=1

        #verifica numero acima
        if(ACTUAL_POSITION_Y - 1 >= 0):
            childrenArray.append([])
            childrenArray[i].append(ACTUAL_POSITION_X)
            childrenArray[i].append(ACTUAL_POSITION_Y - 1)
            i+=1
        
        #verifica numero abaixo
        if(ACTUAL_POSITION_Y + 1 <= 41):
            childrenArray.append([])
            childrenArray[i].append(ACTUAL_POSITION_X)
            childrenArray[i].append(ACTUAL_POSITION_Y + 1)
            i+=1

        item.children = childrenArray
        return item
        
        




    



