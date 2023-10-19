import data
import configuration
import stand_request

#Заголовки для создания пользователя
def get_user_headers():
    create_user_headers = data.headers.copy()
    create_user_headers.pop("Authorization") #для создания пользователя убираем ключ Authorization
    return create_user_headers

#Передача данных/параметров в функцию-запрос на создание пользователя
def get_user_token_by_creating_user():
    response = stand_request.post_new(data.user_body, get_user_headers(), configuration.CREATE_USER_PATH)
    return response

#Получение токена авторизации (парсинг ответа на запрос создания пользователя)
def create_user_token():
    return "Bearer " + get_user_token_by_creating_user().json()["authToken"] #возвращает токен (строка)

#Добавление токена авторизации в заголовки (для создания набора)
def get_kit_headers():
    kit_headers_with_authorization = data.headers.copy()
    kit_headers_with_authorization["Authorization"] = create_user_token()
    #print(f'token finale: {kit_headers_with_authorization["Authorization"]}')
    return kit_headers_with_authorization

#Передача тестовых данных в качестве значения для ключа name (для создания набора)
def get_kit_body(name):
    new_kit_body = data.kit_body.copy()
    new_kit_body["name"] = name
    return new_kit_body

#Создание набора и проверки (успешное создание набора)
def possitive_assert(current_name):
    response = stand_request.post_new(get_kit_body(current_name), current_headers_for_new_kit, configuration.CREATE_KIT_PATH)
    print(f'code: {response.status_code}, body_kit_name: {response.json()["name"]}')
    assert response.status_code == 201
    assert response.json()["name"] == current_name

#Создание набора и проверки (НЕуспешное создание набора)
def negative_assert_code_400(current_name):
    response = stand_request.post_new(get_kit_body(current_name), current_headers_for_new_kit, configuration.CREATE_KIT_PATH)
    print(f'code: {response.status_code}, body_kit_name: {response.json()["name"]}')
    assert response.status_code == 400

#Создание набора в случае отсутствия обязательного параметра name
def negative_assert_no_first_name():
    body = data.kit_body.copy()
    body.pop("name")
    response = stand_request.post_new(body, current_headers_for_new_kit, configuration.CREATE_KIT_PATH)
    print(f'code: {response.status_code}, body_kit_name: {response.json()}')
    assert response.status_code == 400

#Переменная, которая хранит словарь headers с заполненным токеном авторизации пользователя - для создания набора
current_headers_for_new_kit = get_kit_headers()
