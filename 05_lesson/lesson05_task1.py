
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
import time

def test_blue_button():
  
    driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
    
    try:
       
        driver.get("http://uitestingplayground.com/classattr")
        
       
        blue_button = driver.find_element(By.CSS_SELECTOR, ".btn-primary")
        blue_button.click()
        
       
        time.sleep(1)  
        alert = driver.switch_to.alert
        alert.accept()
        
        print("Успешно выполнено!")
  
    finally:
      
        driver.quit()


for i in range(3):
    print(f"Запуск #{i+1}")
    test_blue_button()
    time.sleep(1)  
