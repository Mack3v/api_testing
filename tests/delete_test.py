from src.schema import user_data
from src.utils.utils_put import create_user, assert_status_code
from src.utils.utils_delete import *


def test_delete():
    response, user_id = create_user(user_data)
    assert_status_code(response, 201)
    response_delete = delete_user(user_id)
    assert_status_code(response_delete, 204)
    assert_no_user_in_list(user_id)