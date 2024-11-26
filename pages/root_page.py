from pages.lk_page import LkPage
from locators.root_page_locators import RootPageLocators
import allure
from urls import *
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

    @allure.step('Проверка текста в конструкторе')
    def check_kon_text(self):
        return self.get_elem_text(RootPageLocators.KON_LABEL) == RootPageLocators.KON_LABEL[1][13:28]  #//h1[text()='Соберите бургер'] -> Соберите бургер

    @allure.step('Ждем скрытия надписи "загрузка"')
    def wait_load(self):
        self.wait_elem_hide(RootPageLocators.LOADING)

    @allure.step('Проверка текста в ленте')
    def check_lenta_text(self):
        return self.get_elem_text(RootPageLocators.LENTA_LABEL) == RootPageLocators.LENTA_LABEL[1][13:26]  #//h1[text()='Лента заказов'] -> Лента заказов

    @allure.step('Проверка текста в ингридиентах')
    def check_ingdr_text(self):
        return self.get_elem_text(RootPageLocators.INGDR_LABEL) == RootPageLocators.INGDR_LABEL[1][13:31]

    @allure.step('Ждем крестик на ингридиентах')
    def click_close(self):
        self.click_elem_with_wait(RootPageLocators.CLOSE)

    @allure.step('Проверка текста в конструкторе')
    def check_kon_clickable(self):
        return self.elem_is_clickable(RootPageLocators.KONSTRUKT)

    @allure.step('Проверка текста в заказе')
    def check_order_text(self):
        return self.get_elem_text(RootPageLocators.LABEL_ORDER) == RootPageLocators.LABEL_ORDER[1][12:32]
