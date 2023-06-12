import requests

all_teams_link = 'https://www.balldontlie.io/api/v1/teams'
all_teams_request = requests.get(all_teams_link).json()
teams = all_teams_request['data']




list_cities = []
for team in teams:
    list_cities.append(team['city'])


list_names = []
for team in teams:
    list_names.append(team['name'])





def all_teams():
    for team in teams:
        print(team['full_name'])


# Alterando o nome do time Clippers onde a cidade consta LA para Los Angeles
teams[12] = {'id': 13, 'abbreviation': 'LAC', 'city': 'Los Angeles', 'conference': 'West', 'division': 'Pacific', 'full_name': 'LA Clippers', 'name': 'Clippers'}






def search_city(city):
    if city in list_cities:
        for team in teams:
            if team['city'] == city:
                print(f"City: {team['city']}\n"
                      f"Conference: {team['conference']}\n"
                      f"Division: {team['division']}\n"
                      f"Name: {team['name']}\n"
                      f"Full name: {team['full_name']}\n")
            else:
                pass
    else:
        print(f'The city {city} has not a NBA team.')

def search_name(name):
    if name in list_names:
        for team in teams:
            if team['name'] == name:
                print(f"City: {team['city']}\n"
                      f"Conference: {team['conference']}\n"
                      f"Division: {team['division']}\n"
                      f"Name: {team['name']}\n"
                      f"Full name: {team['full_name']}\n")
            else:
                pass
    else:
        print(f"Doesn't exist NBA team with called {name}.")