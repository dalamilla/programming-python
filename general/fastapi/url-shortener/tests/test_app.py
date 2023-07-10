from fastapi.testclient import TestClient

from app.main import app

client = TestClient(app)


def test_get_not_found():
    response = client.get("/api/shorturl/1000")
    assert response.status_code == 200
    assert response.json() == {"error": "No short URL found for the given input"}


def test_get_incorrect_format():
    response = client.get("/api/shorturl/text")
    assert response.status_code == 200
    assert response.json() == {"error": "Wrong format"}


def test_post_invalid_url():
    response = client.post("/api/shorturl", data={"url": "http://localhost"})
    assert response.status_code == 200
    assert response.json() == {"error": "invalid url"}


def test_post_url():
    response = client.post(
        "/api/shorturl", data={"url": "https://www.freecodecamp.org/"}
    )
    assert response.status_code == 200
    assert response.json().get("original_url") == "https://www.freecodecamp.org/"


def test_redirect_url():
    post = client.post("/api/shorturl", data={"url": "https://teachyourselfcs.com/"})
    short_url = post.json().get("short_url")
    response = client.get(f"/api/shorturl/{short_url}")
    assert response.history[0].status_code == 302
    assert response.url == "https://teachyourselfcs.com/"
