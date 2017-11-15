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


def we_have_a_looser(player):
    print(player.name, "Congrats, you are a Looser. Go buy your mates a drink") 


def nicer_dicer_and_scorekeeper(player, inst):
    number = inst[0]
    faces = inst[1]
    seed = inst[2]
    animation()
    sum = 0
    sum = scorekeeper(roll_dice(number, faces, seed))
    print("Dice was:", sum)  
    return(sum)  


def state_check(sum, player):
    if (sum == 9):
        we_have_a_looser(player)
        sum = -1
        return (sum)
    elif (sum == 10):
        print("Force dice role due to 10.")
        sum += scorekeeper(roll_dice(number, faces, seed))
        state_check(sum)
        retrn(sum)
    elif (sum == 16):
        we_have_a_looser(player)
        sum = -1
        return (sum)
    return sum
   

def start(inst, players):
    number = inst[0]
    faces = inst[1]
    seed = inst[2]
    sum = 0
    for player in players:
        print("Player", player.name, "it's your turn. Press enter to gamble")
        print("Press n to end your round")
        while(True):
            inp = input()
            if (inp == ""):
                sum += nicer_dicer_and_scorekeeper(player, inst)
                print(sum)
                state_check(sum, player)                
                if (sum == -1):
                    break
            elif (inp == "n"):
                player.score = sum
                sum = 0
                break
            else:
                print("Unreadable. Again")
    
    for player in players:
        print(player)
