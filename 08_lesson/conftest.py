import pytest
import requests
import random
import string

@pytest.fixture
def base_url():
    return "https://yougile.com/api-v2/"

@pytest.fixture
def test_credentials():
    return {
        "username": "test_user@example.com",
        "password": "test_password123"
    }