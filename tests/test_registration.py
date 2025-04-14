import requests
import allure
import urls
from data import Data
from helper import Generator

class TestRegistration:
    @allure.title('Проверка создания пользователя - заполнены все обязательные поля')
    def test_registration(self, create_and_delete_user):
        email, _, name, response_create_user, _ = create_and_delete_user

        assert response_create_user.status_code == 200
        data = response_create_user.json()
        assert data["success"] is True
        assert data["user"]["email"] == email
        assert data["user"]["name"] == name
        assert "accessToken" in data and data["accessToken"].startswith("Bearer ")
        assert "refreshToken" in data and len(data["refreshToken"]) > 0

    @allure.title('Проверка создания пользователя - не указан пароль')
    def test_registration_no_password(self):
        payload = {"email": Generator.fake_email(), "password": "", "name": Generator.fake_name()}
        response = requests.post(urls.BASE_URL + urls.REGISTRATION_ENDPOINT, json=payload)

        assert response.status_code == 403
        data = response.json()
        assert data["success"] is False
        assert data["message"] == Data.registration_data_403_error

    @allure.title('Проверка создания пользователя - указаны данные существующего пользователя')
    def test_registration_user_exists(self, create_and_delete_user):
        email, password, name, _, _ = create_and_delete_user

        payload = {"email": email, "password": password, "name": name}
        response = requests.post(urls.BASE_URL + urls.REGISTRATION_ENDPOINT, json=payload)

        assert response.status_code == 403
        data = response.json()
        assert data["success"] is False
        assert data["message"] == Data.registration_user_403_error