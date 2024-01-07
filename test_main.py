from fastapi.testclient import TestClient
from main import app

client = TestClient(app)



def test_publish():
    response = client.post('/', json={'id':0,'media_url':'http://www.testing.com','caption':'my test post'})
    assert response.status_code == 201
    assert response.json() == {
        'message':'data recieved'
    }

