from player import Player

def new_players(players):
    print("Category choosen: New Game")
    print("Please enter the number of participants")
    inp = input()
    while (True):
        try:
            inp = int(inp)
            break
        except (ValueError, IndexError):
            print("No valid Input. Please repeat")
    
    for i in range(inp):
        print("Please enter a Name for Player" , i)
        name = input()
        players.append(Player(name, score = 0, id = i))
    
    return(players)  