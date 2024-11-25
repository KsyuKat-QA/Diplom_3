from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions

class BasePage:
    def_waits = 4  # сколько готовы ждать

    def __init__(self, driver):
        self.driver = driver

    def find_elem_with_wait(self, locator):
        WebDriverWait(self.driver, self.def_waits).until(expected_conditions.visibility_of_element_located(locator))
        return self.driver.find_element(*locator)

    def find_elems_with_wait(self, locator):
        WebDriverWait(self.driver, self.def_waits).until(expected_conditions.presence_of_element_located(locator))
        return self.driver.find_elements(*locator)

    def click_elem_with_wait(self, locator):
        WebDriverWait(self.driver, self.def_waits).until(expected_conditions.element_to_be_clickable(locator))
        self.driver.find_element(*locator).click()

    def wait_elem_hide(self, locator): #ждем скрытия элемента
        WebDriverWait(self.driver, self.def_waits).until(expected_conditions.invisibility_of_element_located(locator))

    def fill_elem_text(self, locator, text):
        self.find_elem_with_wait(locator).send_keys(text)

    def get_elem_text(self, locator):
        return self.find_elem_with_wait(locator).text

    def get_cur_url(self):
        return self.driver.current_url

    def check_active_element(self, locator):
        return self.driver.switch_to.active_element == self.find_elem_with_wait(locator)

    def elem_is_clickable(self, locator):
        return WebDriverWait(self.driver, self.def_waits).until(expected_conditions.element_to_be_clickable(locator)) == self.find_elem_with_wait(locator)