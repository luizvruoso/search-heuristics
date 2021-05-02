from tkinter import Tk
from tkinter.filedialog import askopenfilename
from tkinter import Label
from tkinter import ttk
from utils.arrayTreatment import arrayContentToInt
from search.item import ItemSearch
import copy

# 1 --> Verde           (Custo: 1)
# 2 --> Marrom          (Custo: 5)
# 3 --> Azul            (Custo: 10)
# 4 --> Vermelho        (Custo: 15)


class OpenScreen:
    def __init__(self):
        self.sketchMatrix = []
        self.squareMatrixSize = 42  # const
        self.startPosition = []
        self.finishPosition = []
        self.matrixObject = None
        self.searchParams = None

    def openConfigs(self, button):

        filename = askopenfilename(title="Select file", filetypes=(("Text Files", "*.txt"),))
        f = open("index.txt", 'r')
        self.searchParams.setSearchMethod(button)
        self.matrixObject.readConfigsMatrixFromJSON()

        auxReadLine = f.readline()
        auxPosition = arrayContentToInt(auxReadLine.strip().split(","))
        self.startPosition = ItemSearch(auxPosition, 0, 0, None, None)

        auxReadLine = f.readline()

        auxPosition = arrayContentToInt(auxReadLine.strip().split(","))
        self.finishPosition = ItemSearch(auxPosition, 0, 0, None, None)

        file_contents = f.read()
        file_contents = file_contents.replace('\n', '').replace(',', '')
        # ACEITA APENAS MATRIZES QUADRADAS

        for i in range(self.squareMatrixSize):
            self.sketchMatrix.append([])

            for j in range(self.squareMatrixSize):
                self.sketchMatrix[i].append(int(file_contents[(i * 42) + j]))

        self.matrixObject.setSketchMatrix(copy.deepcopy(self.sketchMatrix))
        self.matrixObject.setMatrix(self.sketchMatrix)

        self.searchParams.setInitialPosition(self.startPosition)
        self.searchParams.setTargetPosition(self.finishPosition)

        quit()

    def screen(self, matrix, searchParams):
        global screen
        self.matrixObject = matrix
        self.searchParams = searchParams

        screen = Tk()
        screen.eval('tk::PlaceWindow . center')
        screen.geometry("400x400")
        screen.title("DATA")
        screen.resizable(False, False)
        Label(text="D.A.T.A", bg="grey", width="150", height="2", font=("Calibri", 15)).pack()
        Label(text="").pack()

        blindSearchButton = ttk.Button(screen, text="Blind Search", width="20",
                                       command=lambda: self.openConfigs("blind"))
        blindSearchButton.place(x=135, y=70)

        manhattanButton = ttk.Button(screen, text="Manhattan Distance", width="20",
                                     command=lambda: self.openConfigs("manhattan"))
        manhattanButton.place(x=135, y=100)

        labelGroup = ttk.Label(screen, text="Luiz Vinicius Ruoso   RA: 18233486", width="40", font=("Calibri", 11))
        labelGroup.place(x=20, y=350)

        labelGroup = ttk.Label(screen, text="Victor Soldera             RA: 18045674", width="40", font=("Calibri", 11))
        labelGroup.place(x=20, y=370)

        screen.mainloop()

    def quit(self):
        global screen
        screen.quit()
