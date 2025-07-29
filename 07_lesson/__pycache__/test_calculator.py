from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class CalculatorPage:
    def __init__(self, driver):
        self.driver = driver
        self.delay_input = (By.CSS_SELECTOR, "#delay")
        self.result_field = (By.CSS_SELECTOR, ".screen")
        
    def open(self):
        self.driver.get("https://bonigarcia.dev/selenium-webdriver-java/slow-calculator.html")
        
    def set_delay(self, delay):
        self.driver.find_element(*self.delay_input).clear()
        self.driver.find_element(*self.delay_input).send_keys(str(delay))
        
    def click_button(self, button_text):
        button_locator = (By.XPATH, f"//span[text()='{button_text}']")
        self.driver.find_element(*button_locator).click()
        
    def get_result(self, timeout=50):
        wait = WebDriverWait(self.driver, timeout)
        result_element = wait.until(
            EC.text_to_be_present_in_element(self.result_field, "")
        )
        return self.driver.find_element(*self.result_field).text