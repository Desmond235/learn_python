import  requests

base_url = "https://pokeapi.co/api/v2/"

def get_pokemon_info(name):
    url = f'{base_url}/pokemon/{name}'
    try:
        response = requests.get(url)
        if response.status_code == 200:
            pokemon_data =response.json()
            return  pokemon_data
        else:
            print(f'failed to retrieve data {response.status_code}')
    except ConnectionError:
        print("No internet connection")

pokemon_name = "Typhlosion"
pokemon_info = get_pokemon_info(pokemon_name)

if pokemon_info:
    print(f'Name: {pokemon_info['name']}')
    print(f'id: {pokemon_info['id']}')
    print(f'height: {pokemon_info['height']}')
    print(f'weight: {pokemon_info['weight']}')