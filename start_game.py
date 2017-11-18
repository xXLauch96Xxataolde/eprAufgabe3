"""Start Game

Probably the most complex part of our little game. 
Here everything is tied together.
"""

import main
import random
from player import Player
import sys
import time

__author__ = "6770541: Niels Heissel, 6785468: Robert am Wege"
__copyright__ = "Copyright 2017/2018 - EPR-Goethe-Uni" 
__credits__ = "" 
__email__ = "uni.goethe.horde@gmail.com" 

def roll_dice(number=1, faces=6, seed=None):
    """Rolls an adjustable dice. The arguments can be configured as needed"""
    
    score = []
    output = ""
    for i in range(number):
        random.seed(seed)
        score.append(random.randint(1, faces))
    
    for j in score:
        output = output + str(j) + ","
    
    return output


def roll_cheating_dice():  
    """Rolls an special dice. 
    
    The cheating dices can be used during the game. The user only has to write
    cheat into the console. The probabilties are around 14% for every number 
    (1-6) except 3 which has 28% as demanded in the scope.
    """
    animation()
    faces = [1, 2, 3, 3, 4, 5, 6]
    random.shuffle(faces)
    pips = faces[0]
    print("Dice was: ", pips)
    return(pips)
    

def roll_dice_int_builder(score):
    """Builds an int from strings.
    
    Because of reasons unknown, the roll_dice function returns stings. 
    But for calculation reasons, int are far superior. So this func builts a
    sum out of a given string. It is not checked whether the string contains 
    only numbers. because it is unnecessary. This func is only called by
    roll_dice.
    """
    score = score.replace(",", "")  # replaces all comma with nothing
    sum_score = 0
    for i in score:
        sum_score += int(i)
    return(sum_score)

    
def animation():
    """Just a small procedure for printing the random num. looks funny."""
      
    animation = "."
    for i in range(20):
        time.sleep(0.1)
        sys.stdout.write(animation[i % len(animation)])
        sys.stdout.flush()


def we_have_a_looser(div):
    """Looser Procedure.
    
    A procedure for printing the lucky looser. Argument div provides names
    of loosers. We hope our output string is funny in a pub environment, where
    we figuered, 16 is dead is mostly enjoyed. Me might change it, if we design 
    an app for mobile 16 is dead. 
    """
    
    print(div + " congrats, you have the lowest points :)")
    print("Go buy your mates a drink.", "\n" * 3)
    time.sleep(4.2)  # 420 lol
    # do you wish to play again func


def nicer_dicer_and_scorekeeper(player, inst):
    """The nicer dicer is a handy tool, and so it is for our code.
    
    This piece rolls either a dice or a cheating dice, depending on your input.
    In the if request it is determined between the dices, but both parts
    return a sum of what was randomly shuffled.
    """
    
    if (inst == ("ch", "ea", "t")):
        return(roll_cheating_dice())
    else:
        number = inst[0]
        faces = inst[1]
        seed = inst[2]
        animation()
        sum = 0
        sum = roll_dice_int_builder(roll_dice(number, faces, seed))
        print("Dice was:", sum)  
        return(sum)  


def seconds_rule():
    """Procedure for waiting 3 seconds.
    
    If a player has a total score of 10, the game forces a new dice roll.
    Before the force dice role, the game waits 3 seconds. For dramatic effect, 
    we added a count down.  
    """
    
    print("Force dice role due to 10.")
    print("3")
    time.sleep(1)
    print("2")
    time.sleep(1)
    print("1")
    time.sleep(1)
    

def state_check(sum, player, inst):
    """State Check
    
    Here the code checks for the state of the score of a player. If the player
    has encountered a score of 9, he is not allowed to roll the dice anymore, 
    but he is not out. If he didnt scored a total of 9, but 10, the algorithm 
    forces a dice roll. For every score >15 the state check return -100, which 
    is then interpreted by the start function. 
    """
    
    number = inst[0]
    faces = inst[1]
    seed = inst[2]
    if (sum == 9):
        return (9)
    elif (sum == 10):
        seconds_rule()
        pips = roll_dice_int_builder(roll_dice(number, faces, seed))
        sum += pips
        print("Dice was: ", pips)
        print("Total score is:", sum)
        state_check(sum, player, inst)
    elif (sum > 15):
        we_have_a_looser(player.name)
        return (-100)
    else:
        return sum
   

def start(inst, players):
    """Complicated Function. Ugly but helpful.
    
    The start func handles every possible entry user side, into the console.
    The entry cheat, lets you use a cheating dice. 
    Enter lets you shuffle your dice(s), unless you are out for reasons
    mentioned above. 
    If you enter exit, your game exits any time
    if you enter restart, the game restarts. 
    The game_on var is essential, because it shows the state of the running game
    If it is 1 the game is on and there was not yet user found who has lost
    If it is 0 a or a group of losers is printed with the held of the
    we_have_a_looser procedure.
    All funcs and procedures used here are explained in the the docstrings above
    so we avoid the redundancy. 
    """
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
            print("Press <n> to end your round. To exit or restart type 'exit' or 'restart'.")
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
                elif (inp == "cheat"):
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
                elif (inp == "exit"):
                    print("Exiting game.")
                    game_on = 0
                    possible_winners = []
                    break
                elif (inp == "restart"):
                    print("Restarting game.")
                    possible_winners = []

                    return (start(inst, players))

                else:
                    # the code doesnt delete inp the way i want it,
                    # so as the loop continues, else is called
                    print("Unreadable. Again press <enter> or <n>.")
        else:
            print("The End - Buy our exclusive 79,99 Euro DLC \n")
            time.sleep(2)
            break
        
    """The code below, organizes the losers in a list."""
    
    if (len(possible_winners) > 0 and game_on == 1):
        winners = []
        losers = []
        winners = sorted(possible_winners, key=lambda x: x.score)
        person = winners[0]
        for pers in winners:
            if (pers.score == person.score):
                losers.append(pers)
        
        div = ""
        for looser in losers:
            div += looser.name + ", "
        
        we_have_a_looser(div)
