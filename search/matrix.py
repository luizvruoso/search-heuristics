import json
import copy
class Matrix:

    def __init__(self, matrix, sketchMatrix, sizeX, sizeY):
        self.matrix = matrix
        self.sketchMatrix = sketchMatrix
        self.sizeX = sizeX
        self.sizeY = sizeY

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

    def getCostByValue(self, value):
        if (value == 1):
            return 2
        elif (value == 2):
            return 5
        elif (value == 3):
            return 10
        elif (value == 4):
            return 15
        return 0

    def getValueWithMatchFromMatrix(self, X, Y):
        return self.matrix[X][Y]

    def readConfigsMatrixFromJSON(self):
        with open('properties/configs.json') as json_file:
            data = json.load(json_file)
            self.sizeX = data['matrix']['matrix-max-column']
            self.sizeY = data['matrix']['matrix-max-row']