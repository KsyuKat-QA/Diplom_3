from pages.base_page import BasePage
from data import *
from locators.reset_page_locators import ResetPageLocators
import allure

class ResetPage(BasePage):
    @allure.step('Открыли браузер по ссылке ' + ROOT_SITE)
    def go_to_site(self):
        self.driver.get(ROOT_SITE)
        return self.driver

    @allure.step('Щелкнули по входу в ЛК')
    def lk_click(self):
        self.click_elem_with_wait(ResetPageLocators.BUT_LOGIN)

    @allure.step('Открыли форму восстановления пароля')
    def but_recover_click(self):
        self.click_elem_with_wait(ResetPageLocators.BUT_RECOVER)

    @allure.step('Указали почту')
    def fill_mail(self, mail):
        self.fill_elem_text(ResetPageLocators.MAIL, mail)

    @allure.step('Нажали кнопку восстановления пароля')
    def but_recover_final_click(self):
        self.click_elem_with_wait(ResetPageLocators.DO_RECOVER)

    @allure.step('Нажали кнопку показать пароль')
    def show_pass(self):
        self.click_elem_with_wait(ResetPageLocators.SHOW_PASS)