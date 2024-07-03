ORDER_INFO = {
            "firstName": "Naruto",
            "lastName": "Uchiha",
            "address": "Konoha, 142 apt.",
            "metroStation": 4,
            "phone": "+7 800 355 35 35",
            "rentTime": 5,
            "deliveryDate": "2020-06-06",
            "comment": "Saske, come back to Konoha",
            "color": ["BLACK"]
        }

SCOOTER_URL = 'https://qa-scooter.praktikum-services.ru'

OK_MESSAGE = '{"ok":true}'

MISSING_FILED_MESSAGE = '{"code":400,"message":"Недостаточно данных для создания учетной записи"}'
# body ошибок в документации не совпадает, должен быть без '"code":***'

LOGIN_EXISTS_MESSAGE = '{"code":409,"message":"Этот логин уже используется. Попробуйте другой."}'

INCORRECT_FIELD_MESSAGE = '{"code":404,"message":"Учетная запись не найдена"}'

EMPTY_FIELD_MESSAGE = '{"code":400,"message":"Недостаточно данных для входа"}'

ID_DOESNT_EXIST_MESSAGE = '{"code":404,"message":"Курьера с таким id нет."}'

NO_COUR_ID_ACCEPT_ORDER_MESSAGE = '{"code":400,"message":"Недостаточно данных для поиска"}'

WRONG_COUR_ID_ACCEPT_ORDER_MESSAGE = '{"code":404,"message":"Курьера с таким id не существует"}'

WRONG_ORDER_ID_ACCEPT_ORDER_MESSAGE = '{"code":404,"message":"Заказа с таким id не существует"}'

NO_TRACK_GET_ORDER_MESSAGE = '{"code":400,"message":"Недостаточно данных для поиска"}'

WRONG_TRACK_GET_ORDER_MESSAGE = '{"code":404,"message":"Заказ не найден"}'

