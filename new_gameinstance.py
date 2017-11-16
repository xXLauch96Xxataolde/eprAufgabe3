import main
from player import Player


def game_inst():
    number = 0
    faces = 0
    seed = 0.0
    print("Do you wish to configure your own dice(s). (y/n)")
    inp = input()
    if (inp == "y"):
        while (True):
            print("Great. How many dices? 1-10 are possible")
            inp = input()
            try:
                inp = int(inp)
                if (0 < inp and inp < 11):
                    print("Great")
                    number = inp
                else:
                    print("Too many dices. Repeat")
                    continue

                print("How many faces per Dice? Faces between 2 and 100.")
                inp = int(input())
                if (1 < inp and inp < 101):
                    print("Great")
                    faces = inp
                else:
                    print("Too many faces. Repeat")
                    continue
                print("Do you want a seed? (y/n)")
                inp = input()
                if (inp =="y"):
                    print("Which seed for pseudo random? Float expected")
                    inp = float(input())
                    seed = inp
                    return (number, faces, seed)
                else:
                    print("Standard Seed=None it is")
                    return (number, faces, None)
                break
            except (ValueError, IndexError):
                print("Unreadable")
    elif (inp == "n"):
        print("Ok. 1 dice, 6 faces. No seed")
        number = 1
        faces = 6
        seed = None
        return (number, faces, seed)
    else:
        print("You must be wasted. Standard Game for you <3")
        number = 1
        faces = 6
        seed = None
        return (number, faces, seed)
