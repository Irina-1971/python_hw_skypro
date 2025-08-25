import pytest
import allure
from selenium import webdriver
from login_page import LoginPage
from inventory_page import InventoryPage
from cart_page import CartPage
from checkout_page import CheckoutPage

@pytest.fixture
def browser():
    driver = webdriver.Chrome()
    yield driver
    driver.quit()

@allure.title("Оформление заказа в SauceDemo")
@allure.description("Тест проверяет полный процесс оформления заказа: авторизацию, добавление товаров, заполнение информации и проверку суммы")
@allure.feature("Checkout Process")
@allure.severity(allure.severity_level.CRITICAL)
def test_saucedemo_checkout(browser):
    with allure.step("1. Авторизация"):
        login_page = LoginPage(browser)
        login_page.open()
        login_page.enter_username("standard_user")
        login_page.enter_password("secret_sauce")
        login_page.click_login()

    with allure.step("2. Добавление товаров в корзину"):
        inventory_page = InventoryPage(browser)
        inventory_page.add_backpack()
        inventory_page.add_tshirt()
        inventory_page.add_onesie()
        inventory_page.go_to_cart()

    with allure.step("3. Проверка корзины и переход к оформлению"):
        cart_page = CartPage(browser)
        with allure.step("Проверка количества товаров в корзине"):
            assert cart_page.get_cart_items_count() == 3, "В корзине должно быть 3 товара"
        cart_page.click_checkout()

    with allure.step("4. Заполнение информации о доставке"):
        checkout_page = CheckoutPage(browser)
        checkout_page.fill_shipping_info("John", "Doe", "12345")
        checkout_page.click_continue()

    with allure.step("5. Проверка итоговой суммы"):
        total_amount = checkout_page.get_total_amount()
        with allure.step(f"Проверка что сумма равна $58.29, получено: {total_amount}"):
            assert total_amount == "Total: $58.29", f"Ожидалась сумма $58.29, но получено {total_amount}"