from configMatrix import OpenScreen
from mapMatrixUI import Map
from search.blindSearch.blindSearch import BlindSearch
from search.manhattanDistance.manhattanDistance import ManhattanDistance
import pygame
import threading


def main():
    openScreen = OpenScreen()
    openScreen.screen()
    arrayColorFinalResult = []
    arrayColorFrontier = []
    arrayColorActualPosition = []
    # thread = aux(openScreen)

    t = threading.Thread(target=mainScreen,
                         args=[openScreen, arrayColorActualPosition, arrayColorFinalResult, arrayColorFrontier])
    t.start()

    # search = BlindSearch()
    # t1 = threading.Thread(target=search.blindSearch, args=[openScreen.startPosition, openScreen.finishPosition, openScreen.sketchMatrix, arrayColorActualPosition, arrayColorFinalResult, arrayColorFrontier] )

    search = ManhattanDistance()
    t1 = threading.Thread(target=search.manhattanDistance,
                          args=[openScreen.startPosition, openScreen.finishPosition, openScreen.sketchMatrix,
                                arrayColorActualPosition, arrayColorFinalResult, arrayColorFrontier])

    t1.start()

    # search.blindSearch(openScreen.startPosition, openScreen.finishPosition, openScreen.sketchMatrix, arrayColorActualPosition, arrayColorFinalResult, arrayColorFrontier)


def mainScreen(openScreen, arrayColorActualPosition, arrayColorFinalResult, arrayColorFrontier):
    mapScreen = Map()
    mapScreen.screen(openScreen, arrayColorActualPosition, arrayColorFinalResult, arrayColorFrontier)
    return


if __name__ == "__main__":
    main()
