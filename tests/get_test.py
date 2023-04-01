import json
from src.utils.utils_get import get_users, validate_user_item


def test_get_users():
    response, data = get_users()
    for item in data:
        validate_user_item(item)
    print(json.dumps(data, sort_keys=True, indent=4))
