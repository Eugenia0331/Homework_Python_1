import pytest
import requests

BASE_URL = "https://yougile.com/api/v1"
API_TOKEN = "YOUR_TOKEN_HERE"

headers = {
    "Authorization": f"Bearer {API_TOKEN}",
    "Content-Type": "application/json"
}
# -----------------------------
#            PUT
# -----------------------------

@pytest.fixture
def created_project():
    #"""Фикстура — создаёт проект перед тестом"""
    payload = {"name": "Initial Project"}
    response = requests.post(f"{BASE_URL}/projects", json=payload, headers=headers)
    project_id = response.json().get("id")
    return project_id


def test_put_update_project_positive(created_project):
    #"""Позитивный тест обновления проекта"""
    payload = {"name": "Updated Project"}
    response = requests.put(f"{BASE_URL}/projects/{created_project}", json=payload, headers=headers)

    assert response.status_code == 200
    assert response.json().get("name") == "Updated Project"
