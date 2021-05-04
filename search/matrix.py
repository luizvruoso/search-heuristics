import json





class Matrix:

    def __init__(self, matrix, sketchMatrix, sizeX, sizeY):
        self.matrix = matrix
        self.sketchMatrix = sketchMatrix
        self.sizeX = sizeX
        self.sizeY = sizeY

        self.op1 = None
        self.op2 = None
        self.op3 = None
        self.op4 = None

    def __init__(self):
        return

    def setSketchMatrix(self, value):
        self.sketchMatrix = value

    def getSketchMatrix(self):
        return self.sketchMatrix

    def setMatrix(self, value):
        self.matrix = value

    def getMatrix(self):
        return self.matrix

    def setSizeX(self, value):
        self.sizeX = value

    def getSizeX(self):
        return self.sizeX

    def setSizeY(self, value):
        self.sizeY = value

    def getSizeY(self):
        return self.sizeY

    def getValueWithMatchFromMatrix(self, X, Y):
        return self.matrix[X][Y]

    def readConfigsMatrixFromJSON(self):
        with open('properties/configs.json') as json_file:
            data = json.load(json_file)
            self.sizeX = data['matrix']['matrix-max-column']
            self.sizeY = data['matrix']['matrix-max-row']

    def makeDbValues(self):
        with open('properties/configs.json') as json_file:
            data = json.load(json_file)
            self.op1 = data['colors']['color-weight']['1']
            self.op2 = data['colors']['color-weight']['2']
            self.op3 = data['colors']['color-weight']['3']
            self.op4 = data['colors']['color-weight']['4']

    def getCostByValue(self, value):
        if value == 1:
            return self.op1
        elif value == 2:
            return self.op2
        elif value == 3:
            return self.op3
        elif value == 4:
            return self.op4
        return 0

