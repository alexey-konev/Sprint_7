import pytest
import allure
import requests
import json
import data


class TestAcceptOrderSuccess:
    @allure.title("Проверка успешного принятия заказа")
    def test_accept_order_success(self,login_new_courier ):

        response_1 = login_new_courier
        r = response_1.json()
        cour_id = r['id']  # получили id курьера

        payload_2 = data.ORDER_INFO
        response_2 = requests.post(f'{data.SCOOTER_URL}/{data.ORDERS_ENDPOINT}', json=payload_2)
        r_2 = response_2.json()
        order_id = r_2['track']  # получили id заказа

        response_3 = requests.put(f'{data.SCOOTER_URL}/{data.ACCEPT_ORDER_ENDPOINT}/{order_id}?courierId={cour_id}')

        assert response_3.status_code == 200 and response_3.text == data.OK_MESSAGE

#тест падает с ошибкой 404, иногда 409, а иногда проходит - в чем причина не могу понять
