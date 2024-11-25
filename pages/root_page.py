from pages.lk_page import LkPage
from locators.root_page_locators import RootPageLocators
import allure
from data import *
from selenium.webdriver.common.action_chains import ActionChains #для перетаскивания элементов

class RootPage(LkPage):
    @staticmethod
    def burg_elem_by_row(locator, row, col):
        method, loc = locator
        loc = loc.format(row,col)
        return method,loc

    @allure.step('Открыли браузер по ссылке ' + ROOT_SITE)
    def go_to_site(self):
        self.driver.get(ROOT_SITE)
        return self.driver

    @allure.step('Щелкнули по конструктору')
    def kon_click(self):
        self.click_elem_with_wait(RootPageLocators.KONSTRUKT)

    @allure.step('Щелкнули по ленте')
    def lenta_click(self):
        self.click_elem_with_wait(RootPageLocators.LENTA)

    @allure.step('Щелкнули по ингридиенту')
    def ingdr_click(self, row, col):
        self.click_elem_with_wait(RootPage.burg_elem_by_row(RootPageLocators.BURG_ELEM,row,col))

    @allure.step('Перетаскиваем ингридиент в правую часть')
    def ingdr_move(self, row, col):
        actions = ActionChains(self.driver)
        actions.drag_and_drop( #перетаскиваем элемент из конструктора (слева) в правую часть
            self.find_elem_with_wait(RootPage.burg_elem_by_row(RootPageLocators.BURG_ELEM,row,col)),
            self.find_elem_with_wait(RootPageLocators.BURG_STRUCT)
        )
        actions.perform()

    @allure.step('Возвращаем текстом каунтер')
    def ingdr_count(self, row, col):
        return self.get_elem_text(RootPage.burg_elem_by_row(RootPageLocators.COUNTER, row, col))

    @allure.step('Оформляем заказ')
    def do_order_click(self):
        self.click_elem_with_wait(RootPageLocators.BUT_ORDER)