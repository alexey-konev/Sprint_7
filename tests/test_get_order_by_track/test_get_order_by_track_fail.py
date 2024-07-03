import pytest
import allure
import requests
import json
import data


class TestAcceptOrderByTrackFail:
    @allure.title("Проверка ошибки получения заказа из-за отсутсвия его номера")
    def test_get_order_without_track_fail(self):

        response = requests.get(f'{data.SCOOTER_URL}/api/v1/orders/track')

        assert response.status_code == 400 and response.text == data.NO_TRACK_GET_ORDER_MESSAGE

    @allure.title("Проверка ошибки получения заказа из-за неправильного номера")
    def test_get_order_by_track_success(self):

        payload = data.ORDER_INFO
        response_1 = requests.post(f'{data.SCOOTER_URL}/api/v1/orders', json=payload)
        r = response_1.json()
        order_id = f'100{r['track']}'  # получили id заказа, добавили 100

        response_2 = requests.get(f'{data.SCOOTER_URL}/api/v1/orders/track?t={order_id}')
        r = response_2.json()

        assert response_2.status_code == 404 and response_2.text == data.WRONG_TRACK_GET_ORDER_MESSAGE
