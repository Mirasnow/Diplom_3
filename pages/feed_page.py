from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from pages.base_page import BasePage
from helpers import CreateOrder
import allure
from data import Urls



class FeedPage(BasePage):

    def __init__(self, driver):
        super().__init__(driver)


    @allure.step('Открытие окна с деталями заказа')
    def click_order_new_window(self, locator_feed, locator_order):
        self.click_on_element(locator_feed)
        self.click_on_element(locator_order)


    @allure.step('Получение номера заказа в ленте заказов')
    def user_orders_in_feed(self, create_user, locator_feed, locator_order, locator_order_number):
        self.click_on_element(locator_feed)
        responce = CreateOrder.create_order_with_auth_with_ingr(create_user)
        order_number = responce.json()['order']['number']
        order_number = str(order_number)
        self.click_on_element(locator_order)
        order_ui = self.get_text_from_element(locator_order_number)
        order_ui = order_ui[2:]
        return order_number, order_ui


    @allure.step('Увеличение счетчика')
    def count_increase(self, create_user, locator_feed, locator_count_total):
        self.click_on_element(locator_feed)
        count_before_order = self.get_text_from_element(locator_count_total)
        CreateOrder.create_order_with_auth_with_ingr(create_user)
        WebDriverWait(self.driver, 3).until(EC.url_to_be(Urls.feed_url))
        count_after_order = self.get_text_from_element(locator_count_total)
        return count_before_order, count_after_order


    @allure.step('Получение новера заказа в работе')
    def number_order_in_progress(self, create_user, locator_feed, locator_order_progress):
        self.click_on_element(locator_feed)
        responce = CreateOrder.create_order_with_auth_with_ingr(create_user)
        order_ui = self.get_text_from_element(locator_order_progress)
        order_number = responce.json()['order']['number']
        order_number = str(order_number)
        return order_number, order_ui
