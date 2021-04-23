from search.item import ItemSearch
from mapMatrixUI import Map
import time, threading
import json
import datetime
from search.matrix import Matrix
from search.search import Search

#BUSCA CEGA COM CUSTO UNIFORME
class BlindSearch():
    
    MATRIX_SIZE = 42


    def __init__(self):
        #Thread.__init__(self)
        self.grid = []

    def getCostByValue(self, value):
        if(value == 1):
            return 1
        elif(value == 2):
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




    def blindSearch(self, matrix, searchParams, arrayColorActualPosition, arrayColorFinalResult, arrayColorFrontier):
        LIST_FRONTIER = []
        LIST_FRONTIER.append([])
        ALREADY_VISITED = []
        ALREADY_VISITED.append([])



        self.setMatrix(matrix.getSketchMatrix())

        LIST_FRONTIER[0].append(self.makeItem(searchParams.getInitialPosition(), 0, []))
        # para interações
        i = 0
        finalResult = []

        dataIni = datetime.datetime.now()

        while(len(LIST_FRONTIER) != 0):
            actual = LIST_FRONTIER.pop(0)
            i += 1

            while(len(LIST_FRONTIER) != 0 ):
                if(ALREADY_VISITED.count(actual[0].actualPosition) <= 0 ):
                    ALREADY_VISITED.append(actual[0].actualPosition)
                    break
                else:
                    i += 1
                    actual = LIST_FRONTIER.pop(0)


            arrayColorActualPosition.append(actual[0].getActualPosition())
            

            if(actual[0].compareBtwnSelfAndItem(searchParams.getTargetPosition())):
                finalResult.append(actual)



            if(len(finalResult) >= 1):
                print("UM CAMINHO FOI ENCONTRADO!")
                print("POSICAO ATUAL: ", actual[0].actualPosition)
                actual[0].historyCalls.pop(0)
                actual[0].historyCalls.append(actual[0].actualPosition)
                print("HISTORICO DE CHAMADAS: ", actual[0].historyCalls)
                print("NUMERO DE ITENS ANALISADOS (N DE POPS): ", i)
                #valorPosicacaoFinal = self.getCostByValue(self.getValueWithMatchFromMatrix(actual[0].actualPosition[0], actual[0].actualPosition[1] ))
                #valorPosicaoInicial = self.getCostByValue(self.getValueWithMatchFromMatrix(initialPosition.getX(), initialPosition.getY() ))
                #print("valor da posicao final", valorPosicacaoFinal)
                #print("TOTAL COST", actual[0].totalCost + valorPosicacaoFinal - valorPosicaoInicial)
                soma = 0
                for item in finalResult:
                    time.sleep(1)
                    arrayColorFrontier.clear()
                    arrayColorActualPosition.clear()
                    arrayColorFinalResult.clear()
                    for item in item[0].historyCalls:
                        soma += self.getCostByValue(self.getValueWithMatchFromMatrix(item[0], item[1]))
                        arrayColorFinalResult.append(item)
                    print("Total2", soma)
                finalResult.clear()
                break


            auxHistoricoChamadas = actual[0].getHistoryCall() + [actual[0].getActualPosition()]
            for item in actual[0].getChildren():    
                LIST_FRONTIER.append([self.makeItem(item, actual[0].getTotalCost(), auxHistoricoChamadas)])

            
            LIST_FRONTIER.sort(key=self.sortItems)

            #array para print
            arrayColorFrontier.clear()
            for item in LIST_FRONTIER:
                arrayColorFrontier.append(item[0].getActualPosition())




        print("Data ini ", dataIni)
        print("DAta fim",datetime.datetime.now())
        print("Tempo total passado",datetime.datetime.now() - dataIni)





    def makeItem(self, actualPosition, costToAdd, whoCalled):
        ACTUAL_POSITION_X = actualPosition.getX()
        ACTUAL_POSITION_Y = actualPosition.getY()
        VALUE_POSITION = self.getValueWithMatchFromMatrix(actualPosition.getX(), actualPosition.getY())
        TOTAL_COST_POSITION = self.getCostByValue(VALUE_POSITION) + costToAdd
        COST_POSITION = self.getCostByValue(VALUE_POSITION) + costToAdd


        childrenArray = []
  
        item = ItemSearch(actualPosition.getActualPosition(), COST_POSITION, TOTAL_COST_POSITION, [], whoCalled)


        # verifica numero direita
        if (ACTUAL_POSITION_Y + 1 <= 41):
            childrenArray.append(ItemSearch([ACTUAL_POSITION_X, ACTUAL_POSITION_Y + 1], 
            self.getValueWithMatchFromMatrix(ACTUAL_POSITION_X, ACTUAL_POSITION_Y + 1),
            0,
            [],
            []))

        #verifica numero a abaixo
        if(ACTUAL_POSITION_X + 1 <= 41):
            childrenArray.append(ItemSearch([ACTUAL_POSITION_X + 1, ACTUAL_POSITION_Y],
            self.getValueWithMatchFromMatrix(ACTUAL_POSITION_X + 1, ACTUAL_POSITION_Y),
            0,
            [],
            []))



        #verifica numero a cima
        if( (ACTUAL_POSITION_X - 1) >= 0 ):
            childrenArray.append(ItemSearch([ACTUAL_POSITION_X - 1, ACTUAL_POSITION_Y],
            self.getValueWithMatchFromMatrix(ACTUAL_POSITION_X - 1, ACTUAL_POSITION_Y),
            0,
            [],
            []))


        #verifica numero esquerda
        if(ACTUAL_POSITION_Y - 1 >= 0):
            #childrenArray.append([])
            #childrenArray[i].append(ACTUAL_POSITION_X)
            #childrenArray[i].append(ACTUAL_POSITION_Y - 1)
            childrenArray.append(ItemSearch([ACTUAL_POSITION_X , ACTUAL_POSITION_Y - 1], 
            self.getValueWithMatchFromMatrix(ACTUAL_POSITION_X, ACTUAL_POSITION_Y - 1),
            0,
            [],
            []))




        item.children = childrenArray

        return item
        
    
   


