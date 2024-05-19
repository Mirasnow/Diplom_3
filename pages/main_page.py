import allure
from pages.base_page import BasePage
from data import CommonData


class MainPage(BasePage):
    def __init__(self, driver):
        super().__init__(driver)


    @allure.step('Переход на страницу заказов')
    def transfer_to_feed(self, driver, locator_feed):
        self.click_on_element(driver, locator_feed)


    @allure.step('Перход на страницу')
    def transfer_to_constructor(self, driver, locator_feed, locator_cons):
        self.click_on_element(driver, locator_feed)
        self.click_on_element(driver, locator_cons)


    @allure.step('Открытие нового окна')
    def new_window(self, driver, locator_element, locator_text):
        self.click_on_element(driver, locator_element)
        return self.get_text_from_element(locator_text)


    @allure.step('Закрытие нового окна')
    def close_new_window(self, driver, locator_element, locator_close):
        self.click_on_element(driver, locator_element)
        self.click_on_element(driver, locator_close)


    @allure.step('Добавление ингридиента')
    def add_ingrediend(self, driver, locator_object, locator_base):
        self.drag_and_drop_element(driver, locator_object, locator_base)


    @allure.step('Создание заказа')
    def create_order(self, driver, locator_button_cabinet, locator_email, locator_password, locator_button_entrance,
                     locator_object, locator_base, locator_create_order):
        self.click_on_element(driver, locator_button_cabinet)
        self.set_text_to_element(locator_email, CommonData.test_email)
        self.set_text_to_element(locator_password, CommonData.test_user_password)
        self.click_on_element(driver, locator_button_entrance)
        self.add_ingrediend(driver, locator_object, locator_base)
        self.click_on_element(driver, locator_create_order)