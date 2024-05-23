from locators.feed_page_locators import FeedPageLocators as Fpl


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
