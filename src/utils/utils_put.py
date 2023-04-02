from src.config import BASE_URL, HEADERS
import requests


def create_user(user_data):
    """ Создание пользователя с заданными в src.schema параметрами """
    response = requests.post(BASE_URL, headers=HEADERS, json=user_data)
    user_id = response.json()["id"]
    return response, user_id


def assert_status_code(response, expected_status_code):
    """
    Проверка статус кода. Код передаётся в тесте
    """
    assert response.status_code == expected_status_code, f"Expected status code {expected_status_code}, " \
                                                         f"but got {response.status_code}"


def put_update_data(updated_data, user_id):
    """
    Обновление даты пользователя на updated_data из src.schema
    """
    put_response = requests.put(f"{BASE_URL}/{user_id}", headers=HEADERS, json=updated_data)
    assert put_response.status_code == 200, f"Expected status code 200, but got {put_response.status_code}"
    new_data = put_response.json()
    return new_data


def assert_new_data(new_data, user_id, expected_put_data):
    """
    Сравнение полученной из ответа сервера даты с ожидаемой
    """
    expected_put_data["id"] = user_id
    assert new_data == expected_put_data, f"Expected response data {expected_put_data}, but got {new_data}"


def assert_new_user_in_list(updated_data, user_id):
    """
    Проверка нахождения созданного пользователя в общем списке.
    Сравнение даты юзера, найденного в общем списке, с updated_data из src.schema
    """
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