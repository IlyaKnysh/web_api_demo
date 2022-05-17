from addict import Dict
from hamcrest import equal_to
from requests import Response

from core.apps.backend.population_api import population_api
from core.testlib.matchers import check_that


class PopulationApiSteps:
    @staticmethod
    def get_country(name: str) -> Response:
        return population_api.get_country(name)

    @staticmethod
    def post_country(name: str, population: int, capital_id: int) -> Response:
        return population_api.post_country(name, population, capital_id)

    @staticmethod
    def post_capital(name: str, population: int) -> Response:
        return population_api.post_capital(name, population)

    @staticmethod
    def get_capital(name: str) -> Response:
        return population_api.get_capital(name)


population_api_steps = PopulationApiSteps()


class PopulationApiAssertSteps:
    @staticmethod
    def check_country_added(country: Dict) -> None:
        country_api = population_api_steps.get_country(country.name).json()

        check_that(country_api.get('name'), equal_to(country.name), f'Country name is {country.name}')
        check_that(country_api.get('population'), equal_to(country.population),
                   f'Country population is {country.population}')
        check_that(country_api.get('capital_id'), equal_to(country.capital_id),
                   f'Country capital_id is {country.capital_id}')


population_api_assert_steps = PopulationApiAssertSteps()
