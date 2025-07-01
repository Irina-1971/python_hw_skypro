from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
import time

def click_blue_button():
    
    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
    
    try:
    
        driver.get("http://uitestingplayground.com/dynamicid")
        
        for i in range(3):  
          
            button = driver.find_element(By.CSS_SELECTOR, "button.btn-primary")
            button.click()
            print(f"Клик {i+1} выполнен успешно")
            time.sleep(1)  
    except Exception as e:
        print(f"Произошла ошибка: {e}")
    finally:
        driver.quit()


click_blue_button()

