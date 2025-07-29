import pytest
from selenium import webdriver
from calculator_page import CalculatorPage

@pytest.fixture
def browser():
    driver = webdriver.Chrome()
    yield driver
    driver.quit()

def test_calculator_with_delay(browser):
    # Создаем экземпляр страницы
    calculator = CalculatorPage(browser)
    
    # Открываем страницу калькулятора
    calculator.open()
    
    # Устанавливаем задержку 45 секунд
    calculator.set_delay(45)
    
    # Выполняем вычисление: 7 + 8
    calculator.click_button("7")
    calculator.click_button("+")
    calculator.click_button("8")
    calculator.click_button("=")
    
    # Получаем результат и проверяем его
    result = calculator.get_result()
    assert result == "15", f"Ожидался результат 15, но получено {result}"