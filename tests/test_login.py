import requests
import allure
import urls
from data import Data

class TestLogin:
    @allure.title('Проверка авторизации под существующим пользователем')
    def test_login(self, create_and_delete_user):
        email, password, name, _, _ = create_and_delete_user

        payload = {"email": email, "password": password}
        response = requests.post(urls.BASE_URL + urls.LOGIN_ENDPOINT, json=payload)

        assert response.status_code == 200
        data = response.json()
        assert data["success"] is True
        assert data["user"]["email"] == email
        assert data["user"]["name"] == name
        assert "accessToken" in data and data["accessToken"].startswith("Bearer ")
        assert "refreshToken" in data and len(data["refreshToken"]) > 0

    @allure.title('Проверка авторизации - неправильно указан пароль')
    def test_login_wrong_password(self, create_and_delete_user):
        email, _, _, _, _ = create_and_delete_user

        payload = {"email": email, "password": "1"}
        response = requests.post(urls.BASE_URL + urls.LOGIN_ENDPOINT, json=payload)

        assert response.status_code == 401
        data = response.json()
        assert data["success"] is False
        assert data["message"] == Data.login_403_error

    @allure.title('Проверка авторизации - неправильно указан email')
    def test_login_wrong_email(self, create_and_delete_user):
        _, password,_, _, _ = create_and_delete_user

        payload = {"email": "1", "password": password}
        response = requests.post(urls.BASE_URL + urls.LOGIN_ENDPOINT, json=payload)

        assert response.status_code == 401
        data = response.json()
        assert data["success"] is False
        assert data["message"] == Data.login_403_error