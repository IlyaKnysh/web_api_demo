from hamcrest import contains_string

from core.apps.frontend.pages.main_page import main_page
from core.testlib.matchers import check_that
from steps.db_steps.population_db_steps import population_db_steps


class MainPageSteps:
    @staticmethod
    def ask_country(name: str) -> None:
        main_page.fill_capital_input(name)
        main_page.click_ask_country_button()


main_page_steps = MainPageSteps()


class MainPageAssertSteps:
    def check_entry_in_log(self, country_name: str) -> None:
        entry = self.build_expected_country_entry(country_name)
        check_that(main_page.get_actions_log_text, contains_string(entry), f'{entry} is in log')

    @staticmethod
    def build_expected_country_entry(country_name: str) -> str:
        country_data = population_db_steps.get_country(country_name)[0]
        id_ = country_data.id
        capital_id = country_data.capital_id
        population = country_data.population

        return f'Received: {{"id":{id_},"capital_id":{capital_id},"name":"{country_name}","population":{population}}}'


main_page_assert_steps = MainPageAssertSteps()
