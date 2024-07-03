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

        payload = {
            "firstName": "Naruto",
            "lastName": "Uchiha",
            "address": "Konoha, 142 apt.",
            "metroStation": 4,
            "phone": "+7 800 355 35 35",
            "rentTime": 5,
            "deliveryDate": "2020-06-06",
            "comment": "Saske, come back to Konoha",
            "color": color
        }

        response = requests.post(f'{data.SCOOTER_URL}/api/v1/orders', json=payload)
        r = response.json()

        assert response.status_code == 201 and r['track']

        