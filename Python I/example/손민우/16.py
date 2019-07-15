def roll():
	from random import randint
	return randint(1,6)


def dice_game():
	strikes = 0
	winnings = 0
	while strikes < 3:
		die1 = roll()
		die2 = roll()
		if die1 == die2:
			strikes = strikes +1
		else:
			winnings = winnings + die1 + die2
	return winnings