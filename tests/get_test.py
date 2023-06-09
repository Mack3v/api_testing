import json
from src.utils.utils_get import *


def test_get_users():
    """
    Запрос всех пользователей сервера и валидация ответа
    """
    response, data = get_users()
    for item in data:
        validate_user_item(item)
    print(json.dumps(data, sort_keys=True, indent=4))
