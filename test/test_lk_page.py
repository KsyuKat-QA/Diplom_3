from locators.lk_page_locators import LkPageLocators
from pages.lk_page import LkPage
from conftest import browser
from data import *
import allure

@allure.title('Тест личного кабинета')
@allure.description('Проверяем вход в ЛК, историю заказов, выход из кабинета')
@allure.link(ROOT_SITE, name='Изначальная ссылка')
def test_lk(browser):
    testing_page = LkPage(browser)
    testing_page.go_to_site()
    testing_page.but_lk_click()
    testing_page.lk_login()
    testing_page.but_lk_click()
    testing_page.but_hist_click()
    assert testing_page.get_cur_url() == ROOT_SITE+'/account/order-history'
    testing_page.wait_elem_hide(LkPageLocators.LOADING) #ждем скрытия надписи "загрузка"
    testing_page.exit_lk()
    testing_page.find_elem_with_wait(LkPageLocators.BUT_RECOVER) #ждем на главной кнопки для восстановления
    assert testing_page.get_cur_url() == LOGIN_SITE