class Data:
    registration_data_403_error = "Email, password and name are required fields"
    registration_user_403_error = "User already exists"
    login_403_error = "email or password are incorrect"
    edit_data_401_error = "You should be authorised"
    ingredients_error = "Ingredient ids must be provided"
    get_orders_401_error = "You should be authorised"
    order_name = "Spicy флюоресцентный бургер"
    ingredient_1_id = "61c0c5a71d1f82001bdaaa72"
    ingredient_2_id = "61c0c5a71d1f82001bdaaa6d"

    ingredient_1 = {
        "_id": "61c0c5a71d1f82001bdaaa72",
        "name": "Соус Spicy-X",
        "type": "sauce",
        "proteins": 30,
        "fat": 20,
        "carbohydrates": 40,
        "calories": 30,
        "price": 90,
        "image": "https://code.s3.yandex.net/react/code/sauce-02.png",
        "image_mobile": "https://code.s3.yandex.net/react/code/sauce-02-mobile.png",
        "image_large": "https://code.s3.yandex.net/react/code/sauce-02-large.png",
        "__v": 0
    }

    ingredient_2 = {
        "_id": "61c0c5a71d1f82001bdaaa6d",
        "name": "Флюоресцентная булка R2-D3",
        "type": "bun",
        "proteins": 44,
        "fat": 26,
        "carbohydrates": 85,
        "calories": 643,
        "price": 988,
        "image": "https://code.s3.yandex.net/react/code/bun-01.png",
        "image_mobile": "https://code.s3.yandex.net/react/code/bun-01-mobile.png",
        "image_large": "https://code.s3.yandex.net/react/code/bun-01-large.png",
        "__v": 0
    }