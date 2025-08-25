import allure
from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webdriver import WebDriver

class CartPage:
    def __init__(self, driver: WebDriver) -> None:
        self.driver = driver
        self.cart_items = (By.CLASS_NAME, "cart_item")
        self.checkout_button = (By.ID, "checkout")
    
    @allure.step("Получение количества товаров в корзине")
    def get_cart_items_count(self) -> int:
        """Возвращает количество товаров в корзине"""
        return len(self.driver.find_elements(*self.cart_items))
    
    @allure.step("Нажатие кнопки оформления заказа")
    def click_checkout(self) -> None:
        """Нажимает кнопку оформления заказа"""
        self.driver.find_element(*self.checkout_button).click()