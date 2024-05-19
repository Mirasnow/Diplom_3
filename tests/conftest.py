import pytest
import requests
from selenium import webdriver
from data import Urls, CreateNewUser


@pytest.fixture(params=['chrome', 'firefox'])
def browser_driver(request):
    if request.param == 'chrome':
        driver = webdriver.Chrome()
        driver.get(Urls.main_url)
    elif request.param == 'firefox':
        driver = webdriver.Firefox()
        driver.get(Urls.main_url)
    yield driver
    driver.quit()


@pytest.fixture()
def create_user():
    body = CreateNewUser.create_new_user()

    yield body
    body_conf = \
        {
            "email": body[0],
            "password": body[1],
            "name": body[2]
        }
    requests.delete(Urls.delete_user_url, json=body_conf)

