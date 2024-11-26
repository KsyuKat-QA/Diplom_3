from pages.reset_page import ResetPage
from conftest import browser
from urls import *
import pytest
import allure

@allure.title('Проверка восстановления пароля')
@allure.description('Проверяем переход в ЛК и восстановление пароля')
@allure.link(ROOT_SITE, name='Изначальная ссылка')
@pytest.mark.parametrize("mail",
                         ["laksdjf@mail.ru",
                         "laksjdfk@mail.com"])
def test_reset_pass(browser,mail):
    testing_page = ResetPage(browser)
    testing_page.go_to_site()
    testing_page.lk_click()
    testing_page.but_recover_click()
    testing_page.fill_mail(mail)
    testing_page.but_recover_final_click()
    testing_page.show_pass()
    assert testing_page.check_active_pass_input() #Сравниваем активный элемент с формой ввода пароля