import allure
import pytest

from core.testlib.matchers import check_schema_is_valid
from resources.json_schemas.api_schema import GET_COUNTRY_SCHEMA
from steps.api_steps.population_api_steps import population_api_steps


@allure.description('pas-1')
@allure.title('Test success get /country')
@allure.tag('Population API schema')
@pytest.mark.parametrize('country', [
    'Ukraine',
    'USA',
    'Germany'
])
def test_get_country(country):
    response = population_api_steps.get_country(country)

    check_schema_is_valid(response.json(), GET_COUNTRY_SCHEMA, 'Get country schema is valid')
