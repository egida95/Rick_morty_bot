import requests


def get_list_location() -> list:
    url = 'https://rickandmortyapi.com/api/location'
    r = requests.get(url)
    data = r.json()['results']
    return data

def get_location_name() -> list:
    data = []
    for i in get_list_location():
        data.append(i['name'])
    return data 

def get_location_data(name: str):
    locations = {i['name']: i['id'] for i in get_list_location()}
    loc_id = locations[name]
    url = f'https://rickandmortyapi.com/api/location/{loc_id}'
    data = requests.get(url).json()
    return data

# print(get_location_data('Anatomy Park'))

def parse_data(name: str) -> str:
    data = get_location_data(name)
    residents = data['residents']
    text = f'''
id: {data['id']}
name: {data['name']}
type:{data['type']}
dimension:{data['dimension']}
created:{data['created']}
residents:{lol(name)}
    
    '''
    return text

def lol(name:list)->list:
    data = get_location_data(name)
    residents = data['residents']
    a=[]
    for i in residents:
        r=requests.get(i).json()
        a.append(r['name'])
        
    return a
        


# print(lol('Earth (C-137)'))
