import pytest
import requests

import data
import helpers


@pytest.fixture()
def register_new_courier():

    # генерируем рандомные данные и отправляем запрос на регистарцию
    payload = helpers.generate_new_courier_data()
    response = requests.post(f'{data.SCOOTER_URL}/{data.REGISTRATION_ENDPOINT}', json=payload)
    yield response

    helpers.delete_courier(payload)  # удаляем тетстовые данные


@pytest.fixture()
def login_new_courier():

    new_user = helpers.register_new_courier_and_return_login_password()  # получаем список из логина, пароля и имени
    payload = {
        "login": new_user[0],  # 0 - индекс логина в списке new_user
        "password": new_user[1]  # 1 - индекс пароля в списке new_user
    }
    response = requests.post(f'{data.SCOOTER_URL}/{data.LOGIN_ENDPOINT}', json=payload)
    yield response

    helpers.delete_courier(payload)
