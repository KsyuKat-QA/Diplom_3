import time
from selenium.webdriver.common.by import By
from pages.root_page import RootPage
from locators.order_page_locators import OrderPageLocators
import allure
from urls import *

class OrderPage(RootPage):
    @allure.step('Открыли браузер по ссылке ' +LENTA_SITE )
    def go_to_site(self):
        return self.driver.get(LENTA_SITE)

    @staticmethod
    def order_elem_by_num(locator, num): #форматируем локатор по номеру
        method, loc = locator
        loc = loc.format(num)
        return method,loc

    @allure.step('Клик по ленте заказов')
    def lenta_click(self):
        self.click_elem_with_wait(OrderPageLocators.LENTA_ORDERS)

    @allure.step('Клик по элементу из ленты, где num - это номер по порядку сверху-вниз')
    def order_click(self, num):
        self.click_elem_with_wait(self.order_elem_by_num(OrderPageLocators.ORDER_LIST_ELEM, num))

    @allure.step('Вернули id заказа в виде #0152641, где num - это номер по порядку сверху-вниз') #до 50
    def get_order_id(self, num):
        return self.get_elem_text(self.order_elem_by_num(OrderPageLocators.ORDER_LIST_ELEM_ID, num)) #вернули id заказа в виде #0152641

    @allure.step('Сравниваем id заказа (вида #0152641) с тем, что на модальной форме')
    def check_modal_order_id(self, order_id):
        return self.get_elem_text(OrderPageLocators.MODAL_ORDER_ID) #== order_id  #сравниваем id заказа (#0152641) с тем, что на модальной форме

    @allure.step('Нажимаем крестик на форме заказа')
    def close_modal_order_id(self):
        i = 0
        while self.get_elem_text(OrderPageLocators.MODAL_ORDER_ID_FROM_MAIN)=='9999' or i<20: #пока не получим id заказа, не закрываем модальную форму
            time.sleep(0.1)
            i =+ 1
        ord_id = self.get_elem_text(OrderPageLocators.MODAL_ORDER_ID_FROM_MAIN) #возвращаем id заказа
        self.click_elem_with_wait(OrderPageLocators.CLOSE_ORD_DONE) #крестик на форме заказа
        return ord_id

    @allure.step('Идем в историю заказов в ЛК')
    def hist_click(self):
        self.click_elem_with_wait(OrderPageLocators.HIST_ORDERS)

    @allure.step('Проверяем, что в ЛК в истории заказов есть элемент с созднным ID (добавив при проверке префикс "#0")')
    def is_order_id_in_hist_elems(self, id):
        block = self.find_elems_with_wait(OrderPageLocators.HIST_ELEMS) #берем все элементы в истории, построчно
        for elem in block[::-1]: #ищем с конца
            if elem.find_element(By.TAG_NAME, "p").text == "#0"+id:
                return True
        return False

    @allure.step('Проверяем, что в ленте заказов есть элемент с созднным ID (добавив при проверке префикс "#0")')
    def is_order_id_in_lenta_elems(self, id):
        block = self.find_elems_with_wait(OrderPageLocators.LENTA_ELEMS) #берем все элементы в истории, построчно
        for elem in block:
            if elem.find_element(By.TAG_NAME, "p").text == "#0"+id:
                return True
        return False

    @allure.step('Вернули число "Выполнено за все время"')
    def get_total_orders_done(self):
        return self.get_elem_text(OrderPageLocators.TOTAL_DONE)

    @allure.step('Вернули число "Выполнено за сегодня"')
    def get_today_orders_done(self):
        return self.get_elem_text(OrderPageLocators.TODAY_DONE)

    @allure.step('Проверяем номер заказа в списке "В работе" в ленте заказов (добавив ведомый 0 вначале)"')
    def check_order_in_work(self, id, wait):
        time.sleep(wait) # нужна задержка, чтобы номер успел появиться на ленте справа
        block = self.find_elems_with_wait(OrderPageLocators.ORDERS_IN_WORK) #берем все элементы в истории, построчно
        for elem in block:
            if elem.find_element(By.TAG_NAME, "li").text == "0"+id:
                return True
        return False
