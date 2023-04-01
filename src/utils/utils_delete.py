from src.config import BASE_URL, HEADERS
import requests


def delete_user(user_id):
    response_delete = requests.delete(f"{BASE_URL}/{user_id}", headers=HEADERS)
    return response_delete

def assert_no_user_in_list(user_id):
    response_get = requests.get(BASE_URL + f"/{user_id}", headers=HEADERS)
    assert response_get.status_code == 404, f"Expected status code 404, but got {response_get.status_code}"
    return response_get
