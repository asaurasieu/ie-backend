from iebank_api import app
import pytest

def test_get_accounts(testing_client):
    """
    GIVEN a Flask application
    WHEN the '/accounts' page is requested (GET)
    THEN check the response is valid
    """
    response = testing_client.get('/accounts')
    assert response.status_code == 200

def test_dummy_wrong_path():
    """
    GIVEN a Flask application
    WHEN the '/wrong_path' page is requested (GET)
    THEN check the response is valid
    """
    with app.test_client() as client:
        response = client.get('/wrong_path')
        assert response.status_code == 404

def test_server_running(testing_client):
    """
    GIVEN a Flask application
    WHEN the '/' page is requested (GET)
    THEN check the response is valid
    """
    response = testing_client.get('/')
    assert response.status_code == 200

def test_delete_account(testing_client):
    """
    GIVEN a Flask application
    WHEN the '/accounts' page is deleted (DELETE)
    THEN check the response is valid
    """
    response = testing_client.delete('/accounts/1')
    assert response.status_code == 200

def test_update_account(testing_client):
    """
    GIVEN a Flask application
    WHEN the '/accounts/<id>' page is updated (PUT)
    THEN check the response is valid
    """
    response = testing_client.put('/accounts/1', json={'name': 'Jane Doe', 'currency': '$', 'country': 'USA'})
    assert response.status_code == 200
    

