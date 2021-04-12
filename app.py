from configMatrix import OpenScreen
from mapMatrixUI import Map
from search.blindSearch.blindSearch import BlindSearch

import pygame, threading

def main():
    openScreen = OpenScreen()
    openScreen.screen()
    arrayColor = []
    #thread = aux(openScreen)

 

    t = threading.Thread(target=mainScreen, args=[openScreen, arrayColor] )
    
    #t1 = threading.Thread(target=aux, args=[openScreen])

    #t1.start()
    t.start()
    
    search = BlindSearch()
    search.blindSearch(openScreen.startPosition, openScreen.finishPosition, openScreen.sketchMatrix, arrayColor)
       



def mainScreen(openScreen, arrayColor):
    mapScreen = Map()




    mapScreen.screen(openScreen, arrayColor)
    return




def aux(openScreen):
   
    return

if __name__ == "__main__":
    main()
