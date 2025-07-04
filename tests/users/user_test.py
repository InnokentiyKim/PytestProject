from src.baseclasses.response import AssertResponse
from src.pydantic_schemas.user import UserSchema



def test_get_users_list(get_users, get_some_number):
    test_obj = AssertResponse(get_users)
    test_obj.assert_status_code(200)
    test_obj.validate(UserSchema)
    print(get_some_number)

