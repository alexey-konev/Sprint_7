import pytest
import allure
import requests
import data, helpers


class TestCreateCourier:
    @allure.title("Проверка регистрации курьера")
    def test_create_courier_success(self, register_new_courier):
        # через фикстуру генерируем данные и отправляем запрос на регистрацию
        response = register_new_courier  # записываем ответ в response

        assert response.status_code == 201 and response.text == data.OK_MESSAGE
        # после asserta удаляются тестовые данные

    @allure.title("Проверка регистрации курьера без логина или пароля")
    @pytest.mark.parametrize('field', ['login', 'password'])
    def test_create_courier_without_field_fail(self, field):
        # по документации непонятно, является ли имя обязательным,
        # в postman можно отправить запрос без имени
        payload = helpers.generate_new_courier_data()
        payload.pop(field)
        response = requests.post(f'{data.SCOOTER_URL}/{data.REGISTRATION_ENDPOINT}', json=payload)

        assert response.status_code == 400 and response.text == data.MISSING_FILED_MESSAGE

    @allure.title("Проверка создания двух одинаковых курьеров")
    def test_create_same_courier_twice_fail(self):

        # генерируем рандомные данные и отправляем запрос на регистарцию
        payload = helpers.generate_new_courier_data()
        requests.post(f'{data.SCOOTER_URL}/{data.REGISTRATION_ENDPOINT}', json=payload)
        response = requests.post(f'{data.SCOOTER_URL}/{data.REGISTRATION_ENDPOINT}', json=payload)  # дублируем запрос на регистарцию

        assert response.status_code == 409 and response.text == data.LOGIN_EXISTS_MESSAGE

        helpers.delete_courier(payload)  # удаляем тестовые данные

