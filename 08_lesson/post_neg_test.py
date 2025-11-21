import pytest
import requests

BASE_URL = "https://yougile.com/api/v1"
API_TOKEN = "YOUR_TOKEN_HERE"

headers = {
    "Authorization": f"Bearer {API_TOKEN}",
    "Content-Type": "application/json"
}

# -----------------------------
#            POST
# -----------------------------

def test_post_create_project_negative():
    #"""Негативный тест: переданы некорректные данные"""
    payload = {"name": ""}  # Пустое имя → ошибка
    response = requests.post(f"{BASE_URL}/projects", json=payload, headers=headers)

    assert response.status_code in (400, 422)  # зависит от API

    assert "error" in response.text.lower()
