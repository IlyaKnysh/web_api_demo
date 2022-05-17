import allure
from addict import Dict

from core.testlib.utils import get_random_str, get_random_int
from steps.api_steps.population_api_steps import population_api_steps, population_api_assert_steps


@allure.description('pa-1')
@allure.title('Test success post /country')
@allure.tag('Population API')
def test_post_country(add_random_capital):
    country = Dict(name=get_random_str(), population=get_random_int(), capital_id=add_random_capital.capital_id)

    population_api_steps.post_country(name=country.name, population=country.population, capital_id=country.capital_id)

    population_api_assert_steps.check_country_added(country)
