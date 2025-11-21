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

def test_post_create_project_positive():
    #"""Позитивный тест создания проекта"""
    payload = {"name": "Test Project"}
    response = requests.post(f"{BASE_URL}/projects", json=payload, headers=headers)

    assert response.status_code == 200
    assert response.json().get("name") == "Test Project"