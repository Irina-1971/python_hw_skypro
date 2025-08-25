import allure
from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webdriver import WebDriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class LoginPage:
    def __init__(self, driver: WebDriver) -> None:
        self.driver = driver
        self.url = "https://www.saucedemo.com/"
        self.username_field = (By.ID, "user-name")
        self.password_field = (By.ID, "password")
        self.login_button = (By.ID, "login-button")
    
    @allure.step("Открытие страницы логина")
    def open(self) -> None:
        """Открывает страницу логина"""
        self.driver.get(self.url)
    
    @allure.step("Ввод имени пользователя: {username}")
    def enter_username(self, username: str) -> None:
        """Вводит имя пользователя в поле ввода"""
        self.driver.find_element(*self.username_field).send_keys(username)
    
    @allure.step("Ввод пароля")
    def enter_password(self, password: str) -> None:
        """Вводит пароль в поле ввода"""
        self.driver.find_element(*self.password_field).send_keys(password)
    
    @allure.step("Нажатие кнопки логина")
    def click_login(self) -> None:
        """Нажимает кнопку входа"""
        self.driver.find_element(*self.login_button).click()