#Nora
#Assignment 1
#map.py
import inventory
import drawing
#import sys
isRunning = True

def ExistIn0_0():
    global isRunning
    
    #insert map
    drawing.Map0_0()

    #looping until player exit or move to the next direction
    while isRunning == True:
    #while True:
        print("the begining")
        respond = str(input("Do you want to look or move or take (the mystery box) or exit? ")).lower()
        rep1 = ""
        
        #look
        if respond == "look":
            print("You find yourself in a serene forest glade, where sunlight filters softly through the canopy above, casting dappled patterns on the ground.")
            print("To the north and west, imposing rock walls loom, ancient and unyielding, like silent sentinels of this hidden sanctuary.")
            print("Nestled in the hollow of a gnarled tree, a treasure chest catches your eye, its surface weathered yet intriguing, hinting at untold secrets within. Winding paths lead away to the south and east, inviting you to explore the mysteries that lie beyond.")

        #take
        #take0_0 = False
        elif respond == "take":
            print("You have a hammer!")
            inventory.takeHammers = True
            #TakeItems(respond)
            

        #move
        elif respond == "move":
            moveDir = str(input("What direction do you want to go (north/west/south/east)? ")).strip().lower()
            
            if moveDir == "north" or moveDir == "west":
                print("Ouch, that rock wall hurt")
                print("Let's try again")

            elif moveDir == "east":
                print("Now you are in the new direction!")
                #print("ExistIn1_0")
                ExistIn1_0()
                #break
            elif moveDir == "south":
                print("Now you are in the new direction!")
                #print("ExistIn0_1")
                ExistIn0_1()
                #break
            else:
                print("Make sure that you just type north/west/south/east")

        #exit
        elif respond == "exit":
            confirm = str(input("Are you sure you want to exit? [y/n] "))
            if confirm == "y":
                print("You are exit now")
            isRunning = False
            #break
            #sys.exit()
        
        else:
            print("I don't know how to do that")

def ExistIn0_1():
    global isRunning

    #insert map
    drawing.Map0_1()

    #looping until player exit or move to the next direction
    while isRunning == True:
    #while True:
        respond = str(input("Do you want to look or move or take (the mystery box) or exit? ")).lower()
        rep2 = ""
        #look
        if respond == "look":
            print("In the pitch-black depths of the cave, shadows press in from all sides. To the north, a faint glimmer hints at an exit, offering a sliver of hope in the darkness.")

        #take
        #take0_1 = False
        elif respond == "take":
            print("You have coins!")
            inventory.takeCoins = True

        #move
        elif respond == "move":
            moveDir = str(input("What direction do you want to go (north/west/south/east)? ")).strip().lower()
            
            if moveDir == "north":
                print("Now you are in the new direction!")
                #print("ExistIn0_0")
                ExistIn0_0()

            elif moveDir == "east" or moveDir == "south" or moveDir == "west":
                print("If you move a grue will eat you")
                
            else:
                print("Make sure that you just type north/west/south/east")

        #exit
        elif respond == "exit":
            confirm = str(input("Are you sure you want to exit? [y/n] "))
            if confirm == "y":
                print("You are exit now")
            isRunning = False
            #break
            #sys.exit()
        else:
            print("I don't know how to do that")


def ExistIn1_0():
    global isRunning
    #while isRunning == True:

    #insert map
    drawing.Map1_0()

    #looping until player exit or move to the next direction
    while isRunning == True:
    #while True:
        respond = str(input("Do you want to look or move or take (the mystery box) or exit? ")).lower()
        #look
        if respond == "look":
            print("You stand in the foothills of a rugged mountain range, with towering peaks rising to the north and the vast ocean stretching out to the east.")
            print("Half-buried in the sand at your feet, a weathered watch catches the light, its hands frozen in time.")

        #take
        elif respond == "take":
            print("Oops! There is nothing")

        #move
        elif respond == "move":
            moveDir = str(input("What direction do you want to go (north/west/south/east)? ")).strip().lower()
            
            if moveDir == "east":
                print("You kick off your shoes and start to swim to the setting sun, then change your mind and return and put your shoes back on")
                
            elif moveDir == "north":
                print("Ouch, that rock wall hurt")
                
            elif moveDir == "west":
                print("Now you are in the new direction!")
                #print("ExistIn0_0")
                ExistIn0_0()
                
            elif moveDir == "south":
                print("Now you are in the new direction!")
                #print("ExistIn1_1")
                ExistIn1_1()
                
            else:
                print("Make sure that you just type north/west/south/east")

        #exit
        elif respond == "exit":
            confirm = str(input("Are you sure you want to exit? [y/n] "))
            if confirm == "y":
                print("You are exit now")
            isRunning = False
            #break
            #sys.exit()

        else:
            print("I don't know how to do that")

def ExistIn1_1():
    global isRunning
    #while isRunning == True:

    #insert map
    drawing.Map1_1()

    #looping until player exit or move to the next direction
    while isRunning == True:
    #while True:
        respond = str(input("Do you want to look or move or take (the mystery box) or exit? ")).lower()
        rep3 = ""
        #look
        if respond == "look":
            print("You find yourself at the bottom of a deep canyon, its rocky walls towering above like silent giants. Amid the dust and stones lies a curious sight—a gleaming golden top hat, once belonging to Abe Lincoln, shining like a relic from another time.")

        #take
        #take1_1 = False
        elif respond == "take":
            print("You have bananas! Enjoy!")
            inventory.takeBananas = True

        #move
        elif respond == "move":
            moveDir = str(input("What direction do you want to go (north/west/south/east)? ")).strip().lower()
            
            if moveDir == "east":
                print("Now you are in the new direction!")
                #print("ExistIn2_1")
                ExistIn2_1()
                
            elif moveDir == "north":
                print("Now you are in the new direction!")
                #print("ExistIn1_0")
                ExistIn1_0()
                
            elif moveDir == "west":
                print("Now you are in the new direction!")
                #print("ExistIn0_1")
                ExistIn0_1()
                
            elif moveDir == "south":
                print("Now you are in the new direction!")
                #print("ExistIn1_2")
                ExistIn1_2()
                
            else:
                print("Make sure that you just type north/west/south/east")

        #exit
        elif respond == "exit":
            confirm = str(input("Are you sure you want to exit? [y/n] "))
            if confirm == "y":
                print("You are exit now")
            isRunning = False
            #break
            #sys.exit()

        else:
            print("I don't know how to do that")


def ExistIn1_2():
    global isRunning
    #while isRunning == True:

    #insert map
    drawing.Map1_2()

    #looping until player exit or move to the next direction
    while isRunning == True:
    #while True:
        respond = str(input("Do you want to look or move or take (the mystery box) or exit? ")).lower()
        rep4 = ""
        #look
        if respond == "look":
            print("You stand in a murky swamp, the air thick with an otherworldly mist. The ground squelches beneath you, revealing a jeweled skull nestled in the muck, its gems glistening like captured stars. To the west, a mysterious portal pulses with a faint glow, while two paths beckon: one leading north into shadowy trees and the other stretching east, where distant creatures stir in the mist.")

        #take
        #take1_2 = False
        elif respond == "take":
            print("You have a short gun! Be careful!")
            inventory.takeGuns = True 

        #move
        elif respond == "move":
            moveDir = str(input("What direction do you want to go (north/west/south/east)? ")).strip().lower()
            
            if moveDir == "east":
                print("Now you are in the new direction!")
                #print("ExistIn2_2")
                ExistIn2_2()
                
            elif moveDir == "north":
                print("Now you are in the new direction!")
                #print("ExistIn1_1")
                ExistIn1_1()
                
            elif moveDir == "west":
                confirm = str(input("Are you sure you want to go to this way? [y/n] "))
                if confirm == "y":
                    ExistIn0_0()
                
            elif moveDir == "south":
                print("This seems to be the end of the world. You cannot go that way.")
                
            else:
                print("Make sure that you just type north/west/south/east")

        #exit
        elif respond == "exit":
            confirm = str(input("Are you sure you want to exit? [y/n] "))
            if confirm == "y":
                print("You are exit now")
            isRunning = False
            #break
            #sys.exit()

        else:
            print("I don't know how to do that")

