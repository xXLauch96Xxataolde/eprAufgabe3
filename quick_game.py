import main
from player import Player
import new_gameinstance
import random


def std_player():
    players = []
    p1 = Player("Player 1", score=0, id=0)
    p2 = Player("Player 2", score=0, id=1)
    players.append(p1)
    players.append(p2)
    
    return(players)

    
def std_dice():
    return(1, 6, None)

    
def roll_dice(number=1, faces=6, seed=None):
    score = []
    output = ""
    for i in range(number):
        random.seed(seed)
        score.append(random.randint(1, faces))
    
    for j in score:
        output = output + str(j) + ","
    
    return output
