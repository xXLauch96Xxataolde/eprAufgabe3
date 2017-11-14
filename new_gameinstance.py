import main
from player import Player


def game_inst():
	print("Do you wish to configure your own dice(s). (y/n)")
	inp = input()
	if (inp == "y"):		
		while (True):
			print("Great. How many dices? 1-99 are possible")
			inp = input()
			try:
				inp = int(inp)
				if (0 < inp and inp < 100):
					"Great"
					break
				else:
					print("Too many dices. Repeat")
			except (ValueError, IndexError):
				print("Unreadable")

	elif(inp == "x"):
		print("Ok. 1 dice, 6 faces.")