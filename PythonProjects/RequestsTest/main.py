import requests
URL = 'https://api.pokemonbattle.ru/v2'
TOKEN = '3475f50582e5fb1cbbcc05aa36889631'
HEADER = {'Content-Type' : 'application/json', 'trainer_token' : TOKEN}

body_create = {
    "name" : "Слоупок",
    "photo_id" : "79"
}

body_change_name = {
    "pokemon_id" : "262844",
    "name" : "Slowpoke",
    "photo_id" : "79"
}

body_add_in_pokeball = {
    "pokemon_id" : "262844"
}

response_create = requests.post(url = f'{URL}/pokemons', headers = HEADER, json = body_create)
print(response_create.text)

response_change_name = requests.put(url = f'{URL}/pokemons', headers = HEADER, json = body_change_name)
print(response_change_name.text)

response_add_in_pokeball = requests.post(url = f'{URL}/trainers/add_pokeball', headers = HEADER, json = body_add_in_pokeball)
print(response_add_in_pokeball.text)