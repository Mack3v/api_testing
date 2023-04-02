from faker import Faker
import random
fake = Faker()

SCHEMA = {
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


# Корректные данные для создания пользователя
user_data = {
    "name": fake.name(),
    "email": fake.email(),
    "gender": random.choice(["male", "female"]),
    "status": random.choice(["active", "inactive"])
}
# Неорректные данные для создания пользователя
incorrect_user_data = {
    "name": fake.name(),
    "email": "fake-email",
    "gender": random.choice(["male", "female"]),
    "status": random.choice(["active", "inactive"])
}
# Ожидаемые данные после отправки POST-запроса
expected_post_data = {
    "name": user_data["name"],
    "email": user_data["email"],
    "gender": user_data["gender"],
    "status": user_data["status"]
}
# Данные для обновления пользователя
updated_data = {
    "name": fake.name(),
    "gender": random.choice(["male", "female"]),
    "status": random.choice(["active", "inactive"])
}
# Ожидаемые данные после PUT-запроса
expected_put_data = {
    "email": user_data["email"],
    "name": updated_data["name"],
    "gender": updated_data["gender"],
    "status": updated_data["status"]
}
