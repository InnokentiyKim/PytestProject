import requests
import pytest
from conf import SERVICE_URL_1
from src.baseclasses.response import AssertResponse
from tests.conftest import calculate
from src.pydantic_schemas.post import PostSchema


@pytest.mark.skip(reason="Issue-1234")
def test_equal():
    assert 1 == 1


@pytest.mark.skipif("1 == 0")
def test_is_not_equal():
    assert 1 != 2, "one is not equal to two"


@pytest.mark.production
@pytest.mark.development
@pytest.mark.parametrize(
    'first_val, second_val, expected',
    [
        (1, 2, 3),
        (-1, 0, -1),
        (0, 0, 0),
        (-2, 2, 0),
        (-1, -2, -3)
    ]
)
def test_calculate(first_val, second_val, expected, calculate):
    assert calculate(first_val, second_val) == expected


def test_getting_posts():
    response = requests.get(SERVICE_URL_1)
    resp_assert = AssertResponse(response)
    resp_assert.assert_status_code(200).validate(PostSchema)
    resp_assert.validate(PostSchema)


@pytest.mark.parametrize(
    "status", [
        "Active",
        "Inactive",
        "Banned"
    ]
)
def test_smth(status, get_player_generator):
    print(get_player_generator.set_status(status).build())
