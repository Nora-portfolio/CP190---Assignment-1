#Nora
#Assignment 1
#gameFile.py

import map
import inventory

def runGame():
    nameCha = str(input("Name your character: "))
    print("Welcome " + nameCha)
    #jump into the game
    map.ExistIn0_0()
    
runGame()
