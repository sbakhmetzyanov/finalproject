import pytest
from jsonschema.validators import validate
from tests_api.dogs_api.conftest import DogApiClient

client = DogApiClient()

schema = {
    "type": "object",
    "properties": {
        "message": {"type": "string"},
        "status": {"const": "success"}
    },
    "required": ["message", "status"]
}


def test_get_list_all_breeds():
    response = client.get_list_all_breeds()
    response_json = response.json()
    assert response.status_code == 200
    assert isinstance(response_json["message"], dict)
    assert response_json["status"] == "success"


def test_get_random_dog():
    response = client.get_random_dog()
    response_json = response.json()
    assert response.status_code == 200
    validate(instance=response_json, schema=schema)


@pytest.mark.parametrize("breed", ["akita", "boxer", "corgi", "labrador", "husky"])
def test_get_random_dog_by_breed(breed):
    response = client.get_random_dog_by_breed(breed)
    response_json = response.json()
    assert response.status_code == 200
    assert isinstance(response_json["message"], str)
    assert response_json["status"] == "success"



def test_get_random_dog_by_breed_negative(breed="incorrect_breed"):
    response = client.get_random_dog_by_breed(breed)
    response_json = response.json()
    assert response.status_code == 404
    assert response_json["message"] == "Breed not found (master breed does not exist)"
    assert response_json["status"] == "error"
    assert response_json["code"] == 404


@pytest.mark.parametrize("breed", ["akita", "boxer", "corgi", "labrador", "husky"])
def test_get_all_dogs_by_breed(breed):
    response = client.get_all_dogs_by_breed(breed)
    response_json = response.json()
    assert response.status_code == 200
    assert isinstance(response_json["message"], list)
    assert response_json["status"] == "success"



def test_get_all_dogs_by_breed_negative(breed="incorrect_breed"):
    response = client.get_random_dog_by_breed(breed)
    response_json = response.json()
    assert response.status_code == 404
    assert response_json["message"] == "Breed not found (master breed does not exist)"
    assert response_json["status"] == "error"
    assert response_json["code"] == 404


@pytest.mark.parametrize("breed", ["akita", "boxer", "corgi", "labrador", "husky"])
def test_get_list_subbreed(breed):
    response = client.get_all_dogs_by_breed(breed)
    response_json = response.json()
    assert response.status_code == 200
    assert isinstance(response_json["message"], list)
    assert response_json["status"] == "success"


def test_get_list_subbreed_negative(breed="incorrect_breed"):
    response = client.get_random_dog_by_breed(breed)
    response_json = response.json()
    assert response.status_code == 404
    assert response_json["message"] == "Breed not found (master breed does not exist)"
    assert response_json["status"] == "error"
    assert response_json["code"] == 404