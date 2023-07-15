import allure
import pytest
from helper import load_json_schema, reqres_session, reqres_responce


@allure.feature('API: other requests')
@allure.story('API: get unknown schema validate')
def test_unknown_json_schema_validate():
    response = reqres_session.get('api/unknown/')

    schema = load_json_schema('get_unknown.json')
    status = response.status_code
    response_json = reqres_responce.responce_json_get(response)

    reqres_responce.responce_status_chek(status, 200)
    if response_json != '':
        reqres_responce.responce_schema_validate(response_json, schema)

@allure.feature('API: other requests')
@allure.story('API: get single unknown schema validate')
def test_single_unknown_json_schema_validate():
    id = 2
    response = reqres_session.get(f'api/unknown/{id}')

    schema = load_json_schema('get_single_unknown.json')
    status = response.status_code
    response_json = reqres_responce.responce_json_get(response)

    reqres_responce.responce_status_chek(status, 200)
    if response_json != '':
        reqres_responce.responce_schema_validate(response_json, schema)


@allure.feature('API: other requests')
@allure.story('API: put user schema validate')
def test_user_put_update_json_schema_validate():
    id = 2
    payload = {"name": "morpheus", "job": "zion resident"}
    response = reqres_session.put(f'api/unknown/{id}', json=payload)

    schema = load_json_schema('put_user.json')
    status = response.status_code
    response_json = reqres_responce.responce_json_get(response)

    reqres_responce.responce_status_chek(status, 200)
    if response_json != '':
        reqres_responce.responce_schema_validate(response_json, schema)


@allure.feature('API: other requests')
@allure.story('API: patch user schema validate')
def test_user_patch_update_json_schema_validate():
    id = 2
    payload = {"name": "morpheus", "job": "zion resident"}
    response = reqres_session.patch(f'api/unknown/{id}', json=payload)

    schema = load_json_schema('patch_user.json')
    status = response.status_code
    response_json = reqres_responce.responce_json_get(response)

    reqres_responce.responce_status_chek(status, 200)
    if response_json != '':
        reqres_responce.responce_schema_validate(response_json, schema)


@pytest.mark.parametrize('email, password',[('eve.holt@reqres.in', 'pistol'), ('eve.holt@reqres.in', None)])
@allure.feature('API: other requests')
@allure.story('API: post register schema validate')
def test_user_register_schema_validate(email, password):
    if password != None:
        payload = {"email": email, "password": password}
    else:
        payload = {"email": email}
    response = reqres_session.post('api/register', json=payload)

    schema_success = load_json_schema('post_register_success.json')
    schema_unsuccess = load_json_schema('post_register_unsuccess.json')
    status = response.status_code
    response_json = reqres_responce.responce_json_get(response)

    if password != None:
        reqres_responce.responce_status_chek(status, 200)
    else:
        reqres_responce.responce_status_chek(status, 400)

    if response_json != '':
        if password != None:
            reqres_responce.responce_schema_validate(response_json, schema_success)
        else:
            reqres_responce.responce_schema_validate(response_json,schema=schema_unsuccess)


@pytest.mark.parametrize('email, password',[('eve.holt@reqres.in', 'cityslicka'), ('eve.holt@reqres.in', None)])
@allure.feature('API: other requests')
@allure.story('API: post login schema validate')
def test_user_login_schema_validate(email, password):
    if password != None:
        payload = {"email": email, "password": password}
    else:
        payload = {"email": email}
    response = reqres_session.post('api/login', json=payload)

    schema_success = load_json_schema('post_login_success.json')
    schema_unsuccess = load_json_schema('post_login_unsuccess.json')
    status = response.status_code
    response_json = reqres_responce.responce_json_get(response)

    if password != None:
        reqres_responce.responce_status_chek(status, 200)
    else:
        reqres_responce.responce_status_chek(status, 400)

    if response_json != '':
        if password != None:
            reqres_responce.responce_schema_validate(response_json, schema_success)
        else:
            reqres_responce.responce_schema_validate(response_json,schema=schema_unsuccess)


@allure.feature('API: other requests')
@allure.story('API: get delay schema validate')
def test_delay_json_schema_validate():
    payload = {'delay': 3}
    response = reqres_session.get('api/users', params=payload)

    schema = load_json_schema('get_delay.json')
    status = response.status_code
    response_json = reqres_responce.responce_json_get(response)

    reqres_responce.responce_status_chek(status, 200)
    if response_json != '':
        reqres_responce.responce_schema_validate(response_json, schema)
