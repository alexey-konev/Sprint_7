import pytest
import allure
import requests
import helpers, data


class TestLoginCourierFail:

    @allure.title("Проверка авторизации курьера c неправильным логином")
    def test_login_with_incorrect_login(self):

        new_user = helpers.register_new_courier_and_return_login_password()  # получаем список из логина, пароля и имени

        payload = {
            "login": f'{new_user[0]}1',  # логин с опечаткой
            "password": new_user[1]  # правильный пароль
        }
        response = requests.post(f'{data.SCOOTER_URL}/api/v1/courier/login', json=payload)

        assert response.status_code == 404 and response.text == data.INCORRECT_FIELD_MESSAGE

        payload = {
            "login": new_user[0],
            "password": new_user[1]
        }

        helpers.delete_courier(payload)


    @allure.title("Проверка авторизации курьера c неправильным паролем")
    def test_login_with_incorrect_password(self):

        new_user = helpers.register_new_courier_and_return_login_password()

        payload = {
            "login": new_user[0],  # правильный логин
            "password": f'{new_user[1]}1'  # пароль с опечаткой
        }
        response = requests.post(f'{data.SCOOTER_URL}/api/v1/courier/login', json=payload)

        assert response.status_code == 404 and response.text == data.INCORRECT_FIELD_MESSAGE

        payload = {
            "login": new_user[0],
            "password": new_user[1]
        }

        helpers.delete_courier(payload)

    @allure.title("Проверка авторизации курьера c пустым логином")
    def test_login_with_empty_login(self):
        new_user = helpers.register_new_courier_and_return_login_password()

        payload = {
            "login": "",
            "password": new_user[1]
        }
        response = requests.post(f'{data.SCOOTER_URL}/api/v1/courier/login', json=payload)

        assert response.status_code == 400 and response.text == data.EMPTY_FIELD_MESSAGE

        payload = {
            "login": new_user[0],
            "password": new_user[1]
        }

        helpers.delete_courier(payload)

    @allure.title("Проверка авторизации курьера c пустым паролем")
    def test_login_with_empty_password(self):
        new_user = helpers.register_new_courier_and_return_login_password()

        payload = {
            "login": new_user[0],
            "password": ""
        }
        response = requests.post(f'{data.SCOOTER_URL}/api/v1/courier/login', json=payload)

        assert response.status_code == 400 and response.text == data.EMPTY_FIELD_MESSAGE

        payload = {
            "login": new_user[0],
            "password": new_user[1]
        }

        helpers.delete_courier(payload)


    @allure.title("Проверка авторизации курьера, не передавая логин")
    def test_login_with_no_login(self):
        new_user = helpers.register_new_courier_and_return_login_password()

        payload = {
            "password": new_user[1]
        }
        response = requests.post(f'{data.SCOOTER_URL}/api/v1/courier/login', json=payload)

        assert response.status_code == 400 and response.text == data.EMPTY_FIELD_MESSAGE

        payload = {
            "login": new_user[0],
            "password": new_user[1]
        }

        helpers.delete_courier(payload)

    @allure.title("Проверка авторизации курьера,не передавая пароль")
    def test_login_with_no_password(self):
        new_user = helpers.register_new_courier_and_return_login_password()

        payload = {
            "login": new_user[0]
        }
        response = requests.post(f'{data.SCOOTER_URL}/api/v1/courier/login', json=payload)

        # без пароля выдает ошибку 504 (?)  в постмане так же
        assert response.status_code == 504

        payload = {
            "login": new_user[0],
            "password": new_user[1]
        }

        helpers.delete_courier(payload)

