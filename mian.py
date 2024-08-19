import requests

URL = "https://api.pokemonbattle.ru/v2"
TOKEN = "your_token_must_be_here" #PASTE YOUR TOKEN HERE
HEADER = {"Content-Type": "application/JSON", "trainer_token": TOKEN}
body_create_pokemon = {"name": "generate", "photo_id": -1}

response_create_pokemon = requests.post(
    url=f"{URL}/pokemons", headers=HEADER, json=body_create_pokemon
)
pokemon_id = response_create_pokemon.json()["id"]
print(response_create_pokemon.text)

body_change_name_pokemon = {"pokemon_id": pokemon_id, "name": "Dudochnik"}

response_change_name_pokemon = requests.patch(
    url=f"{URL}/pokemons", headers=HEADER, json=body_change_name_pokemon
)
print(response_change_name_pokemon.text)


body_add_pokemon_to_pokeball = {"pokemon_id": pokemon_id}

response_add_pokemon_to_pokeball = requests.post(
    url=f"{URL}/trainers/add_pokeball",
    headers=HEADER,
    json=body_add_pokemon_to_pokeball,
)
print(response_add_pokemon_to_pokeball.text)
