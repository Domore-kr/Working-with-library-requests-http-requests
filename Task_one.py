import requests


def intelligence(heroes):
    heroes_int = {}
    for a in heroes:
        page = requests.get(f'https://superheroapi.com/api/2619421814940190/search/{a}')
        intell = page.json()['results'][0]['powerstats']['intelligence']
        heroes_int[a] = intell
    return print(sorted(heroes_int, key=heroes_int.get)[0])


intelligence(['Hulk', 'Captain America', 'Thanos'])
