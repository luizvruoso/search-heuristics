from search.item import ItemSearch
import time

class ManhattanDistance:
    MATRIX_SIZE = 42

    def __init__(self):
        # Thread.__init__(self)
        self.grid = []

    def setMatrix(self, value):
        self.grid = value

    def getMatrix(self):
        return self.grid

    def getValueWithMatchFromMatrix(self, X, Y):
        return self.grid[X][Y]

    def printMatrixColorFrontier(LIST_FRONTIER, arrayColorFrontier):
        arrayColorFrontier.clear()
        for item in LIST_FRONTIER:
            arrayColorFrontier.append(item[0].getActualPosition())
        return

    def sortItemsTotal(item):
        return item[0].totalCost

    def sortItems(self, item):
        return item[0].cost

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

    def manhattanDistance(self, initialPosition, targetPosition, grid, arrayColorActualPosition, arrayColorFinalResult,
                          arrayColorFrontier):

        LIST_FRONTIER = [[]]

        self.setMatrix(grid)

        LIST_FRONTIER[0].append(self.makeItem(initialPosition, initialPosition, 0, []))

        i = 0
        finalResult = []
        flag = True

        while (len(LIST_FRONTIER)) != 0:

            actual = LIST_FRONTIER.pop(0)
            i += 1

            arrayColorActualPosition.append(actual[0].getActualPosition())

            if actual[0].compareBtwnSelfAndItem(targetPosition):
                finalResult.append(actual)
                flag = False

            if (len(finalResult)) >= 1 and (not flag):
                print("achou um final")
                print("POSICAO Atual", actual[0].actualPosition)
                print("HISTORICO", actual[0].historyCalls)
                print("Numero de pops", i)

                for item in finalResult:
                    print("Resultado ")
                    print(item[0].historyCalls)
                    print("hoi", item[0].totalCost)

                    time.sleep(3)
                    arrayColorFrontier.clear()
                    arrayColorActualPosition.clear()
                    arrayColorFinalResult.clear()

                    for item in item[0].historyCalls:
                        arrayColorFinalResult.append(item)
                finalResult.clear()
                break

            aux = actual[0].getHistoryCall() + [actual[0].getActualPosition()]
            for items in actual[0].getChildren():
                LIST_FRONTIER.append([self.makeItem(actual[0], items, actual[0].getTotalCost(), aux)])

            LIST_FRONTIER.sort(key=self.sortItems)

            arrayColorFrontier.clear()
            for item in LIST_FRONTIER:
                arrayColorFrontier.append(item[0].getActualPosition())

    def makeItem(self, actualPosition, nextPosition, costToAdd, whoCalled):

        ACTUAL_POSITION_X = actualPosition.getX()
        ACTUAL_POSITION_Y = actualPosition.getY()

        NEXT_POSITION_X = nextPosition.getX()
        NEXT_POSITION_Y = nextPosition.getY()

        #print("NEXT", nextPosition)
        childrenArray = []

        i = 0

        # verifica numero direita
        if (NEXT_POSITION_Y + 1) <= 41:
            childrenArray.append(ItemSearch([NEXT_POSITION_X, NEXT_POSITION_Y + 1], 0, 0, None, None))
            i += 1

        # verifica numero a abaixo
        if (NEXT_POSITION_X + 1) <= 41:
            childrenArray.append(ItemSearch([NEXT_POSITION_X + 1, NEXT_POSITION_Y], 0, 0, None, None))
            i += 1

        # verifica numero a cima
        if (NEXT_POSITION_X - 1) >= 0:
            childrenArray.append(ItemSearch([NEXT_POSITION_X - 1, NEXT_POSITION_Y], 0, 0, None, None))
            i += 1

        # verifica numero esquerda
        if (NEXT_POSITION_Y - 1) >= 0:
            childrenArray.append(ItemSearch([NEXT_POSITION_X, NEXT_POSITION_Y - 1], 0, 0, None, None))
            i += 1

        VALUE_POSITION = self.getValueWithMatchFromMatrix(NEXT_POSITION_X, NEXT_POSITION_Y)
        TOTAL_COST_POSITION = self.heuristic(ACTUAL_POSITION_X, ACTUAL_POSITION_Y, NEXT_POSITION_X, NEXT_POSITION_Y)
        COST_POSITION = self.heuristic(ACTUAL_POSITION_X, ACTUAL_POSITION_Y, NEXT_POSITION_X, NEXT_POSITION_Y)

        item = ItemSearch(nextPosition.getActualPosition(), COST_POSITION, TOTAL_COST_POSITION, None, whoCalled)

        item.children = childrenArray
        # TOTAL_COST_POSITION_MAN = self.heuristic(actualPosition)

        return item

    def heuristic(self, actualPositionX, actualPositionY, nextPositionX, nextPositionY):
        dx = abs(actualPositionX - nextPositionX)
        dy = abs(actualPositionY - nextPositionY)

        positionValue = self.getValueWithMatchFromMatrix(nextPositionX, nextPositionY)

        return self.getCostByValue(positionValue) * (dx + dy)
