# This will be the file of the main game.
from player import Player


class Game:
    """
    This class will represent the game.

    === Attributes ===
    player: the player of the game
    """
    player: Player(str)

    def __init__(self, player: Player(str)) -> None:
        self.player = player

    def start_round(self) -> None:
