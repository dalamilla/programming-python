from fastapi.testclient import TestClient

from main import app

client = TestClient(app)


def test_whoami():
    response = client.get("/api/whoami", 
        headers={"user-agent": "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/96.0.4664.45 Safari/537.36", 
                    "accept-language": "en-US,en;q=0.9,es;q=0.8"})
    assert response.status_code == 200
    assert response.json() == {"software": "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/96.0.4664.45 Safari/537.36", 
                                "language": "en-US,en;q=0.9,es;q=0.8", "ipaddress": "testclient"}
