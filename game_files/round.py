# This will be the class containing the rounds of each game
from roster_files.random_player_generator import PlayerGenerator

Num_of_players = 538


class Round:
    """
    Each round of a game, where there is a correct NBA player and the player has
    5 tries to get each player. With each guess, the player will be given
    information based on their last guess. If the guessed NBA player plays in
    the same team, has the same height, or has the same weight, the player will
    be told that the correct component is green. if the guessed NBA player plays
    in the same division, is within 3 inches of the correct player, or is within
    15 pounds, then they will be told that they are close to the answer with
    the close component being yellow

    === Attributes ===
    correct_player: The correct NBA player that the player tries to guess
    """
    correct_player: str

    def __init__(self):
        self.correct_player = PlayerGenerator()

    def height_correctness(self, guess: str) -> bool:
        """
        Returns whether or not the guess is correct
        :param guess:
        :return:
        """

if __name__ == '__main__':
    player = Round()


