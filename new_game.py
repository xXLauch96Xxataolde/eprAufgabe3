def new_game(players):
    print("Category choosen: New Game")
    print("Please enter the number of teilnehmer")
    inp = input()
    try:
        while(True):
            inp = int(inp)
            break
        expect (ValueError, IndexError):
            print("No valid Input. Please repeat")
    
    for i in inp:
        print("Please enter a Name for Player" , i)
        name = input()
        p[i] = Player(name, score = 0, id = i)
        p[i].pri