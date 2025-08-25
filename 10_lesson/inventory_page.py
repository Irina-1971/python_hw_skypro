import allure
from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webdriver import WebDriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class InventoryPage:
    def __init__(self, driver: WebDriver) -> None:
        self.driver = driver
        self.backpack_add_button = (By.ID, "add-to-cart-sauce-labs-backpack")
        self.tshirt_add_button = (By.ID, "add-to-cart-sauce-labs-bolt-t-shirt")
        self.onesie_add_button = (By.ID, "add-to-cart-sauce-labs-onesie")
        self.cart_link = (By.CLASS_NAME, "shopping_cart_link")
        self.cart_badge = (By.CLASS_NAME, "shopping_cart_badge")
    
    @allure.step("Добавление рюкзака в корзину")
    def add_backpack(self) -> None:
        """Добавляет рюкзак в корзину"""
        self.driver.find_element(*self.backpack_add_button).click()
    
    @allure.step("Добавление футболки в корзину")
    def add_tshirt(self) -> None:
        """Добавляет футболку в корзину"""
        self.driver.find_element(*self.tshirt_add_button).click()
    
    @allure.step("Добавление комбинезона в корзину")
    def add_onesie(self) -> None:
        """Добавляет комбинезон в корзину"""
        self.driver.find_element(*self.onesie_add_button).click()
    
    @allure.step("Переход в корзину")
    def go_to_cart(self) -> None:
        """Переходит в корзину"""
        self.driver.find_element(*self.cart_link).click()
    
    @allure.step("Получение количества товаров в корзине")
    def get_cart_items_count(self) -> int:
        """Возвращает количество товаров в корзине"""
        try:
            badge = self.driver.find_element(*self.cart_badge)
            return int(badge.text)
        except:
            return 0