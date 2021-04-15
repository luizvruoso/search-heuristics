from configMatrix import OpenScreen
from mapMatrixUI import Map
from search.blindSearch.blindSearch import BlindSearch

import pygame, threading

def main():
    openScreen = OpenScreen()
    openScreen.screen()
    arrayColorFinalResult = []
    arrayColorFrontier = []
    arrayColorActualPosition = []
    #thread = aux(openScreen)

    
    t = threading.Thread(target=mainScreen, args=[openScreen, arrayColorActualPosition, arrayColorFinalResult, arrayColorFrontier] )
    
    #t1 = threading.Thread(target=aux, args=[openScreen])

    #t1.start()
    
    t.start()
    search = BlindSearch()
    t1 = threading.Thread(target=search.blindSearch, args=[openScreen.startPosition, openScreen.finishPosition, openScreen.sketchMatrix, arrayColorActualPosition, arrayColorFinalResult, arrayColorFrontier] )

    t1.start()


    #search.blindSearch(openScreen.startPosition, openScreen.finishPosition, openScreen.sketchMatrix, arrayColorActualPosition, arrayColorFinalResult, arrayColorFrontier)
       



def mainScreen(openScreen, arrayColorActualPosition, arrayColorFinalResult, arrayColorFrontier):
    mapScreen = Map()
    mapScreen.screen(openScreen, arrayColorActualPosition, arrayColorFinalResult, arrayColorFrontier)
    return

if __name__ == "__main__":
    main()
