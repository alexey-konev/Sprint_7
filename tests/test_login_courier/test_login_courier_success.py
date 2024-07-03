import pytest
import allure
import requests
import json


class TestLoginCourier:
    @allure.title("Проверка авторизации курьера")
    def test_login_courier_success(self, login_new_courier):

        #через фикстуру регистрируем курьера и отправляем запрос на авторизацию
        response = login_new_courier  # записываем ответ в response
        r = response.json()

        assert response.status_code == 200 and r['id']
        # после asserta удаляются тестовые данные
