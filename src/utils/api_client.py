import requests
from src.config import BASE_URL, HEADERS


class APIClient:

    base_url = BASE_URL
    users = []
    user_id = None
    new_user_data = []

    def get_users(self):
        url = f"{self.base_url}/users"
        response = requests.get(url, headers=HEADERS)
        if len(response.json()) > 0:
            self.users = response.json()
        return response

    def create_user(self, user_data):
        url = f"{self.base_url}/users"
        response = requests.post(url, user_data, headers=HEADERS)
        if len(response.json()) > 0:
            self.user_id = response.json()['id']
            self.new_user_data = response.json()
        return response
