from faker import Faker
import requests
import random
import pytest

BASE_URL = 'https://gorest.co.in//public/v2/users'
TOKEN = '1c173e094ebdb2a1d204e3ebb96906bceace8e74a64287688220f5c173c2541d'
HEADERS = {'Authorization': f'Bearer {TOKEN}'}

fake = Faker()

# Define user data globally
user_data = {
    "name": fake.name(),
    "email": fake.email(),
    "gender": random.choice(["male", "female"]),
    "status": random.choice(["active", "inactive"])
}
invalid_emails = [
    ("invalid-email", "is invalid"),
    ("invalid.email.com", "is invalid"),
    ("@invalid-email.com", "is invalid"),
    ("invalid-email.com", "is invalid")
]

def test_create_new_user():
    # Send request to create new user
    response = requests.post(BASE_URL, headers=HEADERS, json=user_data)

    # Assert response status code is 201
    assert response.status_code == 201, f"Expected status code 201, but got {response.status_code}"
    print(response.json())
    # Assert response matches expected data
    expected_data = {"name": user_data["name"], "email": user_data["email"], "gender": user_data["gender"],
                     "status": user_data["status"]}
    response_data = response.json()
    response_data.pop("id", None)
    assert response_data == expected_data, f"Expected response data {expected_data}, but got {response_data}"

    # Send request to get all users and assert new user is in the list
    response = requests.get(BASE_URL, headers=HEADERS)
    assert response.status_code == 200, f"Expected status code 200, but got {response.status_code}"
    user_list = response.json()
    assert any(user["email"] == user_data["email"] for user in user_list), f"Expected to find user with email {user_data['email']} in list"


@pytest.mark.parametrize("invalid_email, expected_error", invalid_emails)
def test_incorrect_post(invalid_email, expected_error):
    # Set email to invalid email
    user_data["email"] = invalid_email
    # Send request to create new user with incorrect email
    response = requests.post(BASE_URL, headers=HEADERS, json=user_data)

    # Assert response status code is 422
    assert response.status_code == 422, f"Expected status code 422, but got {response.status_code}"

    print(response.json())

    response_error = response.json()[0]["message"]
    assert "is invalid" in response_error, f"Expected error message to contain 'is invalid', but got {response_error}"
    assert "email" == response.json()[0][
        "field"], f"Expected field to be 'email', but got {response.json()[0]['field']}"