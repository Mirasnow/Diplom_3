import allure
import pytest
from pages.feed_page import FeedPage
from data import CommonData
from helpers import CreateNewUser
from locators.main_page_locators import MainPageLocators as Mpl
from locators.feed_page_locators import FeedPageLocators as Fpl


class TestFeedPage:

    @allure.title('Проверка открытия поп-апа с деталями заказа')
    @allure.description('Проверка, что при нажатии на заказ открывается поп-ап с деталями заказа')
    def test_click_on_order_opens_details_popup_window(self, browser_driver):
        feed_page = FeedPage(browser_driver)
        feed_page.click_order_new_window(Mpl.feed_button, Fpl.orders_number)
        element = browser_driver.find_element(*Fpl.current_order_number)
        assert element.text != ""


    @allure.title('Проверка отображения заказов пользователя из "Истории заказов" на странице "Лента заказов"')
    @allure.description('Проверка, что заказы пользователя из "Истории заказов" отображаются на странице "Лента заказов"')
    def test_user_order_displayed_on_feed_page(self, browser_driver, create_user):
        feed_page = FeedPage(browser_driver)
        order_responce, order_ui = feed_page.user_orders_in_feed(create_user, Mpl.feed_button,
                                                                 Fpl.orders_number, Fpl.current_order_number)
        assert order_responce == order_ui


    @allure.title('Проверка увеличения счетчиков заказов, выполненных за сегодня и за всё время')
    @allure.description('Проверка, что создание нового заказа увеличивает счетчики "Выполнено за сегодня" и "Выполнено за всё время"')
    @pytest.mark.parametrize('counter_locator, description', CommonData.counters)
    def test_increase_counter(self, browser_driver, create_user, counter_locator, description):
        feed_page = FeedPage(browser_driver)
        count_before_order, count_after_order = feed_page.count_increase(create_user,
                                                                         Mpl.feed_button, counter_locator)
        assert int(count_after_order) == int(count_before_order) + 1


    @allure.title('Проверка отображения номера заказа в разделе "В работе"')
    @allure.description('Проверка, что после размещения заказа его номер отображается в разделе "В работе"')
    def test_order_number_displayed_in_progress_section(self, browser_driver, create_user):
        feed_page = FeedPage(browser_driver)
        order_number, order_ui = feed_page.number_order_in_progress(create_user, Mpl.feed_button,
                                                                    Fpl.in_progress_order)
        order_ui = order_ui[1:]
        assert order_number == order_ui