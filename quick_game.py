import main
from players import Players
import game_instance


def std_player():
    players = []
    p1 = Player("Player 0", score=0, id=0)
    p2 = Player("Player 1", score=0, id=1)
    players.append(p1)
    players.append(p2)
    
    return(players)

    
def std_dice():
    return(roll_dice(number=1, faces=6, seed=None))

    
def roll_dice(number=1, faces=6, seed=None):
    score = []
    output = ""
    for i in range(number):
        random.seed(seed)
        score.append(random.randint(1, faces))
    
    for j in score:
        output = output + str(j) + ","
    
    return output
