from fastapi.testclient import TestClient

from app.main import app

client = TestClient(app)


def test_get_users():
    response = client.get("/api/users")
    assert response.status_code == 200
    assert isinstance(response.json(), list)


def test_create_user():
    response = client.post("/api/users", data={"username": "alex"})
    assert response.status_code == 200
    assert response.json().get("_id")
    assert response.json().get("username") == "alex"


def test_get_new_user_logs():
    response = client.post("/api/users", data={"username": "matt"})
    id = response.json().get("_id")
    response = client.get(f"/api/users/{id}/logs")
    assert response.json().get("log") == []


def test_create_user_exercises():
    response = client.post("/api/users", data={"username": "jamie"})
    id = response.json().get("_id")
    response = client.post(
        f"/api/users/{id}/exercises",
        data={"description": "run day", "duration": 60, "date": "2021-01-11"},
    )
    assert response.json() == {
        "_id": id,
        "description": "run day",
        "duration": 60,
        "date": "Mon Jan 11 2021",
        "username": "jamie",
    }


def test_get_user_logs():
    response = client.post("/api/users", data={"username": "nick"})
    id = response.json().get("_id")
    client.post(
        f"/api/users/{id}/exercises",
        data={"description": "run day", "duration": 60, "date": "2021-02-10"},
    )
    client.post(
        f"/api/users/{id}/exercises",
        data={"description": "jump day", "duration": 60, "date": "2021-02-11"},
    )
    client.post(
        f"/api/users/{id}/exercises",
        data={"description": "run day", "duration": 60, "date": "2021-02-12"},
    )
    client.post(
        f"/api/users/{id}/exercises",
        data={"description": "jump day", "duration": 60, "date": "2021-02-13"},
    )
    client.post(
        f"/api/users/{id}/exercises",
        data={"description": "run day", "duration": 60, "date": "2021-02-14"},
    )
    client.post(
        f"/api/users/{id}/exercises",
        data={"description": "jump day", "duration": 60, "date": "2021-02-14"},
    )
    client.post(
        f"/api/users/{id}/exercises",
        data={"description": "run day", "duration": 60, "date": "2021-02-15"},
    )
    client.post(
        f"/api/users/{id}/exercises",
        data={"description": "jump day", "duration": 60, "date": "2021-02-16"},
    )
    assert len(client.get(f"/api/users/{id}/logs?limit=2").json().get("log")) == 2
    assert (
        len(client.get(f"/api/users/{id}/logs?from=2021-02-13").json().get("log")) == 5
    )
    assert len(client.get(f"/api/users/{id}/logs?to=2021-02-15").json().get("log")) == 7
    assert (
        len(
            client.get(f"/api/users/{id}/logs?from=2021-02-11&to=2021-02-14")
            .json()
            .get("log")
        )
        == 5
    )
