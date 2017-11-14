import main
from player import Player


def game_inst():
	print("Do you wish to configure your own dice(s). (y/n)")
	inp = input()
	if (inp == "y"):
		print("Great. How many dices? 1-99 are possible")
		inp = input()
		while (True):
			try:
				inp = int(inp)
				break
			except (ValueError, IndexError):
				print("Unreadable")
		if (1 <= inp or 99 < inp):
			print("Dice number out of bound")
			
	elif(inp == "x"):
		print("Ok. 1 dice, 6 faces.")