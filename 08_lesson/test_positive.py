import pytest
import requests

BASE_URL = "https://yougile.com/api-v2"

Key = "Bearer aXmps1CRXMr6oUpcsv06juMB8ZtG7X+5-HSnhOlB338SqEzGxzZIxAdX1iWbrqQU"
headers = {
"Authorization": Key,
"Content-Type": "application/json"
}


def test_create_company():
    payload={
"title": "home"
}
    
    response = requests.post(BASE_URL+'/projects', headers=headers, json=payload)

    assert response.status_code == 201

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

    assert response.status_code == 200
    response = requests.get(BASE_URL+'/projects'+project_id, headers=headers)
    data = response.json()
    assert data["title"] == "home2"

def test_get_company():
    payload={
"title": "home3"
}
    response = requests.post(BASE_URL+'/projects', headers=headers, json=payload)
    project_id = response.json()["id"]  

    response = requests.get(BASE_URL+'/projects'+project_id, headers=headers)
    data = response.json()
    assert data["title"] == "home3"


