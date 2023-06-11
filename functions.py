import requests

all_teams_link = 'https://www.balldontlie.io/api/v1/teams'
all_teams_request = requests.get(all_teams_link).json()
teams = all_teams_request['data']

def all_teams():
    for team in teams:
        print(team['full_name'])

