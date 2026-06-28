"""Program name: Match Coin Game
   Autor: Alberto Medina
    Purpose: Define a coin class that representes a tossable coin behavior"""

import random

class Coin:
    """Represents a single coin that can be tossed."""

    def __init__(self):
        """Initialize the coin with a random side facing up."""
        self.__sideup = random.choice(["Heads", "Tails"])

    def toss(self):
        """Randomly sets coin side to be Heads or Tails."""
        random_number = random.randint(0, 1)

        if random_number == 0:
            self.__sideup = "Heads"
        else:
            self.__sideup = "Tails"

    def get_sideup(self):
        """Return the current coin side facing up."""
        return self.__sideup