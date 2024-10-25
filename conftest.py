import pytest
import requests
import src.data
import src.helpers

@pytest.fixture(scope='function')
def get_user_token():
    user_data = src.helpers.create_user_and_collect_user_data()
    email = user_data['email']
    password = user_data['password']
    name = user_data['name']
    payload = {
        'email': email,
        'password': password,
        'name': name
    }
    response = requests.post(src.data.LOGIN_USER_URL, data=payload)
    token = response.json().get('accessToken')
    
    yield token
    src.helpers.delete_user(token)