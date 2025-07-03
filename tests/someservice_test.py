import requests
from conf import SERVICE_URL_2
from src.baseclasses.response import AssertResponse
from src.pydantic_schemas.user import UserSchema



def test_get_users_list():
    response = requests.get(SERVICE_URL_2)
    test_obj = AssertResponse(response)
    test_obj.assert_status_code(200)
    test_obj.validate(UserSchema)

