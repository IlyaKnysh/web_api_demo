import allure
import pytest

from steps.ui_steps.main_page_steps import main_page_steps, main_page_assert_steps


@allure.description('mp-1')
@allure.title('Get details by country')
@allure.tag('Main Page')
@pytest.mark.parametrize('country', [
    'Ukraine',
    'USA',
    'Germany',
    'Great Britain'
])
@pytest.mark.usefixtures('driver')
def test_ask_country(country):
    main_page_steps.ask_country(country)

    main_page_assert_steps.check_entry_in_log(country)
