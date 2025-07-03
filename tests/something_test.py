import requests
from conf import SERVICE_URL_1
from src.baseclasses.response import AssertResponse
from src.enums.global_enums import GlobalErrorMessage
from src.pydantic_schemas.post import PostSchema


def test_equal():
    assert 1 == 1

def test_is_not_equal():
    assert 1 != 2, "one is not equal to two"


def test_getting_posts():
    response = requests.get(SERVICE_URL_1)
    resp_assert = AssertResponse(response)
    resp_assert.assert_status_code(200).validate(PostSchema)
    resp_assert.validate(PostSchema)
