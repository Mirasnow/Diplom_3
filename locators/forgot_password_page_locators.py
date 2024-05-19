from selenium.webdriver.common.by import By


class ForgotPasswordPageLocators:
    email_entry_field = (By.XPATH, "//input[@name='name']")
    recover_button = (By.XPATH, "//button[text()='Восстановить']")