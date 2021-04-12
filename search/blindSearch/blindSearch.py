from search.item import ItemSearch
from mapMatrixUI import Map
from threading import Thread
import time
import json


#BUSCA SEGA COM CUSTO UNIFORME
class BlindSearch(Thread):
    
    MATRIX_SIZE = 42


    def __init__(self):
        Thread.__init__(self)
        self.grid = []
        self.start()

    def initA(self):
        print("adasdasdasdasdsadsa")

    def getCostByValue(self, value):
        if(value == 1):
            return 1
        elif(value == 2):
            return 5
        elif(value == 3):
            return 10
        elif(value == 4):
            return 15

        return 0
    
    def sortItems(self, item):
        return item[0].cost

    def blindSearch(self, initialPosition, targetPosition, grid, arrayColor):
        #print(grid)
        LIST_FRONTIER = []
        LIST_FRONTIER.append([])
        #PRIMEIRA PASSO
        LIST_FRONTIER[0].append(self.makeItem(initialPosition, grid, 0, []))
        actual = LIST_FRONTIER[0]
        i = 0
        finalResult = []
        flag = True

        while(True):

            actual = LIST_FRONTIER.pop(0)
            #print("LIST_FRONTIER", LIST_FRONTIER)


            arrayColor.append(actual[0].actualPosition)

            if(actual[0].actualPosition[0] == targetPosition[0] and actual[0].actualPosition[1] == targetPosition[1]):
                finalResult.append(actual)
                flag = False


            if(len(finalResult) >= 1 and not flag):
                print("achou um final")
                print("POSICAO Atual", actual[0].actualPosition)
                print("HISTORICO", actual[0].historyCalls)
                for item in finalResult:
                    print("Resultado ")
                    print(item[0].historyCalls)
                    time.sleep(3)
                    arrayColor.clear()
                    for item in item[0].historyCalls:
                        arrayColor.append(item)
                print("final")

                break
                

            aux = actual[0].historyCalls + [actual[0].actualPosition]
         
            if(len(LIST_FRONTIER) <= 1500): 
                for items in actual[0].children:    
                    LIST_FRONTIER.append([self.makeItem(items, grid, actual[0].cost, aux)])
            
            i += 1
            
            LIST_FRONTIER.sort(key=self.sortItems) #ISSO É AUTO NIVEL - DEMOROU 3 HORAS
            #print("item list")


            #for item in LIST_FRONTIER:
             #   print("item", item[0].cost, "value", item[0].actualPosition, "cost", item[0].cost)
        
        
        

        



    def isAdjacent(self, position, targetPosition):
        ACTUAL_POSITION_X = position[0]
        ACTUAL_POSITION_Y = position[1]

        TARGET_POSITION_X = targetPosition[0].actualPosition[0]
        TARGET_POSITION_Y = targetPosition[0].actualPosition[1]

        #PODE IR A ESQUERDA
        if( (ACTUAL_POSITION_X - 1) >= 0 and ACTUAL_POSITION_Y == TARGET_POSITION_Y):
            return True

        #PODE IR A DIREITA
        if( (ACTUAL_POSITION_X + 1) <= 41 and ACTUAL_POSITION_Y == TARGET_POSITION_Y):
            return True
            
        #PODE IR A ACIMA
        if( ACTUAL_POSITION_X ==  TARGET_POSITION_X and ACTUAL_POSITION_Y - 1 >= 0):
            return True

        #PODE IR A ACIMA
        if( ACTUAL_POSITION_X ==  TARGET_POSITION_X and ACTUAL_POSITION_Y + 1 <= 41):
            return True

        return False


    def makeItem(self, actualPosition, grid, costToAdd, whoCalled):
        
        ACTUAL_POSITION_X = actualPosition[0]
        ACTUAL_POSITION_Y = actualPosition[1]
        VALUE_POSITION = grid[ACTUAL_POSITION_X][ACTUAL_POSITION_Y]
        COST_POSITION = self.getCostByValue(VALUE_POSITION) + costToAdd
        

        
        childrenArray = []
  
        item = ItemSearch(actualPosition, COST_POSITION, None, whoCalled)
        
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
        
        



