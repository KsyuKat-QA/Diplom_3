from pages.order_page import OrderPage
from conftest import browser
import pytest
import allure

@allure.title('Лента заказов')
@allure.description('Проверяем детали по клику на элемент в ленте заказов')
@pytest.mark.parametrize("num", [
        (1),
        (3)
    ])
def test_lenta(browser, num):
    testing_page = OrderPage(browser)
    testing_page.go_to_site()
    testing_page.lenta_click()
    order_id=testing_page.get_order_id(num)
    testing_page.order_click(num)
    assert testing_page.check_modal_order_id(order_id)

@allure.title('Проверка оформления заказа')
@allure.description('После состава бургера, логинимся и оформляем заказ')
@pytest.mark.parametrize("ingdr_pos", [
    (1, 1),
    (1, 2)
    ])
def test_new_order_in_lenta(browser,ingdr_pos):
    testing_page = OrderPage(browser)
    testing_page.go_to_site()
    testing_page.but_lk_click()
    testing_page.lk_login()
    testing_page.ingdr_move(*ingdr_pos)
    testing_page.do_order_click()
    order_id = testing_page.close_modal_order_id() #после создания заказа запомнили его id в виде 152676
    testing_page.but_lk_click()
    testing_page.hist_click() #открыли историю заказов в ЛК
    assert testing_page.is_order_id_in_hist_elems(order_id) #проверяем, что в истории ЛК есть наш свежесозданный заказ
    testing_page.lenta_click()
    assert testing_page.is_order_id_in_lenta_elems(order_id) #проверяем, что этот же заказ есть в ленте заказов


@allure.title('Проверка счетчиков для заказа')
@allure.description('Проверяем сразу три кейса, что меняются числа в "Выполнено за все время" + "Выполнено за сегодня" + номер заказа появился в списке "в работе"')
@pytest.mark.parametrize("ingdr_pos", [
    (1, 1),
    (1, 2)
    ])
def test_new_order_counter(browser, ingdr_pos):
    testing_page = OrderPage(browser)
    testing_page.go_to_site()
    total_cnt_before = int(testing_page.get_total_orders_done())
    today_cnt_before = int(testing_page.get_today_orders_done())
    testing_page.but_lk_click()
    testing_page.lk_login()
    testing_page.ingdr_move(*ingdr_pos)
    testing_page.do_order_click()
    order_id = testing_page.close_modal_order_id()  # после создания заказа запомнили его id в виде 152676
    testing_page.lenta_click()
    assert total_cnt_before < int(testing_page.get_total_orders_done()) #после формирования заказа, прошлое число стало строго меньше
    assert today_cnt_before < int(testing_page.get_today_orders_done()) #после формирования заказа, прошлое число стало строго меньше
    assert testing_page.check_order_in_work(order_id)  #номер заказа появился в списке "в работе"
