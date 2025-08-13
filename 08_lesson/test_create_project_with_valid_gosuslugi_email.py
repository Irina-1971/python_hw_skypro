import pytest
import requests
import random
import re

class TestGosuslugiEmailAPI:
    BASE_URL = "https://yougile.com/api-v2/"
    
    @pytest.fixture
    def auth_headers(self):
        """Фикстура для аутентификации и получения токена"""
        auth_data = {
            "username": "test_user@example.com",
            "password": "test_password123"
        }
        response = requests.post(f"{self.BASE_URL}auth/login", json=auth_data)
        assert response.status_code == 200, "Ошибка аутентификации"
        return {
            "Authorization": f"Bearer {response.json()['token']}",
            "Content-Type": "application/json"
        }
    
    @pytest.fixture
    def random_project_name(self):
        """Генерация уникального имени проекта"""
        return f"Госуслуги_Проект_{random.randint(1000, 9999)}"
    
    @pytest.fixture
    def valid_gosuslugi_email(self):
        """Генерация валидного email Госуслуг"""
        return f"user{random.randint(100, 999)}@gosuslugi.ru"
    
    @pytest.fixture
    def invalid_email(self):
        """Генерация невалидного email"""
        return "invalid_email_format"

    # ====================
    # ПОЗИТИВНЫЙ ТЕСТ
    # ====================

    def test_create_project_with_valid_gosuslugi_email(self, auth_headers, random_project_name, valid_gosuslugi_email):
        """Позитивный тест: создание проекта с валидной почтой Госуслуг"""
        project_data = {
            "name": random_project_name,
            "description": "Проект с валидной почтой Госуслуг",
            "emailSettings": {
                "type": "GOSUSLUGI",
                "config": {
                    "adminEmail": valid_gosuslugi_email,
                    "notificationEmail": valid_gosuslugi_email,
                    "domain": "gosuslugi.ru"
                }
            }
        }
        
        response = requests.post(
            f"{self.BASE_URL}projects",
            json=project_data,
            headers=auth_headers
        )
        
        assert response.status_code == 201, "Не удалось создать проект"
        
        # Проверяем, что email сохранился корректно
        assert response.json()["emailSettings"]["type"] == "GOSUSLUGI"
        assert response.json()["emailSettings"]["config"]["adminEmail"] == valid_gosuslugi_email
        assert response.json()["emailSettings"]["config"]["notificationEmail"] == valid_gosuslugi_email
        
        # Проверяем формат email
        assert re.match(r"^[a-zA-Z0-9_.+-]+@gosuslugi\.ru$", 
                       response.json()["emailSettings"]["config"]["adminEmail"])
        
        # Очистка
        project_id = response.json()["id"]
        requests.delete(f"{self.BASE_URL}projects/{project_id}", headers=auth_headers)
