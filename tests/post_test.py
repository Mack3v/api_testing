from src.utils.utils_post import *
from src.schema import user_data, expected_post_data, incorrect_user_data


def test_create_new_user():
    # Send request to create new user
    response = create_user(user_data)
    assert_status_code(response, 201)
    # Assert response matches expected data
    assert_user_data(response, expected_post_data)
    # Send request to get all users and assert new user is in the list
    find_user_in_list(user_data["email"])
    # assert find_user_in_list(user_data["email"]), f"Expected to find user with email {user_data['email']} in list"


def test_create_incorrect_user():
    response = create_user(incorrect_user_data)
    assert_status_code(response, 422)
    assert_error_message(response, 'email', 'is invalid')
