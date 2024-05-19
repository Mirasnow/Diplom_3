import allure
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from pages.forgot_password_page import ForgotPasswordPage
from locators.login_page_locators import LoginPageLocators as Lpl
from locators.main_page_locators import MainPageLocators as Mpl
from locators.forgot_password_page_locators import ForgotPasswordPageLocators as Fpl
from data import Urls


class TestForgotPasswordPage:

    @allure.title('Проверка перехода на страницу восстановления пароля')
    @allure.description('Проверка, что нажатие на кнопку "Восстановить пароль" открывает страницу восстановления пароля')
    def test_click_on_pass_recovery_button_opens_recovery_page(self, browser_driver):
        forgot_page = ForgotPasswordPage(browser_driver)
        forgot_page.recover_password(browser_driver, Mpl.account_button, Lpl.forgot_password_button,
                                     Fpl.email_entry_field, Fpl.recover_button)
        WebDriverWait(browser_driver, 3).until(EC.url_to_be(Urls.reset_password_url))
        result = browser_driver.current_url
        assert result == Urls.reset_password_url

    @allure.title('Проверка перехода на страницу "Сброс пароля"')
    @allure.description('Проверка, что после ввода электронной почты и нажатия на кнопку "Восстановить пароль" '
                        'открывается страница "Сброс пароля"')
    def test_input_email_and_click_on_pass_recovery_button_opens_pass_page(self, browser_driver):
        forgot_page = ForgotPasswordPage(browser_driver)
        forgot_page.page_recover(browser_driver, Mpl.account_button, Lpl.forgot_password_button)
        browser_driver.implicitly_wait(3)
        result = browser_driver.current_url
        assert result == Urls.forgot_password_url



    @allure.title('Проверка фокуса на поле ввода пароля')
    @allure.description('Проверка, что после нажатия на кнопку "Показать/скрыть пароль"'
                        'подсвечивается поле ввода пароля на странице "Сброс пароля"')
    def test_highlight_pass_entry_field(self, browser_driver):
        forgot_page = ForgotPasswordPage(browser_driver)
        forgot_page.hide_password(browser_driver, Mpl.account_button, Fpl.email_entry_field)
        element = browser_driver.find_element(*Fpl.email_entry_field)
        tab = element.find_element(*Lpl.email_active_field)
        tab_class = tab.get_attribute("class")
        assert tab_class == 'input pr-6 pl-6 input_type_text input_size_default input_status_active'
