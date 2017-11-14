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
				if (0 < inp and inp < 10):
					print("Great")
					number = inp
				else:
					print("Too many dices. Repeat")
					continue
					
				print("How many faces per Dice. Min 1")
				inp = input()
				inp = int(inp)
				if (1 < inp and inp < 101):
					print("Great")
					faces = inp
				else:
					print("Too many faces. Repeat")
					continue
				
				print("Which seed for pseudo random? Float expected")
				inp = input()
				inp = float(inp)
				seed = inp
				return(number, faces, seed)
				break
			except (ValueError, IndexError):
				print("Unreadable")
	elif(inp == "x"):
		print("Ok. 1 dice, 6 faces. No seed")
		number = 1
		faces = 6
		seed = none
		return(number, faces, seed)
	else:
		print("You must be wasted. Standard Game for 2 <3")
	print("number", number, "faces", faces, "seed", seed)
