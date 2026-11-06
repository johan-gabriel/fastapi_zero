from http import HTTPStatus

from fastapi.testclient import TestClient

from fastapi_zero.app import app

client = TestClient(app)


def test_root_should_return_hello_world():
    """
    Esse teste tem 3 etapas (AAA):
    - A: Arrange - Arranja o cenário de teste.
    - A: Act - Executa a ação que queremos testar.(SUT - System Under Test)
    - A: Assert - Verifica se o resultado da ação é o esperado.
    """
    # arrange
    client = TestClient(app)
    # act
    response = client.get('/')
    # assert
    assert response.json() == {'message': 'Hello World'}
    assert response.status_code == HTTPStatus.OK
