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

def test_put_update_project_negative():
    #"""Негативный тест: обновление несуществующего проекта"""
    payload = {"name": "Should Not Update"}
    response = requests.put(f"{BASE_URL}/projects/invalid-id-123", json=payload, headers=headers)

    assert response.status_code == 404
    assert "not found" in response.text.lower()
