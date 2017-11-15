import main
import random
from player import Player
import sys
import time


def roll_dice(number=1, faces=6, seed=None):
    score = []
    output = ""
    for i in range(number):
        random.seed(seed)
        score.append(random.randint(1, faces))
    
    for j in score:
        output = output + str(j) + ","
    
    return output


def scorekeeper(score):
    score = score.replace(",", "")  # replaces all comma with nothing
    sum_score = 0
    for i in score:
        sum_score += int(i)
    return(sum_score)

    
def animation():
    animation = "."
    for i in range(30):
        time.sleep(0.1)
        sys.stdout.write(animation[i % len(animation)])
        sys.stdout.flush()


def start(inst, players):
    number = inst[0]
    faces = inst[1]
    seed = inst[2]
    for player in players:
        sum = 0
        print("Player", player.name, "it's your turn. Press enter to gamble")
        print("Press n to end your round")
        while(True):
            inp = input()
            if (inp == ""):
                animation()
                score = roll_dice(number, faces, seed)
                sum += scorekeeper(score)
                print("sum", sum)
                
            elif (inp == "n"):
                break
            else:
                print("Unreadable. Again")
