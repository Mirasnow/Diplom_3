from selenium.webdriver.common.by import By


class LoginPageLocators:
    sign_in_button = (By.XPATH, ".//button[text()='Войти']")
    forgot_password_button = (By.XPATH, ".//a[text()='Восстановить пароль']")
    email_input_field = (By.XPATH, "//input[@type='text']")
    password_input_field = (By.XPATH, "//input[@type='password']")
    show_button = (By.CLASS_NAME, "//div[@class='input__icon.input__icon-action']")
    email_active_field = (By.XPATH, "//div[@class='input pr-6 pl-6 input_type_text input_size_default input_status_active']")
