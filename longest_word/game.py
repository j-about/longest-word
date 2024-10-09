# pylint: disable=missing-docstring
# pylint: disable=too-few-public-methods
import string
import random

class Game:
    def __init__(self) -> list:
        """Attribute a random grid to size 9"""
        self.grid = random.choices(string.ascii_uppercase, k=9)

    def is_valid(self, word: str) -> bool:
        """Return True if and only if the word is valid, given the Game's grid"""
        tmp_grid = self.grid.copy()
        for letter in word:
            if letter not in tmp_grid:
                return False
            tmp_grid.remove(letter)
        return True
