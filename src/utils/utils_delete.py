from src.config import BASE_URL, HEADERS
import requests


def delete_user(user_id):
    """
    Удаление ранее созданного пользователя. ID передаётся из фунуции create_user
    """
    response_delete = requests.delete(f"{BASE_URL}/{user_id}", headers=HEADERS)
    return response_delete

def assert_no_user_in_list(user_id):
    """
    Проверка отсутсвия удаленного пользователя в общем списке
    """
    response_get = requests.get(BASE_URL + f"/{user_id}", headers=HEADERS)
    assert response_get.status_code == 404, f"Expected status code 404, but got {response_get.status_code}"
    return response_get
