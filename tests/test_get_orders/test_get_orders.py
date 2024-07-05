import pytest
import allure
import requests
import json
import data


class TestGetOrders:

    @allure.title('Проверка получения списка заказов')
    def test_get_orders(self):
        response = requests.get(f'{data.SCOOTER_URL}/{data.ORDERS_ENDPOINT}?limit=5')
        r = response.json()

        assert response.status_code == 200 and r['orders']

