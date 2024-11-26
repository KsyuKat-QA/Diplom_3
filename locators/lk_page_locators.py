from selenium.webdriver.common.by import By

class LkPageLocators:
    BUT_LOGIN = [By.XPATH, "//p[text()='Личный Кабинет']"]  #кнопка "Личный Кабинет" вверху справа
    LK_LGOIN = [By.XPATH, "//label[text()='Email']/parent::div/input"]  #поле ввода почты
    LK_PASS = [By.XPATH, "//label[text()='Пароль']/parent::div/input"]  #поле ввода пароля
    BUT_LOGGING = [By.XPATH, "//button[text()='Войти']"]  # кнопка "Войти" после ввода данных
    ORDER_HIST = [By.XPATH, "//a[text()='История заказов']"]  # история заказов
    BUT_EXIT = [By.XPATH, "//button[text()='Выход']"]  # выйти
    LOADING = [By.XPATH, "//div[text()='Загрузка...']"]  # Надпись загрузки
    BUT_RECOVER =  [By.XPATH, "//a[text()='Восстановить пароль']"]   #кнопка восстановления пароля