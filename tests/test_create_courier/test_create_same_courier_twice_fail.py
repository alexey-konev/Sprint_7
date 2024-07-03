import allure
import pytest
import requests

import data
import helpers


class TestCreateSameCourierTwice:
    @allure.title("Проверка создания двух одинаковых курьеров")
    def test_create_same_courier_twice_fail(self):

        # генерируем рандомные данные и отправляем запрос на регистарцию
        payload = helpers.generate_new_courier_data()
        requests.post(f'{data.SCOOTER_URL}/api/v1/courier', json=payload)
        response = requests.post(f'{data.SCOOTER_URL}/api/v1/courier', json=payload)  # дублируем запрос на регистарцию

        assert response.status_code == 409 and response.text == data.LOGIN_EXISTS_MESSAGE

        helpers.delete_courier(payload)  # удаляем тестовые данные

