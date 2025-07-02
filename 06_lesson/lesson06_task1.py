from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


driver = webdriver.Chrome()  
driver.get("http://uitestingplayground.com/ajax")

ajax_button = driver.find_element(By.ID, "ajaxButton")
ajax_button.click()


try:
    success_message = WebDriverWait(driver, 10).until(
        EC.visibility_of_element_located((By.CLASS_NAME, "bg-success"))
    )
    text = success_message.text
    print(text)  
except Exception as e:
    print("Элемент не найден:", e)
finally:
    driver.quit()  