


class ItemSearch:
    historyCalls = []

    def __init__(self, actualPosition, cost, array, history):
        self.actualPosition = actualPosition
        self.cost = cost
        self.children = array
        self.historyCalls = history
