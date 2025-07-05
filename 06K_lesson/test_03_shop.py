from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# 1. Инициализация драйвера (используем Edge)
driver = webdriver.Edge()  # Для Safari: webdriver.Safari()

try:
    # 2. Переход на страницу
    driver.get("https://bonigarcia.dev/selenium-webdriver-java/loading-images.html")
    
    # 3. Ожидание загрузки всех изображений (исчезновение спиннера)
    WebDriverWait(driver, 10).until(
        EC.invisibility_of_element_located((By.ID, "spinner"))
    )
    
    # 4. Получение всех изображений
    images = driver.find_elements(By.CSS_SELECTOR, "#image-container img")
    
    # 5. Проверка, что изображений достаточно
    if len(images) >= 3:
        # 6. Получение атрибута src у 3-й картинки (индекс 2)
        third_image_src = images[2].get_attribute("src")
        
        # 7. Вывод результата в консоль
        print("URL третьей картинки:", third_image_src)
    else:
        print("Ошибка: На странице меньше 3 изображений")

finally:
    # 8. Закрытие браузера
    driver.quit()