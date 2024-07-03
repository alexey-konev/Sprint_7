import pytest
import allure
import requests
import data, helpers


class TestDeleteCourier:
    @allure.title("Проверка успешного удаления курьера")
    def test_delete_courier_success(self):
        # создаем курьера не через фикстуру, тк в фикстуре происходит удаление курьера в конце
        new_user = helpers.register_new_courier_and_return_login_password()
        payload = {
            "login": new_user[0],  # 0 - индекс логина в списке new_user
            "password": new_user[1]  # 1 - индекс пароля в списке new_user
        }

        response_1 = requests.post(f'{data.SCOOTER_URL}/api/v1/courier/login', json=payload)
        r = response_1.json()
        cour_id = r['id']

        response_2 = requests.delete(f'{data.SCOOTER_URL}/api/v1/courier/{cour_id}')

        assert response_2.status_code == 200 and response_2.text == data.OK_MESSAGE

