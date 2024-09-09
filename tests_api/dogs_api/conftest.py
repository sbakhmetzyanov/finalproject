import requests


class DogApiClient:

    def __init__(self,
                 base_url="https://dog.ceo/api",
                 breed="akita"):
        self.breed = breed
        self.base_url = base_url

    def get_list_all_breeds(self):
        response = requests.get(url=f"{self.base_url}/breeds/list/all")
        return response

    def get_random_dog(self):
        response = requests.get(url=f"{self.base_url}/breeds/image/random")
        return response

    def get_random_dog_by_breed(self, breed):
        self.breed = breed
        response = requests.get(url=f"{self.base_url}/breed/{self.breed}/images/random")
        return response

    def get_all_dogs_by_breed(self, breed):
        self.breed = breed
        response = requests.get(url=f"{self.base_url}/breed/{self.breed}/images")
        return response

    def get_list_subbreed(self, breed):
        self.breed = breed
        response = requests.get(url=f"{self.base_url}/breed/{self.breed}/list")
        return response
