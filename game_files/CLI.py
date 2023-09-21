"""
This file will be the command line interface for the Poeltl duplicate game.
"""
from game import *
from player import *

# First we will begin by letting the user input their information to get started
name = input("Please Enter Your Name:")
p1 = Player(name)

# Next we will start up the game
new_game = Game(p1)

new_game.start_new_round()
