from search.item import ItemSearch
from mapMatrixUI import Map
import time, threading
import json


#BUSCA CEGA COM CUSTO UNIFORME
class BlindSearch():
    
    MATRIX_SIZE = 42


    def __init__(self):
        #Thread.__init__(self)
        self.grid = []

    def getCostByValue(self, value):
        if value == 1:
            return 1
        elif value == 2:
            return 5
        elif value == 3:
            return 10
        elif value == 4:
            return 15

        return 0
    
    def setMatrix(self, value):
        self.grid = value

    def getMatrix(self):
        return self.grid

    def getValueWithMatchFromMatrix(self, X, Y):
        return self.grid[X][Y]

    def sortItems(self, item):
        return item[0].cost

    def sortItemsTotal(self, item):
        return item[0].totalCost

    def blindSearch(self, initialPosition, targetPosition, grid, arrayColorActualPosition, arrayColorFinalResult, arrayColorFrontier):
        #print(grid)
        LIST_FRONTIER = []
        LIST_FRONTIER.append([])
        #PRIMEIRA PASSO
        self.setMatrix(grid)
        LIST_FRONTIER[0].append(self.makeItem(initialPosition, 0, []))

        actual = LIST_FRONTIER[0]
        ALREADY_VISITED = []
        ALREADY_VISITED.append([])
        COLOR = []
        
        i = 0
        finalResult = []
        flag = True
        #f = open("saida.txt", 'w')
        #f.truncate(0)
        auxTotalCostFounded = 0
        while(len(LIST_FRONTIER) != 0):
            #print(len(LIST_FRONTIER))
            actual = LIST_FRONTIER.pop(0)
            i += 1

            while(len(LIST_FRONTIER) != 0):
                if(ALREADY_VISITED.count(actual[0].actualPosition) <= 1 ):
                    ALREADY_VISITED.append(actual[0].actualPosition)
                    break
                else:
                    #f.write("Popado"+ str(actual[0].actualPosition) + "\n")
                    i += 1
                    actual = LIST_FRONTIER.pop(0)

            #for item in LIST_FRONTIER:
                #ctrl = -1
                #try: 
                   # ctrl = ALREADY_VISITED.index(item[0])
                #except:
                    #ctrl = -1
                #if(ctrl == -1):
                    #print("LIST_FRONTIER | Posicao", item[0].actualPosition, "Custo", item[0].cost, "Total", item[0].totalCost)

            #ALREADY_VISITED.append(actual)
            arrayColorActualPosition.append(actual[0].getActualPosition())
            

            if(actual[0].compareBtwnSelfAndItem(targetPosition)):
                finalResult.append(actual)
                flag = False

            #if(actual[0].actualPosition[0] == targetPosition[0] and actual[0].actualPosition[1] == targetPosition[1]):
            #    finalResult.append(actual)
            #    flag = False


            if(len(finalResult) >= 1 and not flag):
                print("achou um final")
                print("POSICAO Atual", actual[0].actualPosition)
                print("HISTORICO", actual[0].historyCalls)
                print("Numero de pops", i)
                for item in finalResult:
                    print("Resultado ")
                    print(item[0].historyCalls)
                    print("hoi", item[0].totalCost)
                    auxTotalCostFounded = item[0].totalCost
                    time.sleep(3)
                    arrayColorFrontier.clear()
                    arrayColorActualPosition.clear()
                    arrayColorFinalResult.clear()
                    #print('asdadasdasdasdas', item[0].historyCalls)
                    for item in item[0].historyCalls:
                        arrayColorFinalResult.append(item)
                finalResult.clear()
                break


            aux = actual[0].getHistoryCall() + [actual[0].getActualPosition()]
            for items in actual[0].getChildren():    
                LIST_FRONTIER.append([self.makeItem(items, actual[0].getTotalCost(), aux)])
            

          
            
            LIST_FRONTIER.sort(key=self.sortItems) #ISSO É ALTO NIVEL - DEMOROU 3 HORAS
            #LIST_FRONTIER.sort(key=self.sortItemsTotal, reverse=True) #ISSO É AUTO NIVEL - DEMOROU 3 HORAS
            #aux = "LOOP "+str(i)+"=============== Posicao Atual"+str(actual[0].actualPosition)

            #print("LOOP ", i, "=============== Posicao Atual", actual[0].actualPosition)
            #f.write(str(aux)+"\n")

            #print("item list")

            arrayColorFrontier.clear()
            for item in LIST_FRONTIER:
                arrayColorFrontier.append(item[0].getActualPosition())
                #aux = "item Cost"+str(item[0].cost)+"position"+str(item[0].actualPosition)
                #f.write(str(aux)+"\n")

           # t1 = threading.Thread(target=self.printMatrixColorFrontier,
            #                      args=[LIST_FRONTIER, arrayColorFrontier])
            #t1.start()


            #print("item", item[0].cost, "value", item[0].actualPosition)
        
        #f.close()
        


    def printMatrixColorFrontier(self, LIST_FRONTIER, arrayColorFrontier):
        arrayColorFrontier.clear()
        for item in LIST_FRONTIER:
            arrayColorFrontier.append(item[0].getActualPosition())
        return

    def makeItem(self, actualPosition, costToAdd, whoCalled):
        ACTUAL_POSITION_X = actualPosition.getX()
        ACTUAL_POSITION_Y = actualPosition.getY()
        VALUE_POSITION = self.getValueWithMatchFromMatrix(actualPosition.getX(), actualPosition.getY())
        TOTAL_COST_POSITION = self.getCostByValue(VALUE_POSITION) + costToAdd
        COST_POSITION = self.getCostByValue(VALUE_POSITION) + costToAdd

        # print(TOTAL_COST_POSITION)
        childrenArray = []
  
        item = ItemSearch(actualPosition.getActualPosition(), COST_POSITION, TOTAL_COST_POSITION, None, whoCalled)
        
        i = 0

        # verifica numero direita
        if (ACTUAL_POSITION_Y + 1 <= 41):
            #childrenArray.append([])
            childrenArray.append(ItemSearch([ACTUAL_POSITION_X, ACTUAL_POSITION_Y + 1], 0, 0, None, None))
            #childrenArray[i].append(ACTUAL_POSITION_Y + 1)
            i += 1
        #verifica numero a abaixo
        if(ACTUAL_POSITION_X + 1 <= 41):
            #childrenArray.append([])
            #childrenArray[i].append(ACTUAL_POSITION_X + 1)
            #childrenArray[i].append(ACTUAL_POSITION_Y)
            childrenArray.append(ItemSearch([ACTUAL_POSITION_X+1, ACTUAL_POSITION_Y], 0, 0, None, None))

            #print(item.historyCalls.count(childrenArray[i]))
            i+=1

        #verifica numero a cima
        if( (ACTUAL_POSITION_X - 1) >= 0 ):
            #childrenArray.append([])
            childrenArray.append(ItemSearch([ACTUAL_POSITION_X - 1 , ACTUAL_POSITION_Y], 0, 0, None, None))

            #childrenArray[i].append(ACTUAL_POSITION_X - 1)
            #childrenArray[i].append(ACTUAL_POSITION_Y)
            i+=1

        #verifica numero esquerda
        if(ACTUAL_POSITION_Y - 1 >= 0):
            #childrenArray.append([])
            #childrenArray[i].append(ACTUAL_POSITION_X)
            #childrenArray[i].append(ACTUAL_POSITION_Y - 1)
            childrenArray.append(ItemSearch([ACTUAL_POSITION_X, ACTUAL_POSITION_Y - 1], 0, 0, None, None))

            i+=1
            

        # aux = []
        # for j in range(len(childrenArray)):
        #      if(item.historyCalls.count(childrenArray[j]) == 0):
        #         aux.append(childrenArray[j])



        item.children = childrenArray

        return item
        
        



