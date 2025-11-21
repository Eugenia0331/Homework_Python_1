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

def test_get_project_negative():
    #"""Негативный тест: запрос проекта с неверным ID"""
    response = requests.get(f"{BASE_URL}/projects/nonexisting-id", headers=headers)

    assert response.status_code == 404
    assert "not found" in response.text.lower()
