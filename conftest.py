import requests
import urls
import pytest
from helper import Generator

@pytest.fixture
def create_and_delete_user():
    email = Generator.fake_email()
    password = Generator.fake_password()
    name = Generator.fake_name()

    payload = {"email": email, "password": password, "name": name}
    response_create_user = requests.post(urls.BASE_URL + urls.REGISTRATION_ENDPOINT, json=payload)
    if response_create_user.status_code != 200 or response_create_user.json()["success"] is not True:
        pytest.fail(f"Ошибка при создании пользователя: {response_create_user.status_code}, {response_create_user.text}")

    access_token = {"Authorization": response_create_user.json()["accessToken"]}

    yield email, password, name, response_create_user, access_token

    response_delete_user = requests.delete(urls.BASE_URL + urls.USER_ENDPOINT, headers=access_token)
    if response_delete_user.status_code != 202 or response_delete_user.json()["success"] is not True:
        pytest.fail(f"Ошибка при удалении пользователя: {response_delete_user.status_code}, {response_delete_user.text}")
