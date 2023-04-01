from src.utils.utils_put import *
from src.schema import user_data, updated_data, expected_put_data


def test_put():
    response, user_id = create_user(user_data)
    assert_status_code(response, 201)
    new_data = put_update_data(updated_data, user_id)
    assert_new_data(new_data, user_id, expected_put_data)
    assert_new_user_in_list(updated_data, user_id)
