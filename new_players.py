from player import Player


def new_players(players):
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
        print("Please enter a Name for Player" , i)
        name = input()
        players.append(Player(name, score=0, id=i))
    
    return(players)  
