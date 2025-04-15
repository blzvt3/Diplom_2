## Дипломный проект. Задание 2: API-тесты

### Автотесты для проверки программы, которая помогает заказать бургер в Stellar Burgers

### Реализованные сценарии

Созданы API-тесты, покрывающие эндпоинты: создание пользователя, изменение данных пользователя, создание заказа, получение заказов конкретного пользователя

### Структура проекта

- `tests` - пакет, содержащий тесты, разделенные по эндпоинтам. Например, `test_registration.py`, `test_login.py` и т.д.
- `allure_results` - пакет, содержащий json файлы отчета о тестировании

### Запуск автотестов

**Установка зависимостей**

> `$ pip install -r requirements.txt`

**Запуск автотестов и создание HTML-отчёта о тестировании**

> `$ pytest --alluredir=allure_results`
> `$ allure serve allure_results`