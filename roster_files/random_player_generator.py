# This file will generate random NBA players
import Constants
import random
import csv


# This function will generate a random NBA player
def PlayerGenerator() -> str:
    with open('player_names.csv', 'r') as file_obj:

        reader_obj = csv.DictReader(file_obj)

        n = random.randint(1, Constants.NUM_OF_PLAYERS)

        i = 1
        for row in reader_obj:
            if i == n:
                return row['Player']
            i += 1


if __name__ == '__main__':
    PlayerGenerator()
