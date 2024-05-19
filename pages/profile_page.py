import time
import allure
from pages.base_page import BasePage
from data import CommonData


class ProfilePage(BasePage):
    def __init__(self, driver):
        super().__init__(driver)


    @allure.step('Переход в личный кабинет')
    def transfer_to_cabinet(self, driver, locator_button_cabinet):
        self.click_on_element(driver, locator_button_cabinet)


    @allure.step('Открытие истории заказов')
    def history_orders(self, driver, locator_button_cabinet, locator_email, locator_password, locator_button_entrance,
                       locator_history):
        self.click_on_element(driver, locator_button_cabinet)
        self.set_text_to_element(locator_email, CommonData.test_email)
        self.set_text_to_element(locator_password, CommonData.test_user_password)
        self.click_on_element(driver, locator_button_entrance)
        time.sleep(2)
        self.click_on_element(driver, locator_button_cabinet)
        self.click_on_element(driver, locator_history)


    @allure.step('Разлогин пользователя')
    def authorization_and_exit(self, driver, locator_button_cabinet, locator_email, locator_password,
                               locator_button_entrance,
                               locator_exit):
        self.click_on_element(driver, locator_button_cabinet)
        self.set_text_to_element(locator_email, CommonData.test_email)
        self.set_text_to_element(locator_password, CommonData.test_user_password)
        self.click_on_element(driver, locator_button_entrance)
        time.sleep(2)
        self.click_on_element(driver, locator_button_cabinet)
        self.click_on_element(driver, locator_exit)
