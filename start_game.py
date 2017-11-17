import main
import random
from player import Player
import sys
import time


def roll_dice(number=1, faces=6, seed=None):  # returns String
    
    score = []
    output = ""
    for i in range(number):
        random.seed(seed)
        score.append(random.randint(1, faces))
    
    for j in score:
        output = output + str(j) + ","
    
    return output


def roll_cheating_dice():  
    
    faces = [1, 2, 3, 3, 4, 5, 6]
    random.shuffle(faces)
    pips = faces[0]
    return(pips)
    

def roll_dice_int_builder(score):
    
    score = score.replace(",", "")  # replaces all comma with nothing
    sum_score = 0
    for i in score:
        sum_score += int(i)
    return(sum_score)

    
def animation():
    
    animation = "."
    for i in range(20):
        time.sleep(0.1)
        sys.stdout.write(animation[i % len(animation)])
        sys.stdout.flush()


def we_have_a_looser(player):
    
    print(player.name, "Congrats, you are a Looser :) Go buy your mates a drink.", "\n")
    # do you wish to play again func?


def nicer_dicer_and_scorekeeper(player, inst):
    
    if (inst == ("ch", "ea", "t")):
        return(roll_cheating_dice())
    else:
        number = inst[0]
        faces = inst[1]
        seed = inst[2]
        #animation()
        sum = 0
        sum = roll_dice_int_builder(roll_dice(number, faces, seed))
        print("Dice was:", sum)  
        return(sum)  


def seconds_rule():
    print("Force dice role due to 10.")
    print("3")
    time.sleep(1)
    print("2")
    time.sleep(1)
    print("1")
    time.sleep(1)
    

def state_check(sum, player, inst):
    number = inst[0]
    faces = inst[1]
    seed = inst[2]
    if (sum == 9):
        return (9)
    elif (sum == 10):
        seconds_rule()
        sum += roll_dice_int_builder(roll_dice(number, faces, seed))
        print("Total score is:", sum)
        state_check(sum, player, inst)
        return(sum)
    elif (sum > 15):
        we_have_a_looser(player)
        return (-100)
    else:
        print(sum)
        return sum

   

def start(inst, players):
    number = inst[0]
    faces = inst[1]
    seed = inst[2]
    cheating_inst = ("ch", "ea", "t")
    game_on = 1
    possible_winners = []
    for player in players:
        sum = 0
        if (game_on == 1):
            print(player.name,
                  "it's your turn. Press <enter> to gamble")
            print("Press <n> to end your round.")
            while(True):
                inp = input()
                if (inp == ""):
                    sum += nicer_dicer_and_scorekeeper(player, inst)
                    print("Total score is:", sum)
                    a = state_check(sum, player, inst)
                    sum = a
                    if (a == 9):
                        player.score = sum
                        possible_winners.append(player)
                        break
                    elif (a == -100):
                        game_on = 0
                        player.score = sum
                        possible_winners.append(player)
                        break
                    continue
                if (inp == "cheat"):
                    sum += nicer_dicer_and_scorekeeper(player, cheating_inst)
                    print("Total score is:", sum)
                    a = state_check(sum, player, inst)
                    sum = a
                    if (a == 9):
                        player.score = sum
                        possible_winners.append(player)
                        break
                    elif (a == -100):
                        game_on = 0
                        player.score = sum
                        possible_winners.append(player)
                        break
                    continue
                elif (inp == "n"):
                    player.score = sum
                    possible_winners.append(player)
                    break
                else:
                    # the code doesnt delete inp the way i want it,
                    # so as the loop continues, else is called
                    print("Unreadable. Again press <enter> or <n>.")
        else:
            print("The End - Buy our exclusive 79,99 Euro DLC \n*3")
            break
    
    if (len(possible_winners) > 0 and game_on == 1):
        print(possible_winners[0].printer())
        print(possible_winners[1].printer())
        winners = []
        winners = sorted(possible_winners, key=lambda x: x.score)
        print(winners[0].name, "you have the lowest points.")
        we_have_a_looser(winners[0])
        
