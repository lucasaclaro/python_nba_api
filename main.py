import requests
from functions import *

print('All NBA teams:\n')
all_teams()
print('')
print('***' * 20)


city = input('Type it name of the city: ')
search_city(city)
print('')
print('***' * 20)

name = input('Type it a name to search if exist a NBA team: ')
search_name(name)


#print(all_teams_request)



#if request_json['data'][0]['city'] == 'Atlanta':
#    print('Yes')
#else:
#    print('None NBA team in X city.')

#print(request_json['data'][0]['city'])
