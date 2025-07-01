from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.firefox.service import Service
from webdriver_manager.firefox import GeckoDriverManager

def login_and_get_message():
    # Настройка Firefox
    driver = webdriver.Firefox(service=Service(GeckoDriverManager().install()))
    
    try:
        # 1. Открыть страницу логина
        driver.get("http://the-internet.herokuapp.com/login")
        
        # 2. Ввести логин и пароль
        driver.find_element(By.ID, "username").send_keys("tomsmith")
        driver.find_element(By.ID, "password").send_keys("SuperSecretPassword!")
        
        # 3. Нажать кнопку Login
        driver.find_element(By.CSS_SELECTOR, "button.radius").click()
        
        # 4. Получить и вывести текст из зеленой плашки
        flash_message = driver.find_element(By.ID, "flash").text
        clean_message = ' '.join(flash_message.split('\n')[0].split()[1:])
        print("Сообщение после входа:", clean_message)
        
    finally:
        # 5. Закрыть браузер
        driver.quit()
        print("Браузер успешно закрыт")

# Запуск функции
login_and_get_message()