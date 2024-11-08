from fastapi.testclient import TestClient

from main import app

client = TestClient(app)


def test_qrcode_nodata():
    response = client.get("/api/qrcode")
    assert response.status_code == 422
    assert response.json() == {
        "detail": [
            {
                "type": "missing",
                "loc": ["query", "data"],
                "msg": "Field required",
                "input": None,
            }
        ]
    }


def test_qrcode_data():
    params = {"data": "hola"}
    response = client.get("/api/qrcode", params=params)
    assert response.status_code == 200
    assert response.headers["content-type"] == "image/png"
    assert isinstance(response.content, (bytes, bytearray))
