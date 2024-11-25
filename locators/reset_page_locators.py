from selenium.webdriver.common.by import By

class ResetPageLocators:
    BUT_LOGIN = [By.XPATH, "//p[text()='Личный Кабинет']"]  # кнопка логина
    BUT_RECOVER = [By.XPATH, "//a[text()='Восстановить пароль']"]  # кнопка восстановления пароля
    MAIL = [By.XPATH, "//label[text()='Email']/parent::div/input"]  # почта
    DO_RECOVER = [By.XPATH, "//button[text()='Восстановить']"]  #отдельная кнопка восстановить
    SHOW_PASS = [By.CLASS_NAME, "input__icon"]  #кнопка для показа пароля
    PASS_INPUT = [By.XPATH, "//label[text()='Пароль']/parent::div/input"] #поле ввода пароля