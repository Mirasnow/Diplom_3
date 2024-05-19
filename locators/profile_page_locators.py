from selenium.webdriver.common.by import By


class ProfilePageLocators:
    orders_history_url = (By.XPATH, ".//a[text()='История заказов']")
    exit_button = (By.XPATH, ".//button[text()='Выход']")

