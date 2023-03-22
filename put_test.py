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

def test_update_user():
    # Send request to create new user
    response = requests.post(BASE_URL, headers=HEADERS, json=user_data)
    assert response.status_code == 201, f"Expected status code 201, but got {response.status_code}"

    # Get the ID of the created user
    user_id = response.json()["id"]

    # Get current user data
    response = requests.get(f"{BASE_URL}/{user_id}", headers=HEADERS)
    assert response.status_code == 200, f"Expected status code 200, but got {response.status_code}"
    current_data = response.json()

    # Update user data
    updated_data = {
        "name": fake.name(),
        "gender": random.choice(["male", "female"]),
        "status": random.choice(["active", "inactive"])
    }
    response = requests.put(f"{BASE_URL}/{user_id}", headers=HEADERS, json=updated_data)

    # Assert response status code is 200
    assert response.status_code == 200, f"Expected status code 200, but got {response.status_code}"

    # Update expected data with current data and updated data
    expected_data = {
        "id": user_id,
        "email": current_data["email"],
        "name": updated_data["name"],
        "gender": updated_data["gender"],
        "status": updated_data["status"]
    }

    # Assert response matches expected data
    response_data = response.json()
    assert response_data == expected_data, f"Expected response data {expected_data}, but got {response_data}"

    # Send request to get all users and assert updated user is in the list
    response = requests.get(BASE_URL, headers=HEADERS)
    assert response.status_code == 200, f"Expected status code 200, but got {response.status_code}"
    user_list = response.json()
    updated_user = next((user for user in user_list if user["id"] == user_id), None)
    assert updated_user is not None, f"Expected to find user with ID {user_id} in list"
    assert updated_user["name"] == updated_data[
        "name"], f"Expected name to be {updated_data['name']}, but got {updated_user['name']}"
    assert updated_user["gender"] == updated_data[
        "gender"], f"Expected gender to be {updated_data['gender']}, but got {updated_user['gender']}"
    assert updated_user["status"] == updated_data[
        "status"], f"Expected status to be {updated_data['status']}, but got {updated_user['status']}"
