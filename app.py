from configMatrix import OpenScreen
from mapMatrixUI import Map
from search.blindSearch.blindSearch import BlindSearch
from search.manhattanDistance.manhattanDistance import ManhattanDistance
from search.matrix import Matrix
from search.search import Search

import threading


def main():
    arrayColorFinalResult = []
    arrayColorFrontier = []
    arrayColorActualPosition = []
    matrix = Matrix()
    searchParams = Search([], [], [], 0, 0, 0, None)

    t0 = threading.Thread(target=openScreenAux, args=[matrix, searchParams])
    t0.start()
    t0.join()

    t = threading.Thread(target=mainScreen, args=[matrix, searchParams, arrayColorActualPosition, arrayColorFinalResult,
                                                  arrayColorFrontier])

    t.start()

    print("maaaaaoizinho?", searchParams.getSearchMethod())

    if searchParams.getSearchMethod() == 'blind':
        search = BlindSearch()
        t1 = threading.Thread(target=search.blindSearch,
                              args=[matrix, searchParams, arrayColorActualPosition, arrayColorFinalResult,
                                    arrayColorFrontier])
        t1.start()
    else:

        search = ManhattanDistance()
        t1 = threading.Thread(target=search.manhattanDistance,
                               args=[matrix, searchParams, arrayColorActualPosition, arrayColorFinalResult,
                                     arrayColorFrontier])
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
