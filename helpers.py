import json
import allure
import requests
import random
import string
import data


@allure.step('Генерируем строку из букв нижнего регистра указанной длины')
def generate_random_string(length):
    letters = string.ascii_lowercase
    random_string = ''.join(random.choice(letters) for i in range(length))
    return random_string


@allure.step('Генерируем логин, пароль и имя курьера')
def generate_new_courier_data():

    # генерируем логин, пароль и имя курьера
    login = generate_random_string(10)
    password = generate_random_string(10)
    first_name = generate_random_string(10)

    # собираем тело запроса
    payload = {
        "login": login,
        "password": password,
        "firstName": first_name
    }

    return payload


# метод регистрации нового курьера возвращает список из логина и пароля
# если регистрация не удалась, возвращает пустой список
@allure.step('Регистрируем сгенерированного курьера')
def register_new_courier_and_return_login_password():

    # создаём список, чтобы метод мог его вернуть
    login_pass = []

    payload = generate_new_courier_data()
    # отправляем запрос на регистрацию курьера и сохраняем ответ в переменную response
    response = requests.post(f'{data.SCOOTER_URL}/{data.REGISTRATION_ENDPOINT}', json=payload)

    # если регистрация прошла успешно (код ответа 201), добавляем в список логин и пароль курьера
    if response.status_code == 201:
        login_pass.append(payload['login'])
        login_pass.append(payload['password'])
        login_pass.append(payload['firstName'])

    # возвращаем список
    return login_pass

@allure.step('Удаляем сгенерированного тестового курьера')
def delete_courier(courier_data):

    payload = {
        "login": courier_data["login"],
        "password": courier_data["password"]
    }
    response = requests.post(f'{data.SCOOTER_URL}/{data.LOGIN_ENDPOINT}', json=payload)
    r = response.json()
    created_id = r["id"]
    response = requests.delete(f'{data.SCOOTER_URL}/{data.DELETE_ENDPOINT}/{created_id}')
    return response

