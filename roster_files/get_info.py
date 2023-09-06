import requests
from bs4 import BeautifulSoup
import pandas as pd


# Eastern conference divisions
atlantic_div = ['BOS', 'BRK', 'TOR', 'NYK', 'PHI']
central_div = ['CLE', 'CHI', 'DET', 'IND', 'MIL']
south_east_div = ['ATL', 'CHO', 'MIA', 'ORL', 'WAS']

# Western conference divisions
north_west_div = ['DEN', 'MIN', 'POR', 'OKC', 'UTA']
pacific_div = ['GSW', 'LAC', 'LAL', 'PHO', 'SAC']
south_west_div = ['DAL', 'HOU', 'MEM', 'NOP', 'SAS']

# all teams in one list.
divisions = [atlantic_div, central_div, south_east_div, north_west_div,
             pacific_div, south_west_div]

# Url template for each team. Replace {} with the 3 letter team code.
url_start = "https://www.basketball-reference.com/teams/{}/2024.html"

# Loop to start accessing each teams page and writing new files into
# rosters_info directory. Each team gets its own file.
for division in divisions:
    for team in division:
        url = url_start.format(team)
        data = requests.get(url)
        with open("rosters_info/{}.html".format(team), "w+") as f:
            f.write(data.text)

# Taking each team's roster table out from their respective html page
rosters = []
for division in divisions:
    for team in division:
        with open("rosters_info/{}.html".format(team)) as f:
            page = f.read()
        soup = BeautifulSoup(page, "html.parser")
        roster_table = soup.find(id="roster")
        roster = pd.read_html(str(roster_table))[0]
        rosters.append(roster)


# Creating a new csv file with the rosters of each team
div = 0
team = 0
for roster in rosters:
    if team > 4:
        div += 1
        team = 0
    if div > 5:
        break
    roster.to_csv("rosters_info/{}.csv".format(divisions[div][team]))
    team += 1
