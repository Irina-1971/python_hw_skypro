from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

# 1. Инициализация драйвера (используем Edge)
driver = webdriver.Edge()  # Для Safari: webdriver.Safari()

try:
    # 2. Переход на страницу
    driver.get("http://uitestingplayground.com/textinput")
    
    # 3. Ввод текста "SkyPro" в поле
    input_field = driver.find_element(By.ID, "newButtonName")
    input_field.clear()  # Очищаем поле на случай, если там есть текст
    input_field.send_keys("SkyPro")
    
    # 4. Нажатие на синюю кнопку
    blue_button = driver.find_element(By.ID, "updatingButton")
    blue_button.click()
    
    # 5. Получение текста кнопки
    button_text = blue_button.text
    
    # 6. Вывод результата в консоль
    print("Текст кнопки:", button_text)  # Должно вывести "SkyPro"
    
    # Проверка с помощью assert (опционально)
    assert button_text == "SkyPro", f"Ожидался текст 'SkyPro', получено '{button_text}'"

finally:
    # 7. Закрытие браузера
    driver.quit()