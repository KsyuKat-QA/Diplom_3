from selenium.webdriver.common.by import By

class OrderPageLocators:
    LENTA_ORDERS = [By.XPATH, "//p[text()='Лента Заказов']"]  # Лента Заказов
    ORDER_LIST_ELEM = [By.XPATH, "//div/main/div/div/ul/li[{}]"]  # Элемент из ленты заказов
    ORDER_LIST_ELEM_ID = [By.XPATH, "//div/main/div/div/ul/li[{}]/a/div[1]/p[1]"]  # id заказа
    MODAL_ORDER_ID = [By.XPATH, "//div/section[2]/div[1]/div/p[1]"] #id на модальной форме при нажатии из ленты
    MODAL_ORDER_ID_FROM_MAIN = [By.XPATH, "//div/section/div[1]/div/h2"]  # id на модальной форме в момент заказа с главной странцы
    TOTAL_DONE = [By.XPATH, "//div/main/div/div/div/div[2]/p[2]"]  # Выполнено за все время, число
    TODAY_DONE = [By.XPATH, "//div/main/div/div/div/div[3]/p[2]"]  # Выполнено за сегодня, число
    CLOSE_ORD_DONE = [By.XPATH, "//div/section/div[1]/button"]  # когда заказали бургер, закрываем форму
    HIST_ORDERS = [By.XPATH, "//a[text()='История заказов']"]  # История заказов в ЛК
    HIST_ELEMS = [By.XPATH, "//div/main/div/div/div/ul/li"]  # список элементов в истории
    LENTA_ELEMS = [By.XPATH, "//div/main/div/div/ul/li"]  # список элементов в ленте заказов
    ORDERS_IN_WORK = [By.XPATH, "//div/main/div/div/div/div[1]/ul[2]"]  # список элементов в ленте заказов