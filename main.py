from games.dice import RegularDice, DoubleDice
from games.game import Game


# prompt the user to specify the dice
max_score = int(input("Max score for the Dice?\n"))

# create an instance from the Dice (class)
my_dice = DoubleDice(max_score)


# prompt the user
number_turns = int(input("How many turns?:\n"))


# initialize the Game
my_game = Game(number_turns, my_dice)


# play the game
while my_game.status == "In progress":
    take_turn = input("Take turn.")
    my_game.take_turn()
