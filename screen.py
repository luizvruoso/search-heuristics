from tkinter import Tk    
from tkinter.filedialog import askopenfilename
from tkinter import Label
from tkinter import ttk
#from openConfigs import openConfigs

# 1 --> Verde           (Custo: 1)
# 2 --> Marrom          (Custo: 5)
# 3 --> Azul            (Custo: 10)
# 4 --> Vermelho        (Custo: 15)

def mainScreen():
    screen = Tk()
    screen.eval('tk::PlaceWindow . center') 
    screen.geometry("350x400")
    screen.title("DATA")
    screen.resizable(False, False)
    Label(text = "D.A.T.A", bg = "grey", width = "150", height = "2", font = ("Calibri", 15)).pack()
    Label(text = "").pack()

    openButton = ttk.Button(screen, text = "Open", width = "15", command = openConfigs)
    openButton.place(x = 130, y = 70)

    labelGroup = ttk.Label(screen, text = "Luiz Vinicius Ruoso   RA: 18233486", width = "40", font = ("Calibri", 11))
    labelGroup.place(x = 20, y = 350)

    labelGroup = ttk.Label(screen, text = "Victor Soldera             RA: 18045674", width = "40", font = ("Calibri", 11))
    labelGroup.place(x = 20, y = 370)

    screen.mainloop()
 
def openConfigs(): 
    global screen
    filename = askopenfilename(title = "Select file", filetypes = (("Text Files","*.txt"),)) 
    f = open(filename, 'r')
    file_contents = f.read()
    num_lines = sum(1 for line in open(filename))
    print(num_lines)
    file_contents = file_contents.replace(',', ' ')

    pathLabel = ttk.Label(screen, text = file_contents, width = "40")
    pathLabel.place(x = 140, y = 120)
