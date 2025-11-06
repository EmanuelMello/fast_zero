from http import HTTPStatus

from fastapi.testclient import TestClient

from fast_zero.app import app
from fast_zero.schemas import Message


def test_read_root_and_return_hello_world():
    client = TestClient(app)  # arrange
    response = client.get('/')  # act
    assert response.status_code == HTTPStatus.OK  # assert
    assert response.json() == {'message': 'Hello World'}  # assert


def test_hello_world_and_return_message():
    client = TestClient(app)
    response = client.post('/hello_world')
    assert response.status_code == HTTPStatus.OK
    assert response.json() == Message(message='Hello World')
