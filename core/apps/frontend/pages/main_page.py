import allure
from hamcrest import contains_string
from selene import by
from selene.support.shared import browser

from core.apps.entities.entities import CONNECTED_LOG_STRING
from core.apps.frontend.pages.base_page import BasePage
from core.testlib.matchers import check_that


class MainPage(BasePage):
    """
    Every action method in a page module should have allure.step annotation. This steps will be displayed in allure
    report as actions and it will be clear, what happened on the page. That's why it's better to interact with items
    only via wrapped methods.
    Please note, that business steps shouldn't be implemented here
    """

    path = '/'

    country_input = browser.element(by.name('country_data'))
    capital_input = browser.element(by.name('capital_data'))
    ask_country_button = browser.element(by.xpath('//input[@value="Ask country"]'))
    ask_capital_button = browser.element(by.xpath('//input[@value="Ask capital"]'))
    logs = browser.element(by.id('log'))

    def navigate(self):
        super().navigate()
        check_that(self.get_actions_log_text, contains_string(CONNECTED_LOG_STRING), f'Main page is opened')

    @allure.step('Fill country input')
    def fill_country_input(self, text: str):
        self.capital_input.send_keys(text)

    @allure.step('Fill capital input')
    def fill_capital_input(self, text: str):
        self.country_input.send_keys(text)

    @allure.step('Click ask country button')
    def click_ask_country_button(self):
        self.ask_country_button.click()

    @allure.step('Click ask capital button')
    def click_ask_capital_button(self):
        self.ask_capital_button.click()

    @allure.step('Get action logs')
    def get_actions_log_text(self) -> str:
        return self.logs.text


main_page = MainPage()
