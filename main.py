"""Docstring: A very short sentence explaining the function. < 79 characters. 

Additional information if required and more infos. Complete sentences please.
"""

from math import sqrt, log, e  # an example 
# from numpy import array       #another example for third party module
import random  # example for your own module 
from player import Player
import new_players
import new_gameinstance
import start_game
import quick_game
 
__author__ = "123456: John Cleese, 654321: Terry Gilliam"  # put your data here
__copyright__ = "Copyright 2017/2018 - EPR-Goethe-Uni" 
__credits__ = "If you would like to thank somebody \
              i.e. an other student for her code or leave it out" 
__email__ = "your email address" 

  
def menue():
    print("...................Menue.................")
    print(".........................................")
    print(".1..New Game.............................")
    print(".2..Quick Game 2 Play0rs.................")
    print(".3..Help.................................")
    print(".4..Configure your special/Cheating Dice.")
    print(".5..Exit.................................")
    print(".........................................")
    print(".........................................")


def sixteen_is_dead(players):
    while (True):
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
            help()
        elif (inp == "4"):
            conf_special()
        elif (inp == "5"):
            print("Play again soon. Buy our PC exclusive DLC for 79,99 Euro")
            break;
        else:
            print("No valid Input. Please repeat")
            inp = input()
            
    
  # def role_Cheating_dice():

def main():
    players = []
    sixteen_is_dead(players)


if __name__ == '__main__':
    main()
    
