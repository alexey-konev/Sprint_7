import pytest
import allure
import requests
import json
import data


class TestCreateOrder:
    @allure.title("Проверка создания заказа с разными цветами")
    @pytest.mark.parametrize('color',
                            [
                                [''],
                                ['BLACK'],
                                ['GREY'],
                                ['BLACK', 'GREY']
                            ])
    def test_create_order_different_colours(self, color):

        payload = data.ORDER_INFO
        payload["color"] = color

        response = requests.post(f'{data.SCOOTER_URL}/{data.ORDERS_ENDPOINT}', json=payload)
        r = response.json()

        assert response.status_code == 201 and r['track']

        