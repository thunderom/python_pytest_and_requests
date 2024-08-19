import requests
import pytest
from dotmap import DotMap

URL = "https://api.pokemonbattle.ru/v2"
TOKEN = "your_token_must_be_here" #PASTE YOUR TOKEN HERE
HEADER = {"Content-Type": "application/JSON", "trainer_token": TOKEN}
TRAINER_ID = "your_trainer_id_must_be_here" #PASTE YOUR TRAINER_ID HERE
TRAINER_NAME = "your_trainer_name_must_be_here" #PASTE YOUR TRAINER_NAME HERE

def test_get_trainers():
    response_get_trainers = requests.get(url=f"{URL}/trainers", headers=HEADER)
    assert response_get_trainers.status_code == 200

def test_get_my_trainer_name():
    response_get_my_trainer_name = requests.get(
        url=f"{URL}/trainers", headers=HEADER, params={"trainer_id": TRAINER_ID}
    )
    object = DotMap(response_get_my_trainer_name.json())
    assert object.data[0].trainer_name == TRAINER_NAME

@pytest.mark.parametrize(
    "key, value",
    [
        ("id", TRAINER_ID),
        ("trainer_name", TRAINER_NAME),
        ("level", "1"),
        ("get_history_battle", "0"),
        ("is_premium", False),
        ("premium_duration", 0),
        ("city", "новосибирск"),
    ],
)
def test_parametrize(key, value):
    response_get_my_trainer = requests.get(
        url=f"{URL}/trainers", headers=HEADER, params={"trainer_id": TRAINER_ID}
    )
    object = DotMap(response_get_my_trainer.json())
    item = object.data[0]
    assert getattr(item, key) == value
