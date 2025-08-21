import pytest
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

def test_saucedemo_checkout(browser):
    # 1. Авторизация
    login_page = LoginPage(browser)
    login_page.open()
    login_page.enter_username("standard_user")
    login_page.enter_password("secret_sauce")
    login_page.click_login()

    # 2. Добавление товаров в корзину
    inventory_page = InventoryPage(browser)
    inventory_page.add_backpack()
    inventory_page.add_tshirt()
    inventory_page.add_onesie()
    inventory_page.go_to_cart()

    # 3. Переход к оформлению заказа
    cart_page = CartPage(browser)
    assert cart_page.get_cart_items_count() == 3, "В корзине должно быть 3 товара"
    cart_page.click_checkout()

    # 4. Заполнение информации о доставке
    checkout_page = CheckoutPage(browser)
    checkout_page.fill_shipping_info("John", "Doe", "12345")
    checkout_page.click_continue()

    # 5. Проверка итоговой суммы
    total_amount = checkout_page.get_total_amount()
    assert total_amount == "Total: $58.29", f"Ожидалась сумма $58.29, но получено {total_amount}"