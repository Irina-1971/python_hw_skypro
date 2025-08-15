import pytest
import requests

BASE_URL = "https://yougile.com/api-v2"

Key = ""
headers = {
"Authorization": Key,
"Content-Type": "application/json"
}


def test_create_company():
    payload={
"title": ""
}
    
    response = requests.post(BASE_URL+'/projects', headers=headers, json=payload)

    assert response.status_code == 400




def test_get_negativ():

responce = requests.get(base_url + '/projects/' + '1', headers=headers)
assert responce.status_code == 404


def test_edit_company():
    payload={
"title": "home1"
}
    
    response = requests.post(BASE_URL+'/projects', headers=headers, json=payload)
    project_id = response.json()["id"]
    payload={
        "title": "home2"
    }

    response = requests.put(BASE_URL+'/projects'+project_id, headers=headers, json=payload)

    assert response.status_code == 400
    response = requests.get(BASE_URL+'/projects'+project_id +1, headers=headers)
    data = response.json()
    assert data["title"] == "home2"