class ItemSearch:
    historyCalls = []

    def __init__(self, actualPosition, cost, totalCost, array, history):
        self.actualPosition = actualPosition
        self.cost = cost
        self.totalCost = totalCost
        self.children = array
        self.historyCalls = history

    def setActualPosition(self, value):
        self.actualPosition = value

    def getActualPosition(self):
        return self.actualPosition

    def getX(self):
        return self.actualPosition[0]

    def getY(self):
        return self.actualPosition[1]
    
    def setCost(self, value):
        self.setCost = value
    
    def getCost(self, value):
        return self.cost
    
    def setTotalCost(self, value):
        self.totalCost = value
    
    def getTotalCost(self):
        return self.totalCost
    
    def setChildren(self, value):
        self.setChildren = value
    
    def getChildren(self):
        return self.children

    def setHistoryCall(self, value):
        self.historyCalls = value

    def getHistoryCall(self):
        return self.historyCalls


#METODOS UTEIS
    def compareBtwnSelfAndItem(self, item):
        if(item.getX() == self.getX() and item.getY() == self.getY()):
            return True
        else: return False
