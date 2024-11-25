from selenium import webdriver
import pytest
from data import browserName

@pytest.fixture()
def browser():
    if str(browserName).lower() == 'firefox':
        ff_options = webdriver.FirefoxOptions()
        ff_options.add_argument('--window-size=1550,1200')  # добавили ещё настройку
        driver = webdriver.Firefox(options=ff_options)
    elif str(browserName).lower() == 'chrome':
        gc_options = webdriver.ChromeOptions()
        gc_options.add_argument('--window-size=1550,1000')  # добавили ещё настройку
        driver = webdriver.Chrome(options=gc_options)
    else:
        exit()
    yield driver
    driver.quit()