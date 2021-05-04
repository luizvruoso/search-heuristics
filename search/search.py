class Search:

    def __init__(self, initialPosition, nextPosition, targetPosition, numberOfPops, totalCost, totalTime, searchMethod):
        self.initialPosition = initialPosition
        self.nextPosition = nextPosition
        self.targetPosition = targetPosition
        self.numberOfPops = numberOfPops
        self.totalCost = totalCost
        self.totalTime = totalTime
        self.searchMethod = searchMethod


    def setSearchMethod(self, value):
        self.searchMethod = value

    def getSearchMethod(self):
        return self.searchMethod

    def setTotalTime(self, value):
        self.totalTime = value

    def getTotalTime(self):
        return self.totalTime

    def setTotalCost(self, value):
        self.totalCost = value

    def getTotalCost(self):
        return self.totalCost

    def setNumberOfPops(self, value):
        self.numberOfPops = value

    def getNumberOfPops(self):
        return self.numberOfPops

    def setInitialPosition(self, value):
        self.initialPosition = value

    def getInitialPosition(self):
        return self.initialPosition

    def setTargetPosition(self, value):
        self.targetPosition = value

    def getTargetPosition(self):
        return self.targetPosition

    def setNextPosition(self, value):
        self.nextPosition = value

    def getNextPosition(self):
        return self.nextPosition

    def isInititalAndTargetValid(self, matrix):
        if self.initialPosition.actualPosition[0] <= matrix.getSizeX() and self.initialPosition.actualPosition[0] >= 0:
            if self.targetPosition.actualPosition[1] <= matrix.getSizeY() and self.targetPosition.actualPosition[1] >= 0:
                return True

        return False

