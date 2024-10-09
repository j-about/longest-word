from longest_word.game import *

# tests/test_game.py
class TestGame:
    def test_game_initialization(self):
        # setup
        game = Game()
        # exercise
        grid = game.grid
        # verify
        assert isinstance(grid, list)
        assert len(grid) == 9
        for letter in grid:
            assert letter in string.ascii_uppercase

    def test_game_is_valid(self):
        game = Game()
        game.grid = list('KWEUEAKRZ')
        word = "EUREKA"
        assert game.is_valid(word) is True

    def test_game_is_invalid(self):
        game = Game()
        game.grid = list('KWEUEAKRZ')
        word = "BAD"
        assert game.is_valid(word) is False

    def test_unknown_word_is_invalid(self):
        """A word that is not in the English dictionary should not be valid"""
        new_game = Game()
        new_game.grid = list('KWIENFUQW') # Force the grid to a test case:
        assert new_game.is_valid('FEUN') is False
