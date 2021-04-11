from tkinter import Tk    
from tkinter.filedialog import askopenfilename
from tkinter import Label
from tkinter import ttk
from utils.arrayTreatment import arrayContentToInt

# 1 --> Verde           (Custo: 1)
# 2 --> Marrom          (Custo: 5)
# 3 --> Azul            (Custo: 10)
# 4 --> Vermelho        (Custo: 15)

class OpenScreen:

        def __init__(self):
                self.sketchMatrix = []
                self.squareMatrixSize = 42 #const
                self.startPosition = []
                self.finishPosition = []
        

        def openConfigs(self): 
                # filename = askopenfilename(title = "Select file", filetypes = (("Text Files","*.txt"),)) 

                f = open("index.txt", 'r')

                auxReadLine = f.readline()
                self.startPosition = arrayContentToInt(auxReadLine.strip().split(","))

                auxReadLine = f.readline()
                
                self.finishPosition = arrayContentToInt(auxReadLine.strip().split(","))

                file_contents = f.read() 
                file_contents = file_contents.replace('\n', '').replace(',', '')
               
                for i in range(self.squareMatrixSize):
                        self.sketchMatrix.append([])

                        for j in range(self.squareMatrixSize):
                                self.sketchMatrix[i].append(int(file_contents[ ( i * 42 ) + j ]))

                self.quit()

        def screen(self):
               
                global screen
                screen = Tk()
                screen.eval('tk::PlaceWindow . center') 
                screen.geometry("350x400")
                screen.title("DATA")
                screen.resizable(False, False)
                Label(text = "D.A.T.A", bg = "grey", width = "150", height = "2", font = ("Calibri", 15)).pack()
                Label(text = "").pack()

                openButton = ttk.Button(screen, text = "Import File", width = "15", command = self.openConfigs)
                openButton.place(x = 130, y = 70)

                labelGroup = ttk.Label(screen, text = "Luiz Vinicius Ruoso   RA: 18233486", width = "40", font = ("Calibri", 11))
                labelGroup.place(x = 20, y = 350)

                labelGroup = ttk.Label(screen, text = "Victor Soldera             RA: 18045674", width = "40", font = ("Calibri", 11))
                labelGroup.place(x = 20, y = 370)

                screen.mainloop()
        
        def quit(self):
            global screen
            screen.quit()