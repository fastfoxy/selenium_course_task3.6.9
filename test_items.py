from selenium.webdriver.common.by import By

link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/"

def test_add_in_card_button_present(browser):
    # открываем страницу по ссылке
    browser.get(link)
    # добавляем неявное ожидание появления элементов
    browser.implicitly_wait(10)
    # находим кнопку по имени класса
    add_in_card_button = browser.find_element(By.CLASS_NAME, "btn-add-to-basket")
    # проверяем, что кнопка найдена (объект существует, не равен None)
    assert add_in_card_button is not None, "Button not found!"