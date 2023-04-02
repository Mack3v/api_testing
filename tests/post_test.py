from src.utils.utils_post import *
from src.schema import user_data, expected_post_data, incorrect_user_data


def test_create_new_user():
    """
    Создание пользователя с корректными параметрами. Проверка ответа сервера, корректности данных,
    присутсвия пользователя в общем списке
    """
    response = create_user(user_data)
    assert_status_code(response, 201)
    assert_user_data(response, expected_post_data)
    find_user_in_list(user_data["email"])


def test_create_incorrect_user():
    """
    Создание пользователя с некорректными параметрами. Проверка статус кода и сообщения в ответе сервера
    """
    response = create_user(incorrect_user_data)
    assert_status_code(response, 422)
    assert_error_message(response, 'email', 'is invalid')
