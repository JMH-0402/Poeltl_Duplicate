# This will be the file of the main game.
from player import Player
from round import *
from roster_files.random_player_generator import PlayerFinder


class Game:
    """
    This class will represent the game.

    === Attributes ===
    player: the player of the game
    """
    player: Player(str)

    def __init__(self, game_player: Player(str)) -> None:
        self.player = game_player

    def start_round(self) -> str:
        """
        Starts a new round of the game. Runs the round for 5 attempts or when
        the player guesses the correct player. Will return "Correct!" if the
        player manages to guess the NBA players name or will return "Incorrect!"
        if the player does not finish the round.
        :return: The result of the round
        """
        game_round = Round()
        final = []
        i = 1
        while i < 6:
            guess = input("Enter your guess: ")
            guess_info = PlayerFinder(guess)
            if len(guess_info) == 1:
                print("Incorrect Spelling")
                continue
            name_correctness = game_round.name_correctness(guess)
            height_hint = game_round.height_guess(guess)
            weight_hint = game_round.weight_guess(guess)
            position_hint = game_round.position_guess(guess)

            if name_correctness and position_hint == "correct" and \
                    height_hint == "correct" and weight_hint == "correct":
                print("Correct")
                return "Correct"

            cur_round = {"name:": guess,
                         "position: {}".format(guess_info[1]): position_hint,
                         "height: {}".format(guess_info[2]): height_hint,
                         "weight: {}".format(guess_info[3]): weight_hint}
            print(cur_round)
            final.append(cur_round)
            i += 1

        print("Incorrect: The correct player was {}".format(
            game_round.correct_player[0]))
        return "Incorrect: The correct player was {}".format(
            game_round.correct_player[0])


if __name__ == "__main__":
    player1 = Player("Jeong Min")
    a = Game(player1)
    a.start_round()
