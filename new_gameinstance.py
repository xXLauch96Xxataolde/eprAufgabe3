"""Game Instance 

This function returns a specially configured game instance. This is for the
core game mechanics. Dices, Faces and Seeds can be configured as the user wants
it. 
"""

import main
from player import Player

__author__ = "6770541: Niels Heissel, 6785468: Robert am Wege"
__copyright__ = "Copyright 2017/2018 - EPR-Goethe-Uni" 
__credits__ = "" 
__email__ = "uni.goethe.horde@gmail.com" 


def game_inst():
    """As written above this returns a game instance."""
    
    number = 0
    faces = 0
    seed = 0.0
    print("Do you wish to configure your own dice(s). (y/n)")
    inp = input()
    if (inp == "exit"):
        return ("exit")
    if (inp == "y"):
        while (True):
            print("Great. How many dices? 1-10 are possible")
            inp = input()
            if (inp == "exit"):
                return ("exit")
            try:
                inp = int(inp)
                if (0 < inp and inp < 11):
                    print("Great")
                    number = inp
                elif (inp < 1):
                    print("Not enough. Repeat")
                    continue
                elif (inp > 10):
                    print("Too many dices. Repeat")
                    continue
                print("How many faces per Dice? Faces between 2 and 100.")
                inp = int(input())
                if (inp == "exit"):
                    return ("exit")
                if (1 < inp and inp < 101):
                    print("Great")
                    faces = inp
                elif (inp < 2):
                    print("Not enough. Repeat")
                    continue
                elif (inp > 100):
                    print("Too many dices. Repeat")
                    continue
                print("Do you want a seed? (y/n)")
                inp = input()
                if (inp == "exit"):
                    return ("exit")
                if (inp == "y"):
                    print("Which seed for pseudo random? Float expected")
                    inp = input()
                    if (inp == "exit"):
                        return ("exit")
                    seed = float(inp)
                    return (number, faces, seed)
                else:
                    print("Standard Seed=None it is")
                    return (number, faces, None)
                break
            except (ValueError, IndexError):
                print("Unreadable")
    elif (inp == "n"):
        print("Ok. 1 dice, 6 faces. No seed. \n")
        number = 1
        faces = 6
        seed = None
        return (number, faces, seed)
    else:
        print("You must be wasted. Standard Game for you <3")
        number = 1
        faces = 6
        seed = None
        return (number, faces, seed)
