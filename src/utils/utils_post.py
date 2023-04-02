import requests
from src.config import BASE_URL, HEADERS


def create_user(user_data):
    """
    Создание пользователя с заданными в src.schema параметрами
    """
    response = requests.post(BASE_URL, headers=HEADERS, json=user_data)
    return response


def assert_status_code(response, expected_status_code):
    """
    Проверка статус кода. Код передаётся в тесте
    """
    assert response.status_code == expected_status_code, f"Expected status code {expected_status_code}, " \
                                                         f"but got {response.status_code}"


def assert_user_data(response, expected_data):
    """
    Сравнение полученной из ответа сервера даты с ожидаемой
    """
    response_data = response.json()
    response_data.pop("id", None)
    assert response_data == expected_data, f"Expected response data {expected_data}, but got {response_data}"
    return response_data, expected_data


def get_all_users():
    """
    Получаение всех пользователей от сервера
    """
    response_get = requests.get(BASE_URL, headers=HEADERS)
    return response_get.json()


def find_user_in_list(email):
    """
    Проверка нахождения созданного пользователя в общем списке
    """
    user_list = get_all_users()
    return any(user["email"] == email for user in user_list)


def assert_error_message(response, field, message):
    """
    Функция ищет среди ошибок в ответе сервера те, которые соответствуют заданным полям и сообщению об ошибке.
    Значения полей  задаются в тесте, при вызове функции
    """
    errors = response.json()
    for error in errors:
        if error.get('field') == field and error.get('message') == message:
            return True
    assert False, f"Expected error message '{message}' for field '{field}', but got {errors}"
