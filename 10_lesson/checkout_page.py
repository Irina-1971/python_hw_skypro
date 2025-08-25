import allure
from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webdriver import WebDriver

class CheckoutPage:
    def __init__(self, driver: WebDriver) -> None:
        self.driver = driver
        self.first_name_field = (By.ID, "first-name")
        self.last_name_field = (By.ID, "last-name")
        self.zip_code_field = (By.ID, "postal-code")
        self.continue_button = (By.ID, "continue")
        self.total_amount_label = (By.CLASS_NAME, "summary_total_label")
    
    @allure.step("Заполнение информации о доставке: имя={first_name}, фамилия={last_name}, почтовый индекс={zip_code}")
    def fill_shipping_info(self, first_name: str, last_name: str, zip_code: str) -> None:
        """Заполняет информацию о доставке"""
        self.driver.find_element(*self.first_name_field).send_keys(first_name)
        self.driver.find_element(*self.last_name_field).send_keys(last_name)
        self.driver.find_element(*self.zip_code_field).send_keys(zip_code)
    
    @allure.step("Нажатие кнопки продолжения")
    def click_continue(self) -> None:
        """Нажимает кнопку продолжения"""
        self.driver.find_element(*self.continue_button).click()
    
    @allure.step("Получение итоговой суммы")
    def get_total_amount(self) -> str:
        """Возвращает итоговую сумму заказа"""
        return self.driver.find_element(*self.total_amount_label).text