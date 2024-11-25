from selenium.webdriver.common.by import By

class RootPageLocators:
    KONSTRUKT = [By.XPATH, "//p[text()='Конструктор']"]  # кнопка конструктора
    LENTA = [By.XPATH, "//p[text()='Лента Заказов']"]  # кнопка ленты
    KON_LABEL = [By.XPATH, "//h1[text()='Соберите бургер']"]  # надпись конструктора
    LOADING = [By.XPATH, "//div[text()='Загрузка...']"]  # Надпись загрузки
    LENTA_LABEL = [By.XPATH, "//h1[text()='Лента заказов']"]  # Лента заказов

    BURG_ELEM = [By.XPATH, "//div/main/section[1]/div[2]/ul[{}]/a[{}]"]  # динамический локатор для элементов бургера. первый параметр - строка, вторая - элемент
                                                            #общий вид должен быть /div/main/section[1]/div[2]/ul[1]/a[2]
                                                            #первая строка второй элемент = Краторная булка N-200i (для примера)

    INGDR_LABEL = [By.XPATH, "//h2[text()='Детали ингредиента']"]  # инфа об ингридиенте
    CLOSE = [By.XPATH, "//div/section[1]/div[1]/button"]  # крестик

    BURG_STRUCT = [By.XPATH, "//div/main/section[2]/ul"] #структура бургера, куда перетаскиваем элементы (правая часть)
    COUNTER = [By.XPATH, "//div/main/section[1]/div[2]/ul[{}]/a[{}]/div[1]"]
    BUT_ORDER = [By.XPATH, "//button[text()='Оформить заказ']"] #кнопка оформить заказ
    LABEL_ORDER = [By.XPATH, "//p[text()='идентификатор заказа']"]  # надпись
