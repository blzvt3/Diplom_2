import requests
import allure
import urls
from data import Data

class TestCreateOrder:
    @allure.title('Проверка создания заказа с ингредиентами - неавторизованный пользователь')
    def test_create_order_with_ingredients_unauthorized_user(self):
        payload = {"ingredients": [Data.ingredient_1_id, Data.ingredient_2_id]}
        response = requests.post(urls.BASE_URL + urls.ORDER_ENDPOINT, json=payload)

        assert response.status_code == 200
        data = response.json()
        assert data["success"] is True
        assert data["name"] == Data.order_name
        assert "order" in data and isinstance(data["order"]["number"], int)

    @allure.title('Проверка создания заказа без ингредиентов - неавторизованный пользователь')
    def test_create_order_no_ingredients_unauthorized_user(self):
        payload = {}
        response = requests.post(urls.BASE_URL + urls.ORDER_ENDPOINT, json=payload)

        assert response.status_code == 400
        data = response.json()
        assert data["success"] is False
        assert data["message"] == Data.ingredients_error

    @allure.title('Проверка создания заказа с неверным хешем ингредиентов - неавторизованный пользователь')
    def test_create_order_wrong_hash_ingredients_unauthorized_user(self):
        payload = {"ingredients": ["1", ""]}
        response = requests.post(urls.BASE_URL + urls.ORDER_ENDPOINT, json=payload)

        assert response.status_code == 500
        assert "Internal Server Error" in response.text

    @allure.title('Проверка создания заказа с ингредиентами - авторизованный пользователь')
    def test_create_order_with_ingredients_authorized_user(self, create_and_delete_user):
        email, _, name, _, access_token = create_and_delete_user
        payload = {"ingredients": [Data.ingredient_1_id, Data.ingredient_2_id]}
        response_order = requests.post(urls.BASE_URL + urls.ORDER_ENDPOINT, json=payload, headers=access_token)

        assert response_order.status_code == 200
        data = response_order.json()
        assert data["success"] is True
        assert data["name"] == Data.order_name

        order = data["order"]
        ingredients = order["ingredients"]
        assert len(ingredients) == 2
        assert ingredients[0] == Data.ingredient_1
        assert ingredients[1] == Data.ingredient_2

        assert isinstance(order["_id"], str)

        owner = order["owner"]
        assert owner["name"] == name
        assert owner["email"] == email
        assert isinstance(owner["createdAt"], str)
        assert isinstance(owner["updatedAt"], str)

        assert order["status"] == "done"
        assert order["name"] == Data.order_name
        assert isinstance(order["number"], int) and order["number"] > 0
        assert isinstance(order["price"], int) and order["price"] > 0
        assert isinstance(order["createdAt"], str)
        assert isinstance(order["updatedAt"], str)

    @allure.title('Проверка создания заказа без ингредиентов - авторизованный пользователь')
    def test_create_order_no_ingredients_authorized_user(self, create_and_delete_user):
        _, _, _, _, access_token = create_and_delete_user
        payload = {}
        response = requests.post(urls.BASE_URL + urls.ORDER_ENDPOINT, json=payload, headers=access_token)

        assert response.status_code == 400
        data = response.json()
        assert data["success"] is False
        assert data["message"] == Data.ingredients_error
        
    @allure.title('Проверка создания заказа с неверным хешем ингредиентов - авторизованный пользователь')
    def test_create_order_wrong_hash_ingredients_authorized_user(self, create_and_delete_user):
        _, _, _, _, access_token = create_and_delete_user
        payload = {"ingredients": ["1", ""]}
        response = requests.post(urls.BASE_URL + urls.ORDER_ENDPOINT, json=payload, headers=access_token)

        assert response.status_code == 500
        assert "Internal Server Error" in response.text

    class TestGetOrders:
        @allure.title('Проверка получения списка заказов - неавторизованный пользователь')
        def test_get_orders_unauthorized_user(self):
            response = requests.get(urls.BASE_URL + urls.ORDER_ENDPOINT)

            assert response.status_code == 401
            data = response.json()
            assert data["success"] is False
            assert data["message"] == Data.get_orders_401_error

        @allure.title('Проверка получения списка заказов - авторизованный пользователь')
        def test_get_orders_authorized_user(self, create_and_delete_user):
            email, _, name, _, access_token = create_and_delete_user
            payload = {"ingredients": [Data.ingredient_1_id, Data.ingredient_2_id]}
            response_create_order = requests.post(urls.BASE_URL + urls.ORDER_ENDPOINT, json=payload, headers=access_token)

            assert response_create_order.status_code == 200
            data = response_create_order.json()
            assert data["success"] is True
            assert data["name"] == Data.order_name

            order = data["order"]
            ingredients = order["ingredients"]
            assert len(ingredients) == 2
            assert ingredients[0] == Data.ingredient_1
            assert ingredients[1] == Data.ingredient_2

            assert isinstance(order["_id"], str)

            owner = order["owner"]
            assert owner["name"] == name
            assert owner["email"] == email
            assert isinstance(owner["createdAt"], str)
            assert isinstance(owner["updatedAt"], str)

            assert order["status"] == "done"
            assert order["name"] == Data.order_name
            assert isinstance(order["number"], int) and order["number"] > 0
            assert isinstance(order["price"], int) and order["price"] > 0
            assert isinstance(order["createdAt"], str)
            assert isinstance(order["updatedAt"], str)

            response_get_order = requests.get(urls.BASE_URL + urls.ORDER_ENDPOINT, headers=access_token)

            assert response_get_order.status_code == 200
            data = response_get_order.json()
            assert data["success"] is True

            assert isinstance(data["orders"], list) and len(data["orders"]) == 1
            orders = data["orders"][0]
            assert "_id" in orders and isinstance(orders["_id"], str)
            assert orders["ingredients"] == [Data.ingredient_1_id, Data.ingredient_2_id]
            assert orders["status"] == "done"
            assert orders["name"] == Data.order_name
            assert isinstance(orders["createdAt"], str)
            assert isinstance(orders["updatedAt"], str)
            assert isinstance(orders["number"], int) and order["number"] > 0

            assert isinstance(data["total"], int) and data["total"] >= 0
            assert isinstance(data["totalToday"], int) and data["totalToday"] >= 0