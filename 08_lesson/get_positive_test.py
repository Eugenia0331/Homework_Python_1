import pytest
import requests

BASE_URL = "https://yougile.com/api/v1"
API_TOKEN = "YOUR_TOKEN_HERE"

headers = {
    "Authorization": f"Bearer {API_TOKEN}",
    "Content-Type": "application/json"
}
# -----------------------------
#            GET
# -----------------------------

def test_get_project_positive(created_project):
    """Позитивный тест получения проекта"""
    response = requests.get(f"{BASE_URL}/projects/{created_project}", headers=headers)

    assert response.status_code == 200
    assert response.json().get("id") == created_project
