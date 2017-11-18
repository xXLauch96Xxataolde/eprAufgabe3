"""New Player 

Here the code generates the dialogue for building a new player object which is 
done in the Player class. We paid attention to some sensibility, e.g. since
a game of 16 is dead would be useless to play alone, we ask the user to enter
at least 2 players. Wrong inputs are caught.
"""

from player import Player

__author__ = "6770541: Niels Heissel, 6785468: Robert am Wege"
__copyright__ = "Copyright 2017/2018 - EPR-Goethe-Uni" 
__credits__ = "" 
__email__ = "uni.goethe.horde@gmail.com" 

def new_players(players):
    """Gathers the information for new player objects."""
    
    players = []
    print("Category chosen: New Game")    
    while (True):
        print("Please enter the number of participants")
        inp = input()
        try:
            inp = int(inp)
            if (inp > 1):
                print("Great")
                break
            else:
                print("SAD! Invite one or more friends")
                continue
            
        except (ValueError, IndexError):
            print("No valid Input. Please repeat")
    
    for i in range(inp):
        print("Please enter a Name for Player", i + 1)
        while True:
            inp = input()
            inp = inp.strip()
            if (inp != ""):  # there was a more elegant way
                players.append(Player(inp, score=0, id=i))
                break
            else:
                print("You didn't type anything! Try again.")
    
    return(players)  
