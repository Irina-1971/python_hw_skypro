import pytest
import requests
import random
import string

@pytest.fixture
def base_url():
    return "https://yougile.com/api-v2/"