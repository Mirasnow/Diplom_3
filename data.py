import requests
import random
import string
from locators.feed_page_locators import FeedPageLocators as Fpl
from locators.main_page_locators import MainPageLocators as Mpl

class Urls:
    main_url = 'https://stellarburgers.nomoreparties.site/'
    forgot_password_url = f'{main_url}forgot-password'
    order_history_url = f'{main_url}account/order-history'
    login_url = f'{main_url}login'
    feed_url = f'{main_url}feed'
    profile_url = f'{main_url}account/profile'
    reset_password_url = f'{main_url}reset-password'
    register_url = f'{main_url}api/auth/register'
    delete_user_url = f'{main_url}api/auth/user'
    authorization_url = f'{main_url}api/auth/login'
    create_order_url = f'{main_url}api/ingredients'
    get_orders_url = f'{main_url}api/orders'


class CommonData:
    test_email = 'mira_test@yandex.ru'
    test_user_password = 'test12345'
    test_user_name = 'Mira'

    counters = [
        [Fpl.total_orders_counter, 'Completed for all time'],
        [Fpl.today_orders_counter, 'Completed today']
    ]


class CreateOrder:
    @staticmethod
    def create_order_with_auth_with_ingr(create_user):
        # создаем тело запроса
        header = {
                'Authorization': create_user[3]
            }

        body = {
                "email": create_user[0],
                "password": create_user[1],
                "name": create_user[2]
            }
        # авторизуемся
        requests.post(Urls.authorization_url, json=body, headers=header)
        # добавляем ингридиенты
        responce_ingredients = requests.get(Urls.create_order_url)
        ingredients = responce_ingredients.json()["data"]
        # создаем заказ
        body_order = {
                "ingredients": [ingredients[0]["_id"], ingredients[1]["_id"]]
            }

        responce = requests.post(Urls.get_orders_url, json=body_order, headers=header)
        return responce


class CreateNewUser:
    @staticmethod
    def create_new_user():
        newbody = []
        letters = string.ascii_lowercase
        email = ''.join(random.choice(letters) for _ in range(10)) + '@yandex.ru'
        password = ''.join(random.choice(letters) for i in range(8))
        name = ''.join(random.choice(letters) for i in range(6))

        body = {
                "email": email,
                "password": password,
                "name": name
            }

        responce = requests.post(Urls.register_url, json=body)
        atoken = responce.json()["accessToken"]
        if responce.status_code == 200:
            newbody.append(email)
            newbody.append(password)
            newbody.append(name)
            newbody.append(atoken)

        return newbody