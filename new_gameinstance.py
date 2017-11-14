import main
from player import Player


def game_inst():
	print("Do you wish to configure your own dice(s). (y/n)")
	inp = input()
	if (inp == "y"):
		print("Great. How many dices? 1-99 is possible")
		inp = input()
		while (True):
			try:
				inp = int(inp)
				
				if (1 <= inp or inp <= 99):
					break
				print("jop")
			except (ValueError, IndexError):
				print("Unreadable")
	elif(inp == "x"):
		print("Ok. 1 dice, 6 faces.")