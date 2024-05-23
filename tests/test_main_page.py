import allure
from pages.main_page import MainPage
from locators.main_page_locators import MainPageLocators as Mpl
from locators.login_page_locators import LoginPageLocators as Lpl
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from data import Urls


class TestMainPage:

    @allure.title('Проверка перехода на страницy "Лента заказов"')
    @allure.description('Тест на проверку, что нажатие на кнопку "Лента заказов" в заголовке '
                        'перенаправляет на соответствующую страницу')
    def test_transfer_to_feed(self, browser_driver):
        main_page = MainPage(browser_driver)
        main_page.transfer_to_feed(Mpl.feed_button)
        WebDriverWait(browser_driver, 3).until(EC.url_to_be(Urls.feed_url))
        result = browser_driver.current_url
        assert result == Urls.feed_url


    @allure.title('Проверка перехода на страницы "Конструктор"')
    @allure.description('Тест на проверку, что нажатие на кнопку "Конструктор" в заголовке '
                        'перенаправляет на соответствующую страницу')
    def test_transfer_to_cons(self, browser_driver):
        main_page = MainPage(browser_driver)
        main_page.transfer_to_constructor(Mpl.feed_button, Mpl.constructor_button)
        WebDriverWait(browser_driver, 3).until(EC.url_to_be(Urls.main_url))
        result = browser_driver.current_url
        assert result == Urls.main_url


    @allure.title('Проверка открытия поп-апа с информацией об ингредиенте')
    @allure.description('Проверка, что нажатие на ингредиент открывает поп-ап с информацией об ингредиенте')
    def test_new_window(self, browser_driver):
        main_page = MainPage(browser_driver)
        result = main_page.new_window(Mpl.object_order, Mpl.ingredient_details)
        assert result == "Детали ингредиента"


    @allure.title('Проверка закрытия поп-апа с информацией об ингредиенте')
    @allure.description('Проверка, что нажатие на кнопку закрытия поп-апа с информацией об ингредиенте закрывает окно')
    def test_close_new_window(self, browser_driver):
        main_page = MainPage(browser_driver)
        main_page.close_new_window(Mpl.object_order, Mpl.window_button_class)
        element = browser_driver.find_element(*Mpl.section_class)
        element_class = element.get_attribute("class")
        assert element_class == 'Modal_modal__P3_V5'


    @allure.title('Проверка увеличения счетчика ингредиента')
    @allure.description('Проверка, что добавление ингредиента в заказ увеличивает его счетчик на определенное значение')
    def test_add_ingredient(self, browser_driver):
        main_page = MainPage(browser_driver)
        main_page.add_ingrediend(Mpl.object_order, Mpl.base_order_button)
        element = browser_driver.find_element(*Mpl.total_price)
        assert element.text != "0"


    @allure.title('Проверка, что авторизованный пользователь может сделать заказ')
    @allure.description('Проверка, что авторизованный пользователь может оформить заказ')
    def test_create_order(self, browser_driver):
        main_page = MainPage(browser_driver)
        main_page.create_order(Mpl.account_button, Lpl.email_input_field, Lpl.password_input_field,
                               Lpl.sign_in_button, Mpl.object_order, Mpl.base_order_button, Mpl.place_order_button)
        element = browser_driver.find_element(*Mpl.order_number)
        assert element.text != ''
