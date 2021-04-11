from configMatrix import OpenScreen
from mapMatrixUI import Map
from search.blindSearch.blindSearch import BlindSearch

import pygame

def main():
    openScreen = OpenScreen()
    openScreen.screen()
    
    #mapScreen = Map()
    #mapScreen.screen(openScreen)

    search = BlindSearch()
    search.blindSearch(openScreen.startPosition, openScreen.finishPosition, openScreen.sketchMatrix)
    


if __name__ == "__main__":
    main()
