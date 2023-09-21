import requests
from bs4 import BeautifulSoup
import pandas as pd
import Constants

# Url template for each team. Replace {} with the 3 letter team code.
url_start = "https://www.basketball-reference.com/teams/{}/2024.html"

# Loop to start accessing each teams page and writing new files into
# rosters_info directory. Each team gets its own file.
for division in Constants.DIVISIONS:
    for team in division:
        url = url_start.format(team)
        data = requests.get(url)
        with open("rosters_info/{}.html".format(team), "w+") as f:
            f.write(data.text)

# Taking each team's roster table out from their respective html page
rosters = []
for division in Constants.DIVISIONS:
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
    roster.to_csv("rosters_info/{}.csv".format(Constants.DIVISIONS[div][team]))
    team += 1

# Creating a new csv file with only player names
created = False
for division in Constants.DIVISIONS:
    for team in division:
        if not created:
            df = pd.read_csv('rosters_info/{}.csv'.format(team))
            df = df[["Player"]]
            df.to_csv('player_names.csv', index=False)
            created = True
        else:
            df = pd.read_csv('rosters_info/{}.csv'.format(team))
            df = df[["Player"]]
            df.to_csv('player_names.csv', mode='a', index=False, header=False)




