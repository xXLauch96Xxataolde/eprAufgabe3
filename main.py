"""Main or Core Function 

This function handles the whole program
During the whole dev process of the code, we always kept an eye on naming 
the variables, datatypes, objects and so on very descriptive so the code is
easily to service and to understand. 
"""

import random
from player import Player
import new_players
import new_gameinstance
import start_game
import quick_game
import time
import help_menue

__author__ = "6770541: Niels Heissel, 6785468: Robert am Wege"
__copyright__ = "Copyright 2017/2018 - EPR-Goethe-Uni" 
__credits__ = "" 
__email__ = "uni.goethe.horde@gmail.com" 

  
def menue():
    """Just a small procedure for printing a overview of game funcs."""
    
    print(".................Menu....................")
    print(".........................................")
    print(".1..New Game.............................")
    print(".2..Quick Game 2 Players.................")
    print(".3..Help.................................")
    print(".4..Exit.................................")
    print(".........................................")


def sixteen_is_dead(players):
    """Game Algorithm. 
    
    As mentioned in the description of the exercise, this is the key part of
    he whole game. Due to more readable of this function, a lot of help 
    functions and procedures are outsourced. 
    players = new_players.new_players(players) this calls a new module and 
    saves the new players as objects in a list. 
    inst = new_gameinstance.game_inst() this establishes a new game instances 
    with configured dices, faces of dices, and seeds. 
    start_game.start(inst, players) start the game
    """
    
    while (True):
        print("Going back to menu...")
        time.sleep(0.5)
        print("\n"*50)
        time.sleep(0.5);
        menue()
        inp = input()
        if (inp == "1"):
            players = new_players.new_players(players)
            inst = new_gameinstance.game_inst()
            start_game.start(inst, players)
        elif (inp == "2"):
            # print("category choosen" insert
           players = quick_game.std_player()
           inst = quick_game.std_dice()
           start_game.start(inst, players)
        elif (inp == "3"):
            help_menue.helpings()  # time.sleep mhhmmmm
            inp = input()
        elif (inp == "4"):
            print("Play again soon. Buy our PC exclusive DLC for 79,99 Euro")
            break;
        else:
            print("No valid Input. Please repeat")
            
    
def main():
    """Starts everything."""
    
    players = []
    sixteen_is_dead(players)


if __name__ == '__main__':
    main()
    
