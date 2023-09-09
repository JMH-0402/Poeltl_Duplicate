# This will be the class containing the rounds of each game
from roster_files.random_player_generator import *

Num_of_players = 538


class Round:
    """
    Each round of a game, where there is a correct NBA player and the player has
    5 tries to get each player. With each guess, the player will be given
    information based on their last guess. If the guessed NBA player plays in
    the same team, has the same height, or has the same weight, the player will
    be told that the correct component is green. if the guessed NBA player plays
    in the same division, is within 2 inches of the correct player, or is within
    15 pounds, then they will be told that they are close to the answer with
    the close component being yellow

    === Attributes ===
    correct_player: The correct NBA player that the player tries to guess
    """
    correct_player: list

    def __init__(self):
        self.correct_player = PlayerGenerator()

    def name_correctness(self, guess: str) -> bool:
        """
        Returns whether or not the guess is correct
        :param guess: The guess that the player provides
        :return: Whether or not the guess is correct or not
        """
        if guess == self.correct_player:
            return True
        return False

    def height_guess(self, guess: str) -> str:
        """
        Returns "correct" if the height of the guessed player is the same as the
        correct_player. Returns "close" if the height of the guessed player is
        2 inches off of the correct_player. Returns "incorrect" if the height of
        the guessed player is off by more than 2 inches.
        :param guess: The guess that the player provides
        """
        guess_player = PlayerFinder(guess)
        if guess_player[2] == self.correct_player[2]:
            return "correct"
        elif abs(int(guess_player[2][2])-int(self.correct_player[2][2])) < 3:
            return "close"
        else:
            return "incorrect"

    def position_guess(self, guess: str) -> str:
        """
        Return "correct" if the position of the guessed player is the same as
        the correct_player. Returns "close" if either the guessed player or the
        correct player or both have two positions and they both have one
        position in common. Returns "incorrect" if the position of
        the guessed player is wrong.
        :param guess: The name of the player
        """
        guess_player = PlayerFinder(guess)
        if guess_player[1] == self.correct_player[1]:
            return "correct"
        elif len(guess_player[1]) > 1:



if __name__ == '__main__':
    player = Round()


