from configMatrix import OpenScreen
from mapMatrixUI import Map
from search.blindSearch.blindSearch import BlindSearch
import datetime
from search.matrix import Matrix
from search.search import Search
import pygame, threading

def main():

    arrayColorFinalResult = []
    arrayColorFrontier = []
    arrayColorActualPosition = []

    matrix = Matrix()
    searchParams = Search()

    #thread = aux(openScreen)

    t0 = threading.Thread(target=openScreenAux, args=[matrix, searchParams])
    t0.start()
    t0.join()

    #print(matrix)

    t = threading.Thread(target=mainScreen, args=[matrix, searchParams, arrayColorActualPosition, arrayColorFinalResult, arrayColorFrontier] )
    
    #t1 = threading.Thread(target=aux, args=[openScreen])

    #t1.start()
    
    t.start()
    search = BlindSearch()
    t1 = threading.Thread(target=search.blindSearch, args=[matrix, searchParams, arrayColorActualPosition, arrayColorFinalResult, arrayColorFrontier] )

    # search = BlindSearch()
    # t1 = threading.Thread(target=search.blindSearch, args=[openScreen.startPosition, openScreen.finishPosition, openScreen.sketchMatrix, arrayColorActualPosition, arrayColorFinalResult, arrayColorFrontier] )

    search = ManhattanDistance()
    t1 = threading.Thread(target=search.manhattanDistance,
                          args=[openScreen.startPosition, openScreen.finishPosition, openScreen.sketchMatrix,
                                arrayColorActualPosition, arrayColorFinalResult, arrayColorFrontier])

    t1.start()

def mainScreen(matrix, searchParams, arrayColorActualPosition, arrayColorFinalResult, arrayColorFrontier):
    mapScreen = Map()
    mapScreen.screen(matrix, searchParams, arrayColorActualPosition, arrayColorFinalResult, arrayColorFrontier)
    return

def openScreenAux(matrix, searchParams):
    openScreen = OpenScreen()
    openScreen.screen(matrix, searchParams)
    return

if __name__ == "__main__":
    main()
