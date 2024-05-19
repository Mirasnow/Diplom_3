import allure
from data import Urls
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from pages.profile_page import ProfilePage
from locators.main_page_locators import MainPageLocators as Mpl
from locators.profile_page_locators import ProfilePageLocators as Ppl
from locators.login_page_locators import LoginPageLocators as Lpl


class TestProfilePage:

    @allure.title('Проверка перехода на страницу "Профиль"')
    @allure.description('Проверка, что нажатие на кнопку "Личный кабинет" в заголовке открывает страницу "Профиль"')
    def test_click_on_account_button_opens_profile_page(self, browser_driver):
        profile_page = ProfilePage(browser_driver)
        profile_page.transfer_to_cabinet(browser_driver, Mpl.account_button)
        browser_driver.implicitly_wait(3)
        result = browser_driver.current_url
        assert result == Urls.login_url

    @allure.title('Проверка перехода на страницу "История заказов"')
    @allure.description('Проверка, что нажатие на ссылку "История заказов" в профиле открывает страницу "История заказов"')
    def test_click_on_order_history_url_opens_orders_history_page(self, browser_driver):
        profile_page = ProfilePage(browser_driver)
        profile_page.history_orders(browser_driver, Mpl.account_button, Lpl.email_input_field,
                                    Lpl.password_input_field, Lpl.sign_in_button, Ppl.orders_history_url)
        browser_driver.implicitly_wait(3)
        result = browser_driver.current_url
        assert result == Urls.order_history_url

    @allure.title('Проверка выхода из аккаунта')
    @allure.description('Проверка, что нажатие на кнопку "Выход" в профиле приводит к выходу из аккаунта')
    def test_click_on_exit_url_logs_out_from_account(self, browser_driver):
        profile_page = ProfilePage(browser_driver)
        profile_page.authorization_and_exit(browser_driver, Mpl.account_button, Lpl.email_input_field,
                                            Lpl.password_input_field, Lpl.sign_in_button, Ppl.exit_button)
        WebDriverWait(browser_driver, 3).until(EC.url_to_be(Urls.login_url))
        result = browser_driver.current_url
        assert result == Urls.login_url