def ExistIn2_1():
    global isRunning
    #while isRunning == True:

    #insert map
    drawing.Map2_1()

    #looping until player exit or move to the next direction
    while isRunning == True:
    #while True:
        respond = str(input("Do you want to look or move or take (the mystery box) or exit? ")).lower()
        rep5 = ""
        #look
        if respond == "look":
            print("You find yourself in a desolate volcanic wasteland, where the ground is covered in a thick layer of ash. Amidst the bleakness, a diamond sparkles brilliantly, a rare treasure gleaming in the darkness. To the west and south, paths stretch out before you, while to the north, the restless ocean crashes against the shore, its waves whispering secrets of the deep.")

        #take
        #take2_1 = False
        elif respond == "take":
            print("You have a gold brick! You are rich now!")
            inventory.takeGold = True

        #move
        elif respond == "move":
            moveDir = str(input("What direction do you want to go (north/west/south/east)? ")).strip().lower()
            
            if moveDir == "east":
                print("You forgot your skis and cannot go that way")
                
            elif moveDir == "north":
                print("You see a sea serpent in the water and decide it is best to stay on land")

            elif moveDir == "west":
                print("Now you are in the new direction!")
                #print("ExistIn1_1")
                ExistIn1_1()
                
            elif moveDir == "south":
                print("Now you are in the new direction!")
                #print("ExistIn2_2")
                ExistIn2_2()
                
            else:
                print("Make sure that you just type north/west/south/east")

        #exit
        elif respond == "exit":
            confirm = str(input("Are you sure you want to exit? [y/n] "))
            if confirm == "y":
                print("You are exit now")
            isRunning = False
            #break
            #sys.exit()

        else:
            print("I don't know how to do that")
    

def ExistIn2_2():
    global isRunning
    #while isRunning == True:

    #insert map
    drawing.Map2_2()

    #looping until player exit or move to the next direction
    while isRunning == True:
    #while True:
        respond = str(input("Do you want to look or move or take (the mystery box) or exit? ")).lower()
        #look
        if respond == "look":
            print("You stand on a vast grass plain, where the gentle breeze sways the emerald blades like a sea. To the east, a colossal chasm gapes in the earth, a deep void that seems to beckon the brave. Paths stretch to the west and north, guiding you through this tranquil landscape. Nestled in the grass, a pot of gold glimmers, its allure shimmering under the sun. To the south, a glowing exit radiates warmth and mystery, inviting you to discover what lies beyond.")

        #take
        elif respond == "take":
            print("So bad! There is nothing! Good luck next time.")

        #move
        elif respond == "move":
            moveDir = str(input("What direction do you want to go (north/west/south/east)? ")).strip().lower()
            
            if moveDir == "east":
                confirm = str(input("Are you sure you want to go to this way? [y/n] "))
                if confirm == "y":
                    print("You make a spectacular swan dive and vanish into a void, never to be seen again. Game over")
                    isRunning = False

            elif moveDir == "west":
                print("Now you are in the new direction!")
                #print("ExistIn1_2")
                ExistIn1_2()

            elif moveDir == "north":
                print("Now you are in the new direction!")
                #print("ExistIn2_1")
                ExistIn2_1()
                
            elif moveDir == "south":
                print("You escaped! Congratulations!")
                print("Now you have: ")

                if(inventory.takeHammers == False and inventory.takeCoins == False and inventory.takeBananas == False and inventory.takeGuns == False and inventory.takeGold == False):
                    print("You have nothing")

                else:
                    
                    if inventory.takeHammers == True:
                        print("Hammers")
                
                    if inventory.takeCoins == True:
                        print("Coins")

                    if inventory.takeBananas == True:
                        print("Bananas")

                    if inventory.takeGuns == True :
                        print("Short Guns")

                    if inventory.takeGold == True:
                        print("Gold Bricks")
                #exit()
                print("This is the end")
                print("Thank you for joining the game")
                isRunning = False
                #sys.exit()
                
            else:
                print("Make sure that you just type south/east")

        #exit
        elif respond == "exit":
            confirm = str(input("Are you sure you want to exit? [y/n] "))
            if confirm == "y":
                print("You are exit now")
            isRunning = False
            #break
            #sys.exit()

        else:
            print("I don't know how to do that")
