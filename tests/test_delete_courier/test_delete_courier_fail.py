import pytest
import allure
import requests
import data


class TestDeleteCourierFail:
    @allure.title("Проверка удаления курьера без передачи id")
    def test_delete_courier_without_id(self):

        response = requests.delete(f'{data.SCOOTER_URL}/api/v1/courier/')

        assert response.status_code == 404 and response.text == '{"code":404,"message":"Not Found."}'
        # по документации должа быть ошибка 400 "Недостаточно данных для удаления курьера"

    @allure.title("Проверка удаления курьера с несуществующим id")
    def test_delete_courier_with_wrong_id(self):

        response = requests.delete(f'{data.SCOOTER_URL}/api/v1/courier/007')

        assert response.status_code == 404 and response.text == data.ID_DOESNT_EXIST_MESSAGE
