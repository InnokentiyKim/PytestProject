import pytest
import random
from src.generators.player import Player


def _calculate(a, b):
    return a + b


@pytest.fixture
def calculate():
    return _calculate


@pytest.fixture
def get_some_number():
    print('Setup process...')
    yield random.randrange(1, 1000, 5)
    print('Tear down process...')


@pytest.fixture
def get_player_generator():
    return Player()


