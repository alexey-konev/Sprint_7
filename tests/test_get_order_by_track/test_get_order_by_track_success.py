import pytest
import allure
import requests
import json
import data


class TestAcceptOrderByTrack:
    @allure.title("Проверка успешного получения заказа о его номеру")
    def test_get_order_by_track_success(self):

        payload = data.ORDER_INFO
        response_1 = requests.post(f'{data.SCOOTER_URL}/{data.ORDERS_ENDPOINT}', json=payload)
        r = response_1.json()
        order_id = r['track']  # получили id заказа

        response_2 = requests.get(f'{data.SCOOTER_URL}/{data.ORDER_TRACK_ENDPOINT}?t={order_id}')
        r = response_2.json()

        assert response_2.status_code == 200 and r['order']

