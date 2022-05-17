from requests import Response

from config.env import URL
from core.apps.backend.base_api import BaseApi


class PopulationApi(BaseApi):
    api_url = URL

    def get_country(self, name: str) -> Response:
        params = {
            'name': name
        }
        return self.api_get('/country', params=params)

    def get_capital(self, name: str) -> Response:
        params = {
            'name': name
        }
        return self.api_get('/capital', params=params)

    def post_country(self, name: str, population: int, capital_id: int) -> Response:
        data = {
            'name': name,
            'population': population,
            'capital_id': capital_id
        }
        return self.api_post('/country', json=data)

    def post_capital(self, name: str, population: int) -> Response:
        data = {
            'name': name,
            'population': population
        }
        return self.api_post('/capital', json=data)


population_api = PopulationApi()

if __name__ == '__main__':
    api_strict = PopulationApi()
    api_soft = PopulationApi(raise_exception_on_error=False)
    #
    api_soft.get_country('Ukraine')
    api_strict.get_country('Ukraine')  # here will be exception in case of not success response code
    api_strict.post_country(name='new_country', population=1, capital_id=5)
