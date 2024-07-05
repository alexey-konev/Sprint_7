import pytest
import allure
import requests
import json
import data


class TestAcceptOrderFail:
    @allure.title("Проверка ошибки принятия заказа без id курьера")
    def test_accept_order_without_courier_id(self):

        payload = data.ORDER_INFO
        response_2 = requests.post(f'{data.SCOOTER_URL}/{data.ORDERS_ENDPOINT}', json=payload)
        r = response_2.json()
        order_id = r['track']  # получили id заказа

        response_3 = requests.put(f'{data.SCOOTER_URL}/{data.ACCEPT_ORDER_ENDPOINT}/{order_id}')

        assert response_3.status_code == 400 and response_3.text == data.NO_COUR_ID_ACCEPT_ORDER_MESSAGE


    @allure.title("Проверка ошибки принятия заказа из-за несуществующего id курьера")
    def test_accept_order_wrong_courier_id(self, login_new_courier):

        response_1 = login_new_courier
        r = response_1.json()
        cour_id = f'1000{r['id']}'  # получили id курьера, добавили 1000 в начале

        payload = data.ORDER_INFO
        response_2 = requests.post(f'{data.SCOOTER_URL}/{data.ORDERS_ENDPOINT}', json=payload)
        r = response_2.json()
        order_id = r['track']  # получили id заказа

        response_3 = requests.put(f'{data.SCOOTER_URL}/{data.ACCEPT_ORDER_ENDPOINT}/{order_id}?courierId={cour_id}')

        assert response_3.status_code == 404 and response_3.text == data.WRONG_COUR_ID_ACCEPT_ORDER_MESSAGE

    @allure.title("Проверка ошибки принятия заказа без id заказа")
    def test_accept_order_without_order_id(self, login_new_courier):
        response_1 = login_new_courier
        r = response_1.json()
        cour_id = r['id']  # получили id курьера
        
        response_3 = requests.put(f'{data.SCOOTER_URL}/{data.ACCEPT_ORDER_ENDPOINT}/courierId={cour_id}')

        assert response_3.status_code == 400 and response_3.text == data.NO_COUR_ID_ACCEPT_ORDER_MESSAGE

    @allure.title("Проверка ошибки принятия заказа из-за несуществующего id заказа")
    def test_accept_order_wrong_order_id(self, login_new_courier):
        response_1 = login_new_courier
        r = response_1.json()
        cour_id = r['id']  # получили id курьера, добавили 1000 в начале

        payload = data.ORDER_INFO
        response_2 = requests.post(f'{data.SCOOTER_URL}/{data.ORDERS_ENDPOINT}', json=payload)
        r = response_2.json()
        order_id = f'100{r['track']}'  # получили id заказа, обавили 100

        response_3 = requests.put(f'{data.SCOOTER_URL}/{data.ACCEPT_ORDER_ENDPOINT}/{order_id}?courierId={cour_id}')

        assert response_3.status_code == 404 and response_3.text == data.WRONG_ORDER_ID_ACCEPT_ORDER_MESSAGE

