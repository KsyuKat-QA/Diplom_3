from pages.base_page import BasePage
from data import *
from locators.lk_page_locators import LkPageLocators
import allure

class LkPage(BasePage):
    @allure.step('Открыли браузер по ссылке ' + ROOT_SITE)
    def go_to_site(self):
        return self.driver.get(ROOT_SITE)

    @allure.step('Идем в ЛК')
    def but_lk_click(self):
        self.click_elem_with_wait(LkPageLocators.BUT_LOGIN)

    @allure.step('Вводим почту и пароль, логинимся')
    def lk_login(self):
        self.fill_elem_text(LkPageLocators.LK_LGOIN, LK_LOGIN)
        self.fill_elem_text(LkPageLocators.LK_PASS, LK_PASS)
        self.click_elem_with_wait(LkPageLocators.BUT_LOGGING)

    @allure.step('Идем в историю заказов')
    def but_hist_click(self):
        self.click_elem_with_wait(LkPageLocators.ORDER_HIST)

    @allure.step('Выходим из ЛК')
    def exit_lk(self):
        self.click_elem_with_wait(LkPageLocators.BUT_EXIT)