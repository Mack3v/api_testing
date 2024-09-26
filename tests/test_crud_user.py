from src.utils.api_client import APIClient
from src.utils.users_model import UsersResponseModel
from src.schema import user_data, updated_data, expected_put_data


class TestUser(APIClient):
    """
    Тест работы с пользователем
    """

    def test_crud_user(self):
        """
        Создание, проверка наличия пользователя в общем списке, изменение и удаление
        """
        response = self.create_user(user_data)
        assert response.status_code == 201, f"Unexpected status code when creating a user"
        self.new_user_data.pop("id", None)
        assert self.new_user_data == user_data, "Unexpected data of created user"

        response = self.get_users()
        assert response.status_code == 200, f"Unexpected status code when get users"
        UsersResponseModel(self.users)
        assert any(
            user['id'] == self.user_id for user in self.users), f"User with ID {self.user_id} not found in list"

        response = self.put_user(updated_data)
        assert response.status_code == 200, f"Unexpected status code when put user"
        assert self.updated_user_data.pop("id", None)
        assert self.updated_user_data == expected_put_data, "Unexpected data of updated user"

        response = self.delete_user()
        assert response.status_code == 204, f"Unexpected status code when delete user"

        response = self.get_users()
        assert response.status_code == 200, f"Unexpected status code when get users"
        assert not any(
            user['id'] == self.user_id for user in self.users), f"User with ID {self.user_id} not found in list"
