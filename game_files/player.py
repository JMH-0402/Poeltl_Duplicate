"""
This module contains the player class used to track each players score.
"""


class Player:
    """
    This class is to record players scores and information

    Players will have a score which represents how many levels they were able
    to complete and what players they were able to guess on how many attempts.

    === Attributes ===
    name: the name of the player playing the game
    score: the number of NBA players the player was able to guess
    prev_rounds: the dictionary of NBA players that the player was able to
    guess. The keys in the dictionary are the names of NBA players and they are
    paired with the number of attempts to guess
    """
    name: str
    score: int
    prev_rounds: dict

    def __init__(self, name: str) -> None:
        self.name = name
        self.score = 0
        self.prev_rounds = {}

    def add_score(self, correct_name: str, num_of_tries: int) -> None:
        """
        Adds a point to the players score when the NBA player, correct_name,
        is guessed correctly and adds the player with the number of guesses,
        num_of_tries to the players previous guesses.
        :param correct_name: the correct name of the NBA player
        :param num_of_tries: the number of attempts to guess the NBA player
        """
        self.score += 1
        self.prev_rounds[correct_name] = num_of_tries

    def failure(self, correct_name: str) -> None:
        """
        Adds the name of the NBA player, correct_name, to the players history.
        This happens when the player is not able to correctly guess the NBA
        players name.
        :param correct_name: The correct name of the NBA player
        """
        self.prev_rounds[correct_name] = 0

