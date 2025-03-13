import requests
import pytest

URL = 'https://api.pokemonbattle.ru/v2'
TOKEN = '3475f50582e5fb1cbbcc05aa36889631'
HEADER = {'Content-Type' : 'application/json', 'trainer_token' : TOKEN}
TRAINER_ID = 23467

def test_status_code():
    response = requests.get(url = f'{URL}/pokemons', params = {'trainer_id' : TRAINER_ID})
    assert response.status_code == 200

def test_trainer_name():
    response_id = requests.get(url = f'{URL}/me', headers = HEADER, params = {'trainer_id' : TRAINER_ID})
    assert response_id.json()["data"][0]["trainer_name"] == 'Vlad g'