from fastapi.testclient import TestClient

from main import app

client = TestClient(app)


def test_template_title():
    response = client.get("/")
    assert response.status_code == 200
    assert '<title>Form File</title>' in response.text

def test_template_form_name():
    response = client.get("/")
    assert response.status_code == 200
    assert 'name="upfile"' in response.text

def test_template_form_action():
    response = client.get("/")
    assert response.status_code == 200
    assert 'action="/api/fileanalyse"' in response.text

def test_fileanalyse_txt():
    file = {'upfile': ('test.txt', open('resources/test.txt','rb'), 'text/plain')}
    response = client.post("/api/fileanalyse", files=file)
    assert response.status_code == 200
    assert response.json() == {'name': 'test.txt', 'size': '186', 'type': 'text/plain'}

def test_fileanalyse_json():
    file = {'upfile': ('test.json', open('resources/test.json','rb'), 'application/json')}
    response = client.post("/api/fileanalyse", files=file)
    assert response.status_code == 200
    assert response.json() == {'name': 'test.json', 'size': '218', 'type': 'application/json'}

def test_fileanalyse_img():
    file = {'upfile': ('test.png', open('resources/test.png','rb'), 'image/png')}
    response = client.post("/api/fileanalyse", files=file)
    assert response.status_code == 200
    assert response.json() == {'name': 'test.png', 'size': '13907', 'type': 'image/png'}
