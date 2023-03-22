import requests
import random
from faker import Faker


BASE_URL = 'https://gorest.co.in//public/v2/users'
TOKEN = '1c173e094ebdb2a1d204e3ebb96906bceace8e74a64287688220f5c173c2541d'
HEADERS = {'Authorization': f'Bearer {TOKEN}'}

fake = Faker()

user_data = {
    "name": fake.name(),
    "email": fake.email(),
    "gender": random.choice(["male", "female"]),
    "status": random.choice(["active", "inactive"])
}

def test_delete_user():
    # Send request to create new user
    response_post = requests.post(BASE_URL, headers=HEADERS, json=user_data)
    assert response_post.status_code == 201, f"Expected status code 201, but got {response_post.status_code}"

    # Get the ID of the created user
    user_id = response_post.json()["id"]

    response_delete = requests.delete(f"{BASE_URL}/{user_id}", headers=HEADERS)

    # Assert response status code is 204 (no content)
    assert response_delete.status_code == 204, f"Expected status code 204, but got {response_delete.status_code}"

    # Send GET request to check that user is no longer in the list
    response_get = requests.get(BASE_URL + f"/{user_id}", headers=HEADERS)

    # Assert response status code is 404 (not found)
    assert response_get.status_code == 404, f"Expected status code 404, but got {response_get.status_code}"