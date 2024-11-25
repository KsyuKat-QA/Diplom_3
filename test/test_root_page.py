from pages.root_page import RootPage
from locators.root_page_locators import RootPageLocators
from conftest import browser
import pytest
import allure

@allure.title('Проверка конструктора')
@allure.description('Щелкаем по нему и проверяем надпись')
def test_kon(browser):
    testing_page = RootPage(browser)
    testing_page.go_to_site()
    testing_page.kon_click()
    assert testing_page.get_elem_text(RootPageLocators.KON_LABEL) == RootPageLocators.KON_LABEL[1][13:28]  #//h1[text()='Соберите бургер'] -> Соберите бургер

@allure.title('Проверка ленты заказов')
@allure.description('Щелкаем по ленте и проверяем надпись')
def test_lenta(browser):
    testing_page = RootPage(browser)
    testing_page.go_to_site()
    testing_page.lenta_click()
    testing_page.wait_elem_hide(RootPageLocators.LOADING) #ждем скрытия надписи "загрузка"
    assert testing_page.get_elem_text(RootPageLocators.LENTA_LABEL) == RootPageLocators.LENTA_LABEL[1][13:26]  #//h1[text()='Лента заказов'] -> Лента заказов

@allure.title('Проверка клику по состовляющим')
@allure.description('Щелкаем по ингридиентам и проверяем окошко')
@pytest.mark.parametrize("ingdr_pos", [
        (1,1),
        (2,2)
    ])
def test_ingdr(browser, ingdr_pos):
    testing_page = RootPage(browser)
    testing_page.go_to_site()
    testing_page.ingdr_click(*ingdr_pos)
    assert testing_page.get_elem_text(RootPageLocators.INGDR_LABEL) == RootPageLocators.INGDR_LABEL[1][13:31] #проверка окошка
    testing_page.click_elem_with_wait(RootPageLocators.CLOSE) #щелкаем по крестику
    assert testing_page.elem_is_clickable(RootPageLocators.KONSTRUKT)

@allure.title('Проверка перетаскивания состовляющих')
@allure.description('Перетаскиваем ингридиенты и проверяем каунтер')
@pytest.mark.parametrize("ingdr_pos", [
        (1,1),
        (2,1),
        (3,2)
    ])
def test_ingdr_move(browser, ingdr_pos):
    testing_page = RootPage(browser)
    testing_page.go_to_site()
    testing_page.ingdr_move(*ingdr_pos)
    if ingdr_pos[0]==1:
        cnt = 2
    else:
        cnt = 1

    cnt_web_elem = int(testing_page.ingdr_count(*ingdr_pos))
    assert cnt_web_elem==cnt

@allure.title('Проверка оформления заказа')
@allure.description('После состава бургера, логинимся и оформляем заказ')
@pytest.mark.parametrize("ingdr_pos", [
    (1, 1),
    (2, 1)
])
def test_do_order(browser, ingdr_pos):
    testing_page = RootPage(browser)
    testing_page.go_to_site()
    testing_page.ingdr_move(*ingdr_pos)
    testing_page.but_lk_click()
    testing_page.lk_login()
    testing_page.do_order_click()
    assert testing_page.get_elem_text(RootPageLocators.LABEL_ORDER) == RootPageLocators.LABEL_ORDER[1][12:32]  # проверка окошка