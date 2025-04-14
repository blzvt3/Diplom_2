import requests
import allure
import urls
from data import Data
from helper import Generator

class TestEditUserData:
    @allure.title('Проверка изменения данных - авторизованный пользователь')
    def test_edit_data_authorized_user(self, create_and_delete_user):
        _, _, _, _, access_token = create_and_delete_user

        new_email = Generator.fake_email()
        new_name = Generator.fake_name()
        payload = {"email": new_email, "name": new_name}
        response = requests.patch(urls.BASE_URL + urls.USER_ENDPOINT, json=payload, headers=access_token)

        assert response.status_code == 200
        data = response.json()
        assert data["success"] is True
        assert data["user"]["email"] == new_email
        assert data["user"]["name"] == new_name

    @allure.title('Проверка изменения данных - неавторизованный пользователь')
    def test_edit_data_unauthorized_user(self):
        payload = {"email": Generator.fake_email(), "name": Generator.fake_name()}
        response = requests.patch(urls.BASE_URL + urls.USER_ENDPOINT, json=payload)

        assert response.status_code == 401
        data = response.json()
        assert data["success"] is False
        assert data["message"] == Data.edit_data_401_error