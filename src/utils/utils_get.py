from src.schema import *
from src.config import *
import requests
from jsonschema import validate


def get_users():
    response = requests.get(BASE_URL, headers=HEADERS)
    assert response.status_code == 200, f"Expected status code 200, but got {response.status_code}"
    # Проверяем тип содержимого ответа
    assert isinstance(response.content,
                      bytes), f"Expected bytes type for response content, but got {type(response.content)}"
    data = response.json()
    return response, data


def validate_user_item(item):
    validate(item, SCHEMA)
    assert isinstance(item["id"], int), f"Expected type int for 'id' field, but got {type(item['id'])}"
    assert isinstance(item["name"], str), f"Expected type str for 'name' field, but got {type(item['name'])}"
    assert isinstance(item["email"], str), f"Expected type str for 'email' field, but got {type(item['email'])}"
    assert isinstance(item["gender"], str), f"Expected type str for 'gender' field, but got {type(item['gender'])}"
    assert isinstance(item["status"], str), f"Expected type str for 'status' field, but got {type(item['status'])}"
