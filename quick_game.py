"""Quick Game

This function is used for a quick game. The players are just 2, the one dice is
fixed with 6 sides and a std seed.
"""

import main
from player import Player
import new_gameinstance
import random

__author__ = "6770541: Niels Heissel, 6785468: Robert am Wege"
__copyright__ = "Copyright 2017/2018 - EPR-Goethe-Uni" 
__credits__ = "" 
__email__ = "uni.goethe.horde@gmail.com" 

def std_player():
    """Generates Players 1 and 2."""
    
    players = []
    p1 = Player("Player 1", score=0, id=0)
    p2 = Player("Player 2", score=0, id=1)
    players.append(p1)
    players.append(p2)
    
    return(players)

    
def std_dice():
    """Generates the std dice, 1 -> numbers, 6 -> faces, None -> seed"""
    
    return(1, 6, None)

    
def roll_dice(number=1, faces=6, seed=None):
    """Rolls a dice with said config and seed. Returns a string"""
    
    score = []
    output = ""
    for i in range(number):
        random.seed(seed)
        score.append(random.randint(1, faces))
    
    for j in score:
        output = output + str(j) + ","
    
    return output
