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
    
    def test_create_project_with_invalid_gosuslugi_email(self, auth_headers, random_project_name, invalid_email):
        """Негативный тест: создание проекта с невалидной почтой Госуслуг"""
        project_data = {
            "name": random_project_name,
            "description": "Проект с невалидной почтой Госуслуг",
            "emailSettings": {
                "type": "GOSUSLUGI",
                "config": {
                    "adminEmail": invalid_email,
                    "notificationEmail": invalid_email,
                    "domain": "gosuslugi.ru"
                }
            }
        }
        
        response = requests.post(
            f"{self.BASE_URL}projects",
            json=project_data,
            headers=auth_headers
        )
        
        # Ожидаем ошибку валидации
        assert response.status_code == 400, "Ожидалась ошибка 400 для невалидного email"
        assert "error" in response.json(), "В ответе должна быть информация об ошибке"
        assert "email" in response.json()["error"].lower(), "Ошибка должна относиться к email"