# This file will generate random NBA players
import Constants
import random
import csv


def PlayerGenerator() -> list:
    """
    Generates a random NBA player then returns the NBA player in a list where
    the first index is the player name, second index is the player position,
    third index is the players height, and the last index is the weight.
    :return: The NBA player
    """
    player = []
    with open('player_names.csv', 'r') as file_obj:

        reader_obj = csv.DictReader(file_obj)

        n = random.randint(1, Constants.NUM_OF_PLAYERS)
        i = 1
        for row in reader_obj:
            if i == n:
                player.append(row["Player"])
            i += 1

    for division in Constants.DIVISIONS:
        for team in division:
            with open('rosters_info/{}.csv'.format(team), 'r') as file_obj:
                reader_obj = csv.DictReader(file_obj)

                for row in reader_obj:
                    if row["Player"] == player[0]:
                        player.append(row["Pos"])
                        player.append(row["Ht"])
                        player.append(row["Wt"])

    return player


def PlayerFinder(player_name: str) -> list:
    """
    Returns the player_name's name, position, height, and weight in a list
    :param player_name: the name of the player
    :return: The players information
    """
    player = [player_name]
    for division in Constants.DIVISIONS:
        for team in division:
            with open('rosters_info/{}.csv'.format(team), 'r') as file_obj:
                reader_obj = csv.DictReader(file_obj)

                for row in reader_obj:
                    if row["Player"] == player_name:
                        player.append(row["Pos"])
                        player.append(row["Ht"])
                        player.append(row["Wt"])

    print(player)
    return player


if __name__ == '__main__':
    PlayerFinder("Jeff Green")
