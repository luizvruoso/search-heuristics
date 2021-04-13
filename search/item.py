


class ItemSearch:
    historyCalls = []

    def __init__(self, actualPosition, cost,totalCost, array, history):
        self.actualPosition = actualPosition
        self.cost = cost
        self.totalCost = totalCost
        self.children = array
        self.historyCalls = history
