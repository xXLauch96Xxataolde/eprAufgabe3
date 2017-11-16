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
        print("Please enter a Name for Player", i + 1)
        while True:
            name_inp = input()
            name_inp = str(name_inp)
            if name_inp != "" and name_inp != " ":
                name = name_inp
                players.append(Player(name, score=0, id=i))
                break
            else:
                print("You didn't type anything! Try again.")
    
    return(players)  
