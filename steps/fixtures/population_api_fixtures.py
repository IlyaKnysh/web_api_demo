import pytest
from addict import Dict

from core.testlib.utils import get_random_str, get_random_int
from steps.api_steps.population_api_steps import population_api_steps


@pytest.fixture(scope='function')
def add_random_capital() -> Dict:
    capital = Dict(name=get_random_str(), population=get_random_int())
    population_api_steps.post_capital(capital.name, capital.population)

    api_capital = population_api_steps.get_capital(capital.name).json()
    capital.update(capital_id=api_capital.get('id'))

    return capital
