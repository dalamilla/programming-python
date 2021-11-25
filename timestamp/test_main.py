from datetime import datetime, timezone

from fastapi.testclient import TestClient

from main import app

client = TestClient(app)

def test_date():
    response = client.get("/api/2016-12-25")
    assert response.status_code == 200
    assert response.json() == {"unix": 1482624000000, "utc": "Sun, 25 Dec 2016 00:00:00 GMT"}

def test_date_epoch():
    response = client.get("/api/1451001600000")
    assert response.status_code == 200
    assert response.json() == {"unix": 1451001600000, "utc": "Fri, 25 Dec 2015 00:00:00 GMT"}

def test_date_with_space():
    response = client.get("/api/05%20October%202011")
    assert response.status_code == 200
    assert response.json() == {"unix": 1317772800000, "utc": "Wed, 05 Oct 2011 00:00:00 GMT"}

def test_no_a_date():
    response = client.get("/api/this-is-not-a-date")
    assert response.status_code == 400
    assert response.json() == {"error": "Invalid Date"}

def test_date_now():
    current = datetime.now(timezone.utc)
    unix = int(current.timestamp() * 1000)
    utc = current.strftime('%a, %d %b %Y %H:%M:%S GMT')
    response = client.get("/api/{}".format(unix))
    assert response.status_code == 200
    assert response.json() == {"unix": unix ,"utc": utc}

def test_no_parameter():
    current = datetime.now(timezone.utc)
    unix = int(current.timestamp())
    utc = current.strftime('%a, %d %b %Y %H:%M:%S GMT')
    response = client.get("/api")
    assert response.status_code == 200
    assert response.json().get('utc') == utc
    assert int(response.json().get('unix') / 1000) == unix
