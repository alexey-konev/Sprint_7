import allure
import pytest
import requests, json

import data
import helpers


class TestCreateCourierWithoutRequiredField:
    # по документации непонятно, является ли имя обязательным,
    # в postman можно отправить запрос без имени
    @allure.title("Проверка регистрации курьера без логина или пароля")
    @pytest.mark.parametrize('field', ['login', 'password'])
    def test_create_courier_without_name_fail(self, field):

        payload = helpers.generate_new_courier_data()
        payload.pop(field)
        response = requests.post(f'{data.SCOOTER_URL}/api/v1/courier', json=payload)

        assert response.status_code == 400 and response.text == data.MISSING_FILED_MESSAGE
