from hillel_api import API
import requests

s = requests.session()


def test_signup_positive():

    user_data = {
        "name": "John",
        "lastName": "Dou",
        "email": "qam0404@2022test.com",
        "password": "Qam2608venv",
        "repeatPassword": "Qam2608venv"
    }
    r = API.auth.signup(s, user_data)
    r_json = r.json()
    assert r.status_code == 201, "Wrong status code"
    assert r_json["status"] == "ok", "Key 'status' is not ok"


def test_signin_positive():

    user_data = {
        "email": "qam0404@2022test.com",
        "password": "Qam2608venv",
        "remember": False
    }
    r = API.auth.signin(s, user_data)
    r_json = r.json()
    assert r.status_code == 200, "Wrong status code"
    assert r_json["status"] == "ok", "Key 'status' is not ok"


def test_signin_negative():

    user_data_negative = {
        "email": "qam@2022test.com",
        "password": "Qam2",
        "remember": False
    }
    r = API.auth.signin(s, user_data_negative)
    r_json = r.json()
    assert r.status_code == 400, "Wrong status code"
    assert r_json["status"] == "error", "Key 'status' is not error"


def test_logout():

    r = API.auth.logout(s)
    r_json = r.json()
    assert r.status_code == 200, "Wrong status code"
    assert r_json["status"] == "ok", "Key 'status' is not ok"

def test_create_car():

    user_data_signin = {
        "email": "qam0404@2022test.com",
        "password": "Qam2608venv",
        "remember": False
    }
    API.auth.signin(s, user_data_signin)

    user_data_create_car = {
      "carBrandId": 1,
      "carModelId": 1,
      "mileage": 122
    }
    r = API.cars.cars_post(s, user_data_create_car)
    r_json = r.json()
    assert r.status_code == 201, "Wrong status code"
    assert r_json["status"] == "ok", "Key 'status' is not ok"

def test_edit_car():

    user_data_signin = {
        "email": "qam0404@2022test.com",
        "password": "Qam2608venv",
        "remember": False
    }
    API.auth.signin(s, user_data_signin)

    user_data_create_car = {
      "carBrandId": 1,
      "carModelId": 1,
      "mileage": 122
    }
    create_car = API.cars.cars_post(s, user_data_create_car)
    create_car_json = create_car.json()

    id_for_edit = create_car_json['data']['id']

    user_data_edit_car = {
        "carBrandId": 2,
        "carModelId": 2,
        "mileage": 168223
    }
    edit_car = API.cars.cars_id_put(s, {**user_data_edit_car, "id": id_for_edit})
    edit_car_json = edit_car.json()

    assert edit_car.status_code == 200
    assert edit_car_json["status"] == "ok", "Key 'status' is not ok"
    assert edit_car_json["data"]['mileage'] == user_data_edit_car['mileage']
def test_get_car_by_id():

    user_data_signin = {
        "email": "qam0404@2022test.com",
        "password": "Qam2608venv",
        "remember": False
    }
    API.auth.signin(s, user_data_signin)

    user_data_create_car = {
      "carBrandId": 1,
      "carModelId": 1,
      "mileage": 122
    }
    create_car = API.cars.cars_post(s, user_data_create_car)
    create_car_json = create_car.json()

    get_car_response = API.cars.cars_id_get(s, request_body=create_car_json)
    get_car_response_json = get_car_response.json()

    assert get_car_response.status_code == 200
    assert get_car_response_json["status"] == "ok", "Key 'status' is not ok"
    assert get_car_response_json["data"]['mileage'] == user_data_create_car['mileage']
def test_signin_delete_and_cant_resign():
    """E2E test example"""
    user_data = {
        "email": "qam0404@2022test.com",
        "password": "Qam2608venv",
        "remember": False
    }
    r = API.auth.signin(s, user_data)
    r_json = r.json()
    assert r.status_code == 200, "Wrong status code"
    assert r_json["status"] == "ok", "Key 'status' is not ok"
    # delete user
    r = API.users.users(s)
    r_json = r.json()
    assert r.status_code == 200, "Wrong status code"
    assert r_json["status"] == "ok", "Key 'status' is not ok"
    # cant login
    r = API.auth.signin(s, user_data)
    r_json = r.json()
    assert r.status_code == 400, "Wrong status code"
    assert r_json["status"] == "error", "Key 'error' expected"
