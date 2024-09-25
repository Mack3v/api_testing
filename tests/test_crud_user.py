from src.utils.api_client import APIClient
from src.utils.users_model import UsersResponseModel
from src.schema import user_data, expected_post_data, incorrect_user_data


class TestUser(APIClient):

    def test_crud_user(self):
        response = self.create_user(user_data)
        assert response.status_code == 201, f"Unexpected status code when creating a user"
        self.new_user_data.pop("id", None)
        assert self.new_user_data == user_data, "Unexpected data of created user"

        response = self.get_users()
        assert response.status_code == 200, f"Unexpected status code when get users"
        UsersResponseModel(self.users)
        assert any(user['id'] == self.user_id for user in self.users), f"User with ID {self.user_id} not found in list"
