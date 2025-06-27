from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.firefox.service import Service
from webdriver_manager.firefox import GeckoDriverManager

# Настройка Firefox
driver = webdriver.Firefox(service=Service(GeckoDriverManager().install()))

try:
    # 1. Перейти на страницу
    driver.get("http://the-internet.herokuapp.com/inputs")
    
    # 2. Найти поле ввода
    input_field = driver.find_element(By.CSS_SELECTOR, "input[type='number']")
    
    # 3. Ввести текст "Sky"
    input_field.send_keys("Sky")
    print("Текст 'Sky' введен успешно")
    
    # 4. Очистить поле
    input_field.clear()
    print("Поле очищено")
    
    # 5. Ввести текст "Pro"
    input_field.send_keys("Pro")
    print("Текст 'Pro' введен успешно")
    
    # Небольшая пауза для наглядности (необязательно)
    import time
    time.sleep(2)
    
finally:
    # 6. Закрыть браузер
    driver.quit()
    print("Браузер закрыт")