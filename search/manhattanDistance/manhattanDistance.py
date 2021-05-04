import pygame

from search.item import ItemSearch
import time
import datetime
from mapMatrixUI import Map
from datetime import timedelta






class ManhattanDistance:
    MATRIX_SIZE = 42

    def __init__(self):
        self.grid = []

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

    # Usando a heurística Distância Manhattan
    def heuristic(self, nextPositionX, nextPositionY, targetPosition):
        dx = abs(nextPositionX - targetPosition.getX())
        dy = abs(nextPositionY - targetPosition.getY())

        return dx + dy

    def manhattanDistance(self, matrix, searchParams, arrayColorActualPosition, arrayColorFinalResult,
                          arrayColorFrontier):

        LIST_FRONTIER = [[]]
        ALREADY_VISITED = [[]]


        self.setMatrix(matrix.getSketchMatrix())

        LIST_FRONTIER[0].append(
            self.makeItem(matrix, searchParams.getInitialPosition(), 0, [], searchParams.getTargetPosition()))

        # para interações
        i = 0
        finalResult = []

        dataIni = datetime.datetime.now()

        while len(LIST_FRONTIER) != 0:
            actual = LIST_FRONTIER.pop(0)
            i += 1

            while len(LIST_FRONTIER) != 0:
                if ALREADY_VISITED.count(actual[0].actualPosition) <= 0:
                    ALREADY_VISITED.append(actual[0].actualPosition)
                    break
                else:
                    i += 1
                    actual = LIST_FRONTIER.pop(0)

            arrayColorActualPosition.append(actual[0].getActualPosition())

            if actual[0].compareBtwnSelfAndItem(searchParams.getTargetPosition()):
                finalResult.append(actual)

            if len(finalResult) >= 1:
                print("UM CAMINHO FOI ENCONTRADO!")
                print("POSICAO ATUAL: ", actual[0].actualPosition)
                actual[0].historyCalls.pop(0)
                actual[0].historyCalls.append(actual[0].actualPosition)
                print("HISTORICO DE CHAMADAS: ", actual[0].historyCalls)
                print("NUMERO DE ITENS ANALISADOS (N DE POPS): ", i)
                #globals.numberOfPops = i
                searchParams.setNumberOfPops(i)
                soma = 0
                for item in finalResult:
                    time.sleep(5)
                    arrayColorFrontier.clear()
                    arrayColorActualPosition.clear()
                    arrayColorFinalResult.clear()
                    for item in item[0].historyCalls:
                        soma += matrix.getCostByValue(self.getValueWithMatchFromMatrix(item[0], item[1]))
                        arrayColorFinalResult.append(item)

                    searchParams.setTotalCost(soma)
                    print("Total2", soma)

                finalResult.clear()
                break

            auxCallHistory = actual[0].getHistoryCall() + [actual[0].getActualPosition()]
            for item in actual[0].getChildren():
                LIST_FRONTIER.append([self.makeItem(matrix, item, actual[0].getTotalCost(), auxCallHistory,
                                                    searchParams.getTargetPosition())])

            LIST_FRONTIER.sort(key=self.sortItems)

            # array para print
            arrayColorFrontier.clear()
            for item in LIST_FRONTIER:
                arrayColorFrontier.append(item[0].getActualPosition())

        print("Data Inicio: ", dataIni)
        print("Data Fim: ", datetime.datetime.now())
        timeFinal = ((datetime.datetime.now() - timedelta(seconds=5)) - dataIni)
        print("Tempo total passado: ", timeFinal)
        searchParams.setTotalTime(timeFinal)



    def makeItem(self, matrixObject, nextPosition, costToAdd, whoCalled, targetPosition):

        NEXT_POSITION_X = nextPosition.getX()
        NEXT_POSITION_Y = nextPosition.getY()

        VALUE_POSITION = self.getValueWithMatchFromMatrix(nextPosition.getX(), nextPosition.getY())
        TOTAL_COST_POSITION = matrixObject.getCostByValue(VALUE_POSITION) + costToAdd
        COST_POSITION = self.heuristic(NEXT_POSITION_X, NEXT_POSITION_Y, targetPosition) + costToAdd

        childrenArray = []

        item = ItemSearch(nextPosition.getActualPosition(), COST_POSITION, TOTAL_COST_POSITION, [], whoCalled)

        # verifica numero direita
        if (NEXT_POSITION_Y + 1) <= matrixObject.getSizeX() - 1:
            childrenArray.append(ItemSearch([NEXT_POSITION_X, NEXT_POSITION_Y + 1],
                                            self.getValueWithMatchFromMatrix(NEXT_POSITION_X, NEXT_POSITION_Y + 1),
                                            0,
                                            [],
                                            []))

        # verifica numero a abaixo
        if (NEXT_POSITION_X + 1) <= matrixObject.getSizeY() - 1:
            childrenArray.append(ItemSearch([NEXT_POSITION_X + 1, NEXT_POSITION_Y],
                                            self.getValueWithMatchFromMatrix(NEXT_POSITION_X + 1, NEXT_POSITION_Y),
                                            0,
                                            [],
                                            []))

        # verifica numero a cima
        if (NEXT_POSITION_X - 1) >= 0:
            childrenArray.append(ItemSearch([NEXT_POSITION_X - 1, NEXT_POSITION_Y],
                                            self.getValueWithMatchFromMatrix(NEXT_POSITION_X - 1, NEXT_POSITION_Y),
                                            0,
                                            [],
                                            []))

        # verifica numero esquerda
        if (NEXT_POSITION_Y - 1) >= 0:
            childrenArray.append(ItemSearch([NEXT_POSITION_X, NEXT_POSITION_Y - 1],
                                            self.getValueWithMatchFromMatrix(NEXT_POSITION_X, NEXT_POSITION_Y - 1),
                                            0,
                                            [],
                                            []))

        item.children = childrenArray
        return item
