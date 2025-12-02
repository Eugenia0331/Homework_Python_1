import requests

key = "key"
base_url = "base_url"
headers = {"Authorization": f"Bearer {key}"}


def test_create_project():
    body = {
        "title": "Новый проект"
    }
    r = requests.post("https://ru.yougile.com/api-v2/projects", headers=headers, json=body)
    assert r.status_code == 201

import requests

def test_create_project_negative():
    body = {
        "title": "Новый проект"
    }
    # Отправляем запрос без headers (без авторизации)
    r = requests.post("https://ru.yougile.com/api-v2/projects", headers={}, json=body)

    # Выводим статус и ответ для отладки
    print("Status code:", r.status_code)
    print("Response body:", r.text)

    # Проверяем, что сервер вернул 401 Unauthorized
    assert r.status_code == 401, f"Ожидали 401, но получили {r.status_code}"

def test_edit_project():
    body = {
        "title": "Новый проект"
    }
    body2 = {
        "title": "Новый проект 2"
    }
    r = requests.post(f"{base_url}/projects", headers=headers, json=body)
    assert r.status_code == 201
    id = r.json()["id"]
    r2 = requests.put(f"{base_url}/projects/{id}", headers=headers, json=body2)
    assert r2.status_code == 200

    data = r.json()
    assert "id" in data, "В ответе нет ключа 'id'"
    project_id = data["id"]

def test_edit_project_negative():
    body = {
        "title": "Новый проект"
    }
    body2 = {
        "title": ""
    }
    r = requests.post(f"{base_url}/projects", headers=headers, json=body)
    assert r.status_code == 201
    id = r.json()["id"]
    r2 = requests.put(f"{base_url}/projects/{id}", headers=headers, json=body2)
    assert r2.status_code == 400


def test_get_project():
    body = {
        "title": "Новый проект"
    }
    r = requests.post(f"{base_url}/projects", headers=headers, json=body)
    assert r.status_code == 201
    id = r.json()["id"]
    r2 = requests.get(f"{base_url}/projects/{id}", headers=headers)
    assert r2.status_code == 200
    assert r2.json()["title"] == "Новый проект"


def test_get_project_negative():
    id = "key"
    r2 = requests.get(f"{base_url}/projects/{id}", headers=headers)
    assert r2.status_code == 404

