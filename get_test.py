import json
import requests
import jsonschema
from jsonschema import validate

BASE_URL = 'https://gorest.co.in/public-api/users'
TOKEN = '1c173e094ebdb2a1d204e3ebb96906bceace8e74a64287688220f5c173c2541d'
HEADERS = {'Authorization': f'Bearer {TOKEN}'}

schema = {
    "type": "object",
    "properties": {
        "code": {"type": "integer"},
        "data": {
            "type": "array",
            "items": {
                "type": "object",
                "properties": {
                    "id": {"type": "integer"},
                    "name": {"type": "string"},
                    "email": {"type": "string"},
                    "gender": {"type": "string"},
                    "status": {"type": "string"}
                },
                "required": ["id", "name", "email", "gender", "status"]
            }
        }
    }
}


def test_get_users():
    response = requests.get(BASE_URL, headers=HEADERS)
    assert response.status_code == 200, f"Expected status code 200, but got {response.status_code}"
    assert isinstance(response.content, bytes), f"Expected bytes type for response content, but got {type(response.content)}"
    data = response.json()["data"]
    for item in data:
        validate(item, schema)
        assert isinstance(item["id"], int), f"Expected type int for 'id' field, but got {type(item['id'])}"
        assert isinstance(item["name"], str), f"Expected type str for 'name' field, but got {type(item['name'])}"
        assert isinstance(item["email"], str), f"Expected type str for 'email' field, but got {type(item['email'])}"
        assert isinstance(item["gender"], str), f"Expected type str for 'gender' field, but got {type(item['gender'])}"
        assert isinstance(item["status"], str), f"Expected type str for 'status' field, but got {type(item['status'])}"

    print(json.dumps(data, sort_keys=True, indent=4))
