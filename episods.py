import requests

def get_episode() -> list:
    url = 'https://rickandmortyapi.com/api/episode'
    r = requests.get(url)
    data = r.json()['results']
    return data

def get_episode_data(name: str):
    episode = {i['name']: i['id'] for i in get_episode()}
    episode1 = episode[name]
    url = f'https://rickandmortyapi.com/api/episode/{episode1}'
    data = requests.get(url).json()
    return data 


def get_air_date() -> list:
    return [i['air_date'] for i in get_episode()]

def get_names() -> list:
    return [i['name'] for i in get_episode()]


# print(get_episode_data("Ricksy Business"))


def get_episode_names(name:str) -> list:
        data = get_episode_data(name) 
        text = f'''\
        \nid: {data['id']}
        \nname: {data['name']}
        \nair_date:{data['air_date']}
        \ncharacters:{data['characters']}

    '''
        return text 
    
# print(get_episode_names('Meeseeks and Destroy'))

