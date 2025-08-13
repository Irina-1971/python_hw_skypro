import pytest
import requests
import random
import string

class TestGetCompanyByIdAPI:
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
    def test_company(self, auth_headers):
        """Фикстура для создания тестовой компании"""
        company_name = f"TestCompany_{''.join(random.choices(string.ascii_letters, k=8))}"
        company_data = {
            "name": company_name,
            "description": "Тестовая компания для API тестов",
            "isPublic": True
        }
        response = requests.post(
            f"{self.BASE_URL}projects",
            json=company_data,
            headers=auth_headers
        )
        assert response.status_code == 201, "Не удалось создать тестовую компанию"
        company_id = response.json()["id"]
        yield company_id
        
        # Удаление компании после теста
        requests.delete(
            f"{self.BASE_URL}projects/{company_id}",
            headers=auth_headers
        )

    # ====================
    # ПОЗИТИВНЫЕ ТЕСТЫ
    # ====================

    def test_get_company_by_id_positive(self, auth_headers, test_company):
        """Позитивный тест получения компании по валидному ID"""
        response = requests.get(
            f"{self.BASE_URL}projects/{test_company}",
            headers=auth_headers
        )
        
        assert response.status_code == 200
        assert response.json()["id"] == test_company
        assert "name" in response.json()
        assert "description" in response.json()
        assert "createdAt" in response.json()
        assert "updatedAt" in response.json()

