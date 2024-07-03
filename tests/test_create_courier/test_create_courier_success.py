import pytest
import allure
import requests
import data


class TestCreateCourier:
    @allure.title("Проверка регистрации курьера")
    def test_create_courier_success(self, register_new_courier):
        #через фикстуру генерируем данные и отправляем запрос на регистрацию
        response = register_new_courier  # записываем ответ в response

        assert response.status_code == 201 and response.text == data.OK_MESSAGE
        # после asserta удаляются тестовые данные


